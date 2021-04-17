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

        :param str qd:  A date range query parameter.

            Accepts:  ``since:YYYYMMDD``, ``between:YYYYMMDDhhmmss,YYYYMMDDhhmmss``, and ``daysBack:N``.

            Examples:  ``since:20190601``, ``between:20191001000000,20191002060000``, ``daysBack:30``

        :param str campaignIdentifier:  The campaign identifier value to search for.
        :param str fromAddress:  The from address to search for
        :param int childAccountId:  The child account to narrow results
        :param domain:  List of strings.  Narrow results to certain domains that are under this API key
            (multiple allowed)
        :param str headerKey:  Campaigns that used a specific header key
        :param str headerValue:  Campaigns that used a specific header value
        :param str subject:  Subject search criteria
        :param str body:  Body search criteria
        :param int page:  The page to query for in pagination
        :param int per_page:  The amount of records per page you wish to query for (max 100)
        :param str order:  The property to sort by ('property' for decending, '-property' for ascending)

            Accepts:  ``firstSeen``, ``-firstSeen``, ``lastSeen``, ``-lastSeen``, ``inbox``, ``-inbox``, ``spam``,
            ``-spam``
        :param str embed:  The objects within the return model you wish to embed.

            Accepts:  ``sendingIps``, ``gmailCategories``, ``authInbox``

        :return:  A ``list`` object of ``dict`` containing details for a campaign.
        """

        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_campaign_by_id(self, campaignId, **kwargs):
        """
        Get campaign details by querying campaign identifier.

        :param int campaignId: Integer campaign identifier
        :param int childAccountId:  The child account to narrow results
        :param str embed:  The objects within the return model you wish to embed.

            Accepts:  ``sendingIps``, ``gmailCategories``, ``authInbox``

        :return:  A ``dict`` object containing details of the specified campaign.
        """

        endpoint = "/" + str(campaignId)
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_ip_stats(self, **kwargs):
        """
        Get statistics for all IP addresses in your account

        :param str qd:  A date range query parameter.

            Accepts:  ``since:YYYYMMDD``, ``between:YYYYMMDDhhmmss,YYYYMMDDhhmmss``, and ``daysBack:N``.

            Examples:  ``since:20190601``, ``between:20191001000000,20191002060000``, ``daysBack:30``
        :param childAccountId:  List of int.  The child account(s) to narrow results
        :param ipAddress:  List of strings.  The ip address to narrow results to (multiple allowed)
        :param domain:  List of strings.  Narrow results to certain domains that are under this API key (multiple
            allowed)
        :param bool limitToSpecifiedDomains:  Only include data for the supplied domains (vs all domains using the IPs)
        :param int page:  The page to query for in pagination
        :param int per_page:  The amount of records per page you wish to query for (max 100)

        :return:  A ``list`` object of ``dict`` containing campaign details for each IP address.
        """

        endpoint = "/sendingIps"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse
