import json
from .base import Resource


class Ping(Resource):
    key = "ping"

    def ping_service(self):
        """
        Ping the server to verify it is reachable
        :return:  'string' object
        """

        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters({}, {})
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse
