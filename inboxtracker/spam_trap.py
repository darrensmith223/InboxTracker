from .base import Resource

param_model = {
    'childAccountId',
    'partnerAccountId',
    'qd',
    'domain',
    'trapSource',
    'trapType',
    'ipAddress',
    'page',
    'per_page',
    'order',
    'campaignIdentifier',
    'subjectLine',
    'fromAddresses'
}

class SpamTrap:

    def __init__(self, base_uri, api_key):
        self.available_domains = AvailableDomains(base_uri, api_key)
        self.domain = Domain(base_uri, api_key)
        self.ip = IP(base_uri, api_key)
        self.ping = Ping(base_uri, api_key)


class AvailableDomains(Resource):
    key = "available-domains"

    def get_available_domains(self, **kwargs):
        """
        Gets the list of domains associated to your account/child accounts.

        :param int childAccountId: The child account to narrow results. This parameter is optional unless the API
            key is configured to require the childAccountId parameter.
        :param str partnerAccountId: The partnerAccountId associated with the childAccountId. This parameter is
            required by API keys configured to require the childAccountId-partnerAccountId parameters; otherwise the
            parameter is ignored.

        :return:  A ``list`` object of ``dict`` containing the domains available on the account.
        """
        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse


class Domain(Resource):
    key = "domain"

    def get_traps_by_domain(self, **kwargs):
        """
        Get a list of spam trap hits grouped by domain.

        :param str qd: A date range query parameter.

            Accepts:  ``since:YYYYMMDD``, ``between:YYYYMMDDhhmmss,YYYYMMDDhhmmss``, and ``daysBack:N``.

            Examples:  ``since:20190601``, ``between:20191001000000,20191002060000``, ``daysBack:30``

        :param domain: List of strings. The domains to filter on.
        :param trapSource: List of strings. The trap sources to filter on.

            Accepts:  ``ABUSIX``, ``CLOUDMARK``, ``SNDS``, ``GTN_PASSIVE``, ``GTN_ACTIVE``

        :param trapType: List of strings. The trap types to filter on.

            Accepts:  ``PRISTINE``, ``MIXED``, ``RECYCLED``, ``PARKED``, ``TYPO``

        :param ipAddress: List of strings. IP addresses to filter on. Accepts IP ranges, each IP range must be no
            larger that 256 IPs.
        :param int page: The page to query for in pagination.
        :param int per_page: The amount of records per page you wish to query for (max 100)
        :param str order: The property to sort by ('property' for decending, '-property' for ascending)

            Accepts:  ``domain``, ``-domain``, ``hitCountTotal``, ``-hitCountTotal``, ``hitCountRecycled``,
            ``-hitCountRecycled``, ``hitCountMixed``, ``-hitCountMixed``, ``hitCountParked``, ``-hitCountParked``,
            ``hitCountPristine``, ``-hitCountPristine``, ``hitCountTypo``, and ``-hitCountTypo``.

        :return:  A ``list`` object of ``dict`` containing spam trap hit counts
        """
        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_domain_rollup(self, **kwargs):
        """
        Gets a list of aggregated detailed spam trap information and associated campaign information for sending
            domains. A details link is returned which can be used to retrieve the details for each of the spam trap
            hits included in the aggregated spam trap information.

        :param str qd: A date range query parameter.

            Accepts:  ``since:YYYYMMDD``, ``between:YYYYMMDDhhmmss,YYYYMMDDhhmmss``, and ``daysBack:N``.

            Examples:  ``since:20190601``, ``between:20191001000000,20191002060000``, ``daysBack:30``

        :param domain: List of strings. The domains to filter on.
        :param trapSource: List of strings. The trap sources to filter on.

            Accepts:  ``ABUSIX``, ``CLOUDMARK``, ``SNDS``, ``GTN_PASSIVE``, ``GTN_ACTIVE``

        :param trapType: List of strings. The trap types to filter on.

            Accepts:  ``PRISTINE``, ``MIXED``, ``RECYCLED``, ``PARKED``, ``TYPO``

        :param ipAddress: List of strings. IP addresses to filter on. Accepts IP ranges, each IP range must be no
            larger that 256 IPs.
        :param campaignIdentifier: List of strings. The campaign identifier used to identify the campaign when using a
            Campaign Identification method other than Subject/Date. Use the subjectLine filter if a domain is using
            Subject/Date to identify campaigns.
        :param subjectLine: List of strings. The subject lines to filter on.
        :param fromAddresses: List of strings. The "from" addresses to filter on.
        :param int page: The page to query for in pagination.
        :param int per_page: The amount of records per page you wish to query for (max 100)
        :param str order: The property to sort by ('property' for decending, '-property' for ascending)

            Accepts:  ``domain``, ``-domain``, ``hitCountTotal``, ``-hitCountTotal``, ``firstSeen``, ``-firstSeen``,
            ``lastSeen``, ``-lastSeen``, ``hitSources``, ``-hitSources``, ``trapTypes``, ``-trapTypes``,
            ``subjectLine``, ``-subjectLine``, ``campaign``, and ``-campaign``.

        :return: A ``list`` object of ``dict`` containing spam trap information
        """
        endpoint = "/rollup"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_domain_rollup_details(self, **kwargs):
        """
        Gets a list of spam trap hits with detailed information. It is recommended that this endpoint be accessed
            using the details link returned by the domain/rollup endpoint. To retrieve details for a campaign you must
            set a campaignId OR subjectLine filter for the campaign of interest. If you do not set a campaignId OR
            subjectLine filter you will only get detailed hits without an associated campaign.

        :param str qd: A date range query parameter.

            Accepts:  ``since:YYYYMMDD``, ``between:YYYYMMDDhhmmss,YYYYMMDDhhmmss``, and ``daysBack:N``.

            Examples:  ``since:20190601``, ``between:20191001000000,20191002060000``, ``daysBack:30``

        :param domain: List of strings. The domains to filter on.
        :param trapSource: List of strings. The trap sources to filter on.

            Accepts:  ``ABUSIX``, ``CLOUDMARK``, ``SNDS``, ``GTN_PASSIVE``, ``GTN_ACTIVE``

        :param trapType: List of strings. The trap types to filter on.

            Accepts:  ``PRISTINE``, ``MIXED``, ``RECYCLED``, ``PARKED``, ``TYPO``

        :param ipAddress: List of strings. IP addresses to filter on. Accepts IP ranges, each IP range must be no
            larger that 256 IPs.
        :param int campaignId: The campaign id used to filter on.
        :param str subjectLine: The subject line to filter on.
        :param fromAddresses: List of strings. The "from" addresses to filter on.
        :param int page: The page to query for in pagination.
        :param int per_page: The amount of records per page you wish to query for (max 100)
        :param str order: The property to sort by ('property' for decending, '-property' for ascending)

            Accepts:  ``domain``, ``-domain``, ``hitCountTotal``, ``-hitCountTotal``, ``firstSeen``, ``-firstSeen``,
            ``lastSeen``, ``-lastSeen``, ``ipAddress``, ``-ipAddress``, ``hitSources``, ``-hitSources``,
            ``subjectLine``, ``-subjectLine``, ``fromAddress``, ``-fromAddress``, ``trapAgeDays``, and ``-trapAgeDays``.

        :return: A ``list`` object of ``dict`` containing spam trap details for a campaign
        """
        endpoint = "/rollup/details"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse


class IP(Resource):
    key = "ip"

    def get_traps_by_ip(self, **kwargs):
        """
        Get a list of spam trap hits grouped by IP address.

        :param str qd: A date range query parameter.

            Accepts:  ``since:YYYYMMDD``, ``between:YYYYMMDDhhmmss,YYYYMMDDhhmmss``, and ``daysBack:N``.

            Examples:  ``since:20190601``, ``between:20191001000000,20191002060000``, ``daysBack:30``

        :param domain: List of strings. The domains to filter on.
        :param trapSource: List of strings. The trap sources to filter on.

            Accepts:  ``ABUSIX``, ``CLOUDMARK``, ``SNDS``, ``GTN_PASSIVE``, ``GTN_ACTIVE``

        :param trapType: List of strings. The trap types to filter on.

            Accepts:  ``PRISTINE``, ``MIXED``, ``RECYCLED``, ``PARKED``, ``TYPO``

        :param ipAddress: List of strings. IP addresses to filter on. Accepts IP ranges, each IP range must be no
            larger that 256 IPs.
        :param int page: The page to query for in pagination.
        :param int per_page: The amount of records per page you wish to query for (max 100)
        :param str order: The property to sort by ('property' for decending, '-property' for ascending)

            Accepts:  ``ipAddress``, ``-ipAddress``, ``hitCountTotal``, ``-hitCountTotal``, ``hitCountRecycled``,
            ``-hitCountRecycled``, ``hitCountMixed``, ``-hitCountMixed``, ``hitCountParked``, ``-hitCountParked``,
            ``hitCountPristine``, ``-hitCountPristine``, ``hitCountTypo``, and ``-hitCountTypo``

        :return:  A ``list`` object of ``dict`` containing aggregated spam trap data
        """
        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_ip_rollup(self, **kwargs):
        """
        Gets a list of aggregated detailed spam trap information and associated campaign information by IP address for
            sending domains. A details link is returned which can be used to retrieve the details for each of the spam
            trap hits included in the aggregated spam trap information.

        :param str qd: A date range query parameter.

            Accepts:  ``since:YYYYMMDD``, ``between:YYYYMMDDhhmmss,YYYYMMDDhhmmss``, and ``daysBack:N``.

            Examples:  ``since:20190601``, ``between:20191001000000,20191002060000``, ``daysBack:30``

        :param domain: List of strings. The domains to filter on.
        :param trapSource: List of strings. The trap sources to filter on.

            Accepts:  ``ABUSIX``, ``CLOUDMARK``, ``SNDS``, ``GTN_PASSIVE``, ``GTN_ACTIVE``

        :param trapType: List of strings. The trap types to filter on.

            Accepts:  ``PRISTINE``, ``MIXED``, ``RECYCLED``, ``PARKED``, ``TYPO``

        :param ipAddress: List of strings. IP addresses to filter on. Accepts IP ranges, each IP range must be no
            larger that 256 IPs.
        :param campaignIdentifier: List of strings. The campaign identifier used to identify the campaign when using a
            Campaign Identification method other than Subject/Date. Use the subjectLine filter if a domain is using
            Subject/Date to identify campaigns.
        :param subjectLine: List of strings. The subject lines to filter on.
        :param fromAddresses: List of strings. The "from" addresses to filter on.
        :param int page: The page to query for in pagination.
        :param int per_page: The amount of records per page you wish to query for (max 100)
        :param str order: The property to sort by ('property' for decending, '-property' for ascending)

            Accepts:  ``ipAddress``, ``-ipAddress``, ``hitCountTotal``, ``-hitCountTotal``, ``firstSeen``,
            ``-firstSeen``, ``lastSeen``, ``-lastSeen``, ``hitSources``, ``-hitSources``, ``trapTypes``, ``-trapTypes``,
            ``subjectLine``, ``-subjectLine``, ``campaign``,  and ``-campaign``.

        :return: A ``list`` object of ``dict`` containing spam trap data
        """
        endpoint = "/rollup"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_ip_rollup_details(self, **kwargs):
        """
        Gets a list of spam trap hits with detailed information. It is recommended that this endpoint be accessed
            using the details link returned by the ip/rollup endpoint. To retrieve details for a campaign you must set
            a campaignId OR subjectLine filter for the campaign of interest. If you do not set a campaignId OR
            subjectLine filter you will only get detailed hits without an associated campaign.

        :param str qd: A date range query parameter.

            Accepts:  ``since:YYYYMMDD``, ``between:YYYYMMDDhhmmss,YYYYMMDDhhmmss``, and ``daysBack:N``.

            Examples:  ``since:20190601``, ``between:20191001000000,20191002060000``, ``daysBack:30``

        :param domain: List of strings. The domains to filter on.
        :param trapSource: List of strings. The trap sources to filter on.

            Accepts:  ``ABUSIX``, ``CLOUDMARK``, ``SNDS``, ``GTN_PASSIVE``, ``GTN_ACTIVE``

        :param trapType: List of strings. The trap types to filter on.

            Accepts:  ``PRISTINE``, ``MIXED``, ``RECYCLED``, ``PARKED``, ``TYPO``

        :param ipAddress: List of strings. IP addresses to filter on. Accepts IP ranges, each IP range must be no
            larger that 256 IPs.
        :param int campaignId: The campaign id used to filter on.
        :param str subjectLine: The subject line to filter on.
        :param fromAddresses: List of strings. The "from" addresses to filter on.
        :param int page: The page to query for in pagination.
        :param int per_page: The amount of records per page you wish to query for (max 100)
        :param str order: The property to sort by ('property' for decending, '-property' for ascending)

            Accepts:  ``hitCountTotal``, ``-hitCountTotal``, ``firstSeen``, ``-firstSeen``, ``lastSeen``, ``-lastSeen``,
            ``ipAddress``, ``-ipAddress``, ``hitSources``, ``-hitSources``, ``subjectLine``,``-subjectLine``,
            ``fromAddress``, ``-fromAddress``, ``trapAgeDays``,  and ``-trapAgeDays``.

        :return: A ``list`` object of ``dict`` containing spam trap data.
        """
        endpoint = "/rollup/details"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse


class Ping(Resource):
    key = "ping"

    def ping_service(self):
        """
        Ping the service to verify it is reachable.

        :return:  A ``str`` object.  A successful ping will return the string 'pong'.
        """
        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters({}, {})
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse
