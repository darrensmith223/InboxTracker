from .base import Resource


class Regions(Resource):
    key = "regions"

    param_model = {
    }

    def get_regions(self):
        """
        Gets current list of regions supported by the system.

        :return: A ``list`` object of available regions as ``str``.  See
            `Current Regions <https://inboxtracker.readthedocs.io/en/latest/resources/regions.html#supported-regions>`_
            for an updated list of supported regions.
        """

        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters({}, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse