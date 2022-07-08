from .base import Resource

param_model = {
    'qd',
    'domain',
    'page',
    'per_page',
    'order'
}

class PostmasterTools:

    def __init__(self, base_uri, api_key):
        self.yahoo = Yahoo(base_uri, api_key)
        self.ping = Ping(base_uri, api_key)


class Yahoo(Resource):
    key = "yahoo"

    def get_domain_perf(self, **kwargs):
        """
        Get Yahoo Performance data rolled up at the domain level.

        :param str qd: A date range query parameter.

            Accepts:  ``since:YYYYMMDD``, ``between:YYYYMMDDhhmmss,YYYYMMDDhhmmss``, and ``daysBack:N``.

            Examples:  ``since:20190601``, ``between:20191001000000,20191002060000``, ``daysBack:30``
        :param domain: List of strings. The domains to filter on.
        :param int page: The page to query for in pagination.
        :param int per_page: The amount of records per page you wish to query for (max 100)
        :param str order: The property to sort by ('property' for decending, '-property' for ascending)

            Accepts:  ``domain``, ``-domain``, ``inboxVolume``, ``-inboxVolume``, ``spamVolume``, ``-spamVolume``,
            ``folderVolume``, ``-folderVolume``, ``errorVolume``, ``-errorVolume``, ``totalComplaints``,
            ``-totalComplaints``.

            Defaults to ``-inboxVolume``.

        :return: A ``list`` object of ``dict`` containing deliverability performance data.
        """
        endpoint = "/domain"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_ip_perf(self, **kwargs):
        """
        Get Yahoo Performance data grouped by IP address.

        :param str qd: A date range query parameter.

            Accepts:  ``since:YYYYMMDD``, ``between:YYYYMMDDhhmmss,YYYYMMDDhhmmss``, and ``daysBack:N``.

            Examples:  ``since:20190601``, ``between:20191001000000,20191002060000``, ``daysBack:30``

        :param domain: List of strings. The domains to filter on.
        :param ipAddress: List of strings. IP addresses to filter on.
        :param bool onlyComplaintErrorIps: Only return IPs that have errorVolume or totalComplaints greater than zero
            for the period given.
        :param int page: The page to query for in pagination.
        :param int per_page: The amount of records per page you wish to query for (max 100)
        :param str order: The property to sort by ('property' for decending, '-property' for ascending)

            Accepts:  ``ipAddress``, ``-ipAddress``, ``inboxVolume``, ``-inboxVolume``, ``spamVolume``, ``-spamVolume``,
            ``folderVolume``, ``-folderVolume``, ``errorVolume``, ``-errorVolume``, ``totalComplaints``,
            ``-totalComplaints``

        :return: A ``list`` object of ``dict`` containing deliverability performance data.
        """
        endpoint = "/ip"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_volume_over_time(self, **kwargs):
        """
        Volume over time for Yahoo Performance data grouped by the default grouping period:

            HOUR  when <= 7d

            DAY   when <= 31d

            WEEK  when <= 182d

            MONTH when >  182d

        :param str qd: A date range query parameter.

            Accepts:  ``since:YYYYMMDD``, ``between:YYYYMMDDhhmmss,YYYYMMDDhhmmss``, and ``daysBack:N``.

            Examples:  ``since:20190601``, ``between:20191001000000,20191002060000``, ``daysBack:30``

        :param domain: List of strings. The domains to filter on.
        :param sourceFilter: List of strings. The sources to use for inbox percentages.

            Accepts:  ``PANEL``, ``INTELLISEED``

            Defaults to all.

        :return: A ``list`` object of ``dict`` containing volume data.
        """
        endpoint = "/volume/over-time"
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
