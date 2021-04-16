from .base import Resource


class Deliverability(Resource):

    key = "deliverability"

    param_model = {
        'childAccountId',
        'domain',
        'embed',
        'qd'
    }

    def get_deliverability_by_domain(self, domain, **kwargs):
        """
        Get deliverability information for a domain

        :param str domain:  The domain to show results for
        :param str qd:  A date range query parameter.

            Accepts:  ``since:YYYYMMDD``, ``between:YYYYMMDDhhmmss,YYYYMMDDhhmmss``, and ``daysBack:N``.

            Examples:  ``since:20190601``, ``between:20191001000000,20191002060000``, ``daysBack:30``
        :param int childAccountId:  The child account to narrow results
        :param str embed:  The objects within the return model you wish to embed.


            Accepts:  ``gmailCategories``, ``deliveryIndex``, ``ipDetails``

        :return:  A ``dict`` object containing details for a given domain.
        """

        endpoint = "/" + str(domain)
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse
