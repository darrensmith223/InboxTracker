import requests
import json


def GetCampaignById(apiKey, campaignId, embed=None):
    """
    Get campaign details by querying campaign identifier.
    :param apiKey: API key to authenticate
    :param campaignId: Integer campaign identifier
    :param embed:  The objects within the return model you wish to embed.
                    Embed parameter accepts: sendingIps,gmailCategories,authInbox
    :return:  'dict' object.
    """

    apiUrl = "http://api.edatasource.com/v4/inbox/campaigns/"+campaignId
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetCampaigns(apiKey, qd, campaignIdentifier=None, fromAddress=None, childAccountId=None, domain=None, page=None,
                 per_page=None, order=None, embed=None):
    """
    Get all campaign details for a given time period
    :param apiKey: API key to authenticate
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
    :param campaignIdentifier:  The campaign identifier value to search for.
    :param fromAddress:  The from address to search for
    :param childAccountId:  The child account under the API key given to narrow results to
    :param domain:  (Array) Narrow results to certain domains that are under this API key (multiple allowed)
    :param page:  The page to query for in pagination
    :param per_page:  The amount of records per page you wish to query for (max 100)
    :param order:  The property to sort by ('property' for decending, '-property' for ascending)
    :param embed:  The objects within the return model you wish to embed.
                    Embed parameter accepts: sendingIps,gmailCategories,authInbox
    :return:  'list' object
    """

    apiUrl = "http://api.edatasource.com/v4/inbox/campaigns"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters, campaignIdentifier=campaignIdentifier, fromAddress=fromAddress,
                                   childAccountId=childAccountId, domain=domain, page=page, per_page=per_page,
                                   order=order, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetDeliverabilityByDomain(apiKey, domain, qd, embed=None):
    """
    Get deliverability information for a domain
    :param apiKey: API key to authenticate
    :param domain:  The domain under the API key given to narrow results to
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
    :param embed:  The objects within the return model you wish to embed.
                    Embed parameter accepts: gmailCategories, deliveryIndex, ipDetails
    :return:  'dict' object
    """
    apiUrl = "http://api.edatasource.com/v4/inbox/deliverability/"+domain
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetDomainsAvailable(apiKey, childAccountId=None):
    """
    Get all domains available within your account
    :param apiKey: API key to authenticate
    :param childAccountId:  The child account under the API key given to narrow results to
    :return:  'list' object
    """
    apiUrl = "http://api.edatasource.com/v4/inbox/domains/available"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, childAccountId=childAccountId)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetIntelliseed(apiKey, childAccountId=None, type=None):
    """
    Get an updated Intelliseed list
    :param apiKey: API key to authenticate
    :param childAccountId:  The child account under the API key given to narrow results to
    :param type:  The type of IntelliSeed™ list to pull (public, private, or exclusive) default is private
    :return:  'list' object
    """
    apiUrl = "http://api.edatasource.com/v4/inbox/intelliseed"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, childAccountId=childAccountId, type=type)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetIntelliseedLastUpdate(apiKey):
    """
    Get the time of the last update to Intelliseed List
    :param apiKey: API key to authenticate
    :return:  'list' object
    """
    apiUrl = "http://api.edatasource.com/v4/inbox/intelliseed/lastUpdate"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetPing(apiKey):
    """
    Ping the server to verify it is reachable
    :param apiKey: API key to authenticate
    :return:  'string' object
    """

    apiUrl = "http://api.edatasource.com/v4/inbox/ping"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return apiResponse


def GetSeeds(apiKey, childAccountId=None):
    """
    Get an updated Traditional Seeds list
    :param apiKey: API key to authenticate
    :param childAccountId:  The child account under the API key given to narrow results to
    :return:  'list' object
    """

    apiUrl = "http://api.edatasource.com/v4/inbox/seeds"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, childAccountId=childAccountId)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetSeedsLastUpdate(apiKey):
    """
    Get the time of the last update to the Traditional Seeds list
    :param apiKey: API key to authenticate
    :return:  'list' object
    """

    apiUrl = "http://api.edatasource.com/v4/inbox/seeds/lastUpdate"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetSeedsUsage(apiKey):
    """
    Get the Traditional Seeds usage information for your account
    :param apiKey: API key to authenticate
    :return:  'list' object
    """

    apiUrl = "http://api.edatasource.com/v4/inbox/seeds/usage"

    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetSendingIPs(apiKey, qd, childAccountId=None, ipAddress=None, domain=None, limitToSpecifiedDomains=None,
                  page=None, per_page=None, order=None):
    """
    Get statistics for all IP addresses in your account
    :param apiKey: API key to authenticate
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
    :param childAccountId:  (Array) The child account under the API key given to narrow results to
    :param ipAddress:  (Array) The ip address to narrow results to (multiple allowed)
    :param domain:  (Array) Narrow results to certain domains that are under this API key (multiple allowed)
    :param limitToSpecifiedDomains:  Only include data for the supplied domains (vs all domains using the IPs)
    :param page:  The page to query for in pagination
    :param per_page:  The amount of records per page you wish to query for (max 100)
    :param order:  The property to sort by ('property' for decending, '-property' for ascending)
    :return:  'list' object
    """

    apiUrl = "http://api.edatasource.com/v4/inbox/campaigns/sendingIps"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters, childAccountId=childAccountId, ipAddress=ipAddress, domain=domain,
                                   limitToSpecifiedDomains=limitToSpecifiedDomains, page=page, per_page=per_page,
                                   order=order)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def SetOptionalParams(parameters, embed=None, campaignIdentifier=None,
                fromAddress=None, childAccountId=None, domain=None, page=None,
                per_page=None, order=None, type=None, ipAddress=None, limitToSpecifiedDomains=None):
    """
    Set optional parameters for the API calls
    :param parameters:  the parameters to be used in the API calls
    :param embed:  The objects within the return model you wish to embed.
    :param campaignIdentifier:  The campaign identifier value to search for.
    :param fromAddress:  The from address to search for
    :param childAccountId:  The child account to search for
    :param domain:  The domain to search for
    :param page:  The page to query for in pagination
    :param per_page:  The amount of records per page you wish to query for (max 100)
    :param order: The property to sort by ('property' for decending, '-property' for ascending)
    :param type:  The type of IntelliSeed™ list to pull (public, private, or exclusive) default is private
    :param ipAddress:  The IP address to search for
    :param limitToSpecifiedDomains:  Only include data for the supplied domains (vs all domains using the IPs)
    :return: 'dict' object
    """
    arguments = locals()

    for k, v in arguments.items():
        if v is not None and k != "parameters":
            parameters[k] = v

    return parameters


def MakeAPICall(apiUrl, parameters):
    """
    Make a GET API call to the server
    :param apiUrl: The API URL to call
    :param parameters:  The parameters to use in the API call
    :return: 'response' object
    """

    response = requests.get(apiUrl, parameters)

    if response.status_code == 200:
        return response.text
    else:
        return "Problem Getting Data: " + response.reason
