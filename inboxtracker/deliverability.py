import json
from .base import Resource


class Deliverability(Resource):

    key = "deliverability"

    param_model = {
        'domain',
        'embed',
        'qd'
    }

    def get_deliverability_by_domain(self, domain, **kwargs):
        """
        Get deliverability information for a domain
        :param domain:  The domain under the API key given to narrow results to
        :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                    and "daysBack:N".
                    Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
        :param embed:  The objects within the return model you wish to embed.
                        Embed parameter accepts: gmailCategories, deliveryIndex, ipDetails
        :return:  'dict' object
        """

        endpoint = "/" + str(domain)
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse
