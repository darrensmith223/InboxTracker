from .base import Resource


class Domains(Resource):
    key = "domains"

    param_model = {
        'childAccountId'
    }

    def get_available_domains(self, **kwargs):
        """
        Get all domains available within your account

        :param childAccountId:  The child account to narrow results

        :return:  'list' object
        """

        endpoint = "/available"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

