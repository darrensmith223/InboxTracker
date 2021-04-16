import json
from .base import Resource


class Campaigns(Resource):
    key = "campaigns"

    param_model = {
        'body',
        'campaignIdentifier',
        'childAccountId',
        'domain',
        'embed',
        'fromAddress',
        'headerKey',
        'headerValue',
        'ipAddress',
        'limitToSpecifiedDomains',
        'order',
        'page',
        'per_page',
        'qd',
        'subject'
    }

    def get_campaigns(self, **kwargs):
        """
        Get all campaign details for a given time period
        :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                    and "daysBack:N".
                    Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
        :param campaignIdentifier:  The campaign identifier value to search for.
        :param fromAddress:  The from address to search for
        :param childAccountId:  The child account to narrow results
        :param domain:  (Array) Narrow results to certain domains that are under this API key (multiple allowed)
        :param page:  The page to query for in pagination
        :param per_page:  The amount of records per page you wish to query for (max 100)
        :param order:  The property to sort by ('property' for decending, '-property' for ascending)
        :param embed:  The objects within the return model you wish to embed.
                        Embed parameter accepts: sendingIps,gmailCategories,authInbox
        :return:  'list' object
        """

        endpoint = ""  # e.g. "/sendingIps"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_campaign_by_id(self, campaignId, **kwargs):
        """
        Get campaign details by querying campaign identifier.
        :param campaignId: Integer campaign identifier
        :param embed:  The objects within the return model you wish to embed.
                        Embed parameter accepts: sendingIps,gmailCategories,authInbox
        :return:  'dict' object.
        """

        endpoint = "/" + str(campaignId)
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_ip_stats(self, **kwargs):
        """
        Get statistics for all IP addresses in your account
        :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                    and "daysBack:N".
                    Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
        :param childAccountId:  (Array) The child account(s) to narrow results
        :param ipAddress:  (Array) The ip address to narrow results to (multiple allowed)
        :param domain:  (Array) Narrow results to certain domains that are under this API key (multiple allowed)
        :param limitToSpecifiedDomains:  Only include data for the supplied domains (vs all domains using the IPs)
        :param page:  The page to query for in pagination
        :param per_page:  The amount of records per page you wish to query for (max 100)
        :param order:  The property to sort by ('property' for decending, '-property' for ascending)
        :return:  'list' object
        """

        endpoint = "/sendingIps"  # e.g. "/sendingIps"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse
