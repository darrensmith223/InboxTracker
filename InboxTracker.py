import requests
import json
import csv


def GetCampaignById(apiKey, campaignId, embed=None):
    apiUrl = "http://api.edatasource.com/v4/inbox/campaigns/"+campaignId
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters, embed=embed)

    return json.loads(apiResponse)


def GetCampaigns(apiKey, qd, campaignIdentifier=None, fromAddress=None, childAccountId=None, domain=None, page=None, per_page=None, order=None, embed=None):
    apiUrl = "http://api.edatasource.com/v4/inbox/campaigns"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    apiResponse = MakeAPICall(apiUrl, parameters, campaignIdentifier=campaignIdentifier, fromAddress=fromAddress, childAccountId=childAccountId, domain=domain, page=page, per_page=per_page, order=order, embed=embed)

    return json.loads(apiResponse)


def GetDeliverabilityByDomain(apiKey, domain, qd, embed=None):
    apiUrl = "http://api.edatasource.com/v4/inbox/deliverability/"+domain
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    apiResponse = MakeAPICall(apiUrl, parameters, embed=embed)

    return json.loads(apiResponse)


def GetDomainsAvailable(apiKey, childAccountId=None):
    apiUrl = "http://api.edatasource.com/v4/inbox/domains/available"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters, childAccountId=childAccountId)

    return json.loads(apiResponse)


def GetIntelliseed(apiKey, childAccountId=None, type=None):
    apiUrl = "http://api.edatasource.com/v4/inbox/intelliseed"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters, childAccountId=childAccountId, type=type)

    return json.loads(apiResponse)


def GetIntelliseedLastUpdate(apiKey):
    apiUrl = "http://api.edatasource.com/v4/inbox/intelliseed/lastUpdate"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetPing(apiKey):
    apiUrl = "http://api.edatasource.com/v4/inbox/ping"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters)

    return apiResponse


def GetSeeds(apiKey, childAccountId=None):
    apiUrl = "http://api.edatasource.com/v4/inbox/seeds"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters, childAccountId=childAccountId)

    return json.loads(apiResponse)


def GetSeedsLastUpdate(apiKey):
    apiUrl = "http://api.edatasource.com/v4/inbox/seeds/lastUpdate"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetSeedsUsage(apiKey):
    apiUrl = "http://api.edatasource.com/v4/inbox/seeds/usage"

    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetSendingIPs(apiKey, qd, childAccountId=None, ipAddress=None, domain=None, limitToSpecifiedDomains=None, page=None, per_page=None, order=None):
    apiUrl = "http://api.edatasource.com/v4/inbox/campaigns/sendingIps"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    apiResponse = MakeAPICall(apiUrl, parameters, childAccountId=childAccountId, ipAddress=ipAddress, domain=domain, limitToSpecifiedDomains=limitToSpecifiedDomains, page=page, per_page=per_page, order=order)

    return json.loads(apiResponse)


def MakeAPICall(apiUrl, parameters, embed=None, campaignIdentifier=None,
                fromAddress=None, childAccountId=None, domain=None, page=None,
                per_page=None, order=None, type=None, ipAddress=None, limitToSpecifiedDomains=None):

    parameters = AddOptionalParameter(parameters, campaignIdentifier, "campaignIdentifier")
    parameters = AddOptionalParameter(parameters, childAccountId, "childAccountId")
    parameters = AddOptionalParameter(parameters, domain, "domain")
    parameters = AddOptionalParameter(parameters, embed, "embed")
    parameters = AddOptionalParameter(parameters, fromAddress, "fromAddress")
    parameters = AddOptionalParameter(parameters, ipAddress, "ipAddress")
    parameters = AddOptionalParameter(parameters, limitToSpecifiedDomains, "limitToSpecifiedDomains")
    parameters = AddOptionalParameter(parameters, order, "order")
    parameters = AddOptionalParameter(parameters, page, "page")
    parameters = AddOptionalParameter(parameters, per_page, "per_page")
    parameters = AddOptionalParameter(parameters, type, "type")

    response = requests.get(apiUrl, parameters)

    if response.status_code == 200:
        return response.text
    else:
        return response.status_code


def AddOptionalParameter(paramDict, optionalParam, optParamName):

    if optionalParam is not None:
        paramDict[optParamName] = optionalParam

    return paramDict
