import copy
import requests
import inboxtracker
from .exceptions import InboxTrackerAPIException


class RequestsTransport(object):
    def __init__(self):
        import requests
        self.sess = requests.Session()

    def request(self, method, uri, params, **kwargs):
        response = self.sess.request(method, uri, params=params, **kwargs)

        if response.status_code == 204:
            return True
        if not response.ok:
            raise InboxTrackerAPIException(response)
        try:
            if 'results' in response.json():
                return response.json()['results']
        except:
            return response.text
        return response.json()


class Resource(object):
    key = ""

    def __init__(self, base_uri, api_key, transport_class=RequestsTransport):
        self.base_uri = base_uri
        self.api_key = api_key
        self.transport = transport_class()

    @property
    def uri(self):
        return "%s/%s" % (self.base_uri, self.key)

    def request(self, method, uri, params, **kwargs):
        headers = {
            'User-Agent': 'python-inboxtracker/' + inboxtracker.__version__,
            'Content-Type': 'application/json'
        }
        response = self.transport.request(method, uri, params=params, headers=headers,
                                          **kwargs)
        return response

    def SetParameters(self, args, model_remap):
        parameters = {"Authorization": self.api_key}

        model = copy.deepcopy(args)

        # Intersection of keys that need to be remapped
        data_remap_keys = set(model_remap).intersection(model.keys())

        for k in data_remap_keys:
            parameters[k] = model[k]

        return parameters

    def translate_keys(self, args, model_remap):
        model = copy.deepcopy(args)
        # Intersection of keys that need to be remapped
        model_remap_keys = frozenset(model_remap.keys())
        data_remap_keys = model_remap_keys.intersection(model.keys())

        for from_key in data_remap_keys:
            # Remap model keys to match API
            if from_key in model:
                to_model = model
                to_key = model_remap[from_key]
                if '/' in to_key:
                    # Nested within a dict
                    into_list = to_key.split('/')
                    to_key = into_list[-1]
                    to_model = model.setdefault(into_list[0], {})

                # Move from current key and place into new key
                to_model[to_key] = model.pop(from_key)

        return model

    def MakeAPICall(self, apiUrl, parameters):
        """
        Make a GET API call to the server
        :param apiUrl: The API URL to call
        :param parameters:  The parameters to use in the API call
        :return: 'response' object
        """

        response = requests.get(apiUrl, parameters)

        if response.status_code == 200:
            return response.text
        else:
            return "Problem Getting Data: " + response.reason

    def get(self):
        raise NotImplementedError

    def list(self):
        raise NotImplementedError

    def create(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
