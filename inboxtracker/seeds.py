import json
from .base import Resource


class Seeds(Resource):
    key = "seeds"

    param_model = {
        'childAccountId'
    }

    def get_last_update(self, **kwargs):
        """
        Get the time of the last update to the Traditional Seeds list
        :param childAccountId:  The child account under the API key given to narrow results to
        :return:  'list' object
        """

        endpoint = "/lastUpdate"  # e.g. "/sendingIps"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_usage(self, **kwargs):
        """
        Get the Traditional Seeds usage information for your account
        :param childAccountId:  The child account under the API key given to narrow results to
        :return:  'list' object
        """

        endpoint = "/usage"  # e.g. "/sendingIps"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_seeds(self, **kwargs):
        """
        Get an updated Traditional Seeds list
        :param childAccountId:  The child account to narrow results
        :return:  'list' object
        """

        endpoint = ""  # e.g. "/sendingIps"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse
