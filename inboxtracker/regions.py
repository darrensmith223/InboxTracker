import json
from .base import Resource


class Regions(Resource):
    key = "regions"

    param_model = {
    }

    def get_regions(self):
        """
        Gets current list of regions supported by the system.
        :return: 'list' object
        """
        endpoint = ""  # e.g. "/sendingIps"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters({}, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse