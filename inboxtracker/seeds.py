from .base import Resource


class Seeds(Resource):
    key = "seeds"

    param_model = {
        'childAccountId'
    }

    def get_last_update(self, **kwargs):
        """
        Get the time of the last update to the Traditional Seeds list

        :param int childAccountId:  The child account to narrow results

        :return:  A ``list`` object of ``dict`` containing the seed list ID, account ID, and last updated date
        """

        endpoint = "/lastUpdate"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_usage(self, **kwargs):
        """
        Get the Traditional Seeds usage information for your account

        :param int childAccountId:  The child account to narrow results

        :return:  A ``list`` object of ``dict`` containing the usage details of the seed list.
        """

        endpoint = "/usage"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_seeds(self, **kwargs):
        """
        Get an updated Traditional Seeds list

        :param int childAccountId:  The child account to narrow results

        :return:  A ``list`` object of ``dict`` containing the details of the seeds, such as the email address,
            location, and ISP.
        """

        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse
