import json
from .base import Resource


class Intelliseeds(Resource):
    key = "intelliseed"

    param_model = {
        'childAccountId',
        'percentOfList',
        'regions',
        'simulatedEngagementOption',
        'type'
    }

    def get_intelliseeds(self, **kwargs):
        """
        Get an updated IntelliSeed list

        :param childAccountId:  The child account to narrow results
        :param type:  The type of IntelliSeed list to pull (public, private, or exclusive) default is private

        :return:  'list' object
        """

        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_last_update(self, **kwargs):
        """
        Get the time of the last update to IntelliSeed List

        :param childAccountId:  The child account to narrow results

        :return:  'list' object
        """

        endpoint = "/lastUpdate"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_filter_sets(self, **kwargs):
        """
        Get the list of IntelliSeed filter sets configured for an account

        :param childAccountId: The child account to narrow results

        :return: 'list' object
        """

        endpoint = "/filter_sets"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_intelliseeds_filtered(self, filterSetId, **kwargs):
        """
        Gets the latest IntelliSeed list associated with the filter set id provided

        :param filterSetId: The id of the IntelliSeed filter set

        :param childAccountId: The child account to narrow results

        :return: 'list' object
        """

        endpoint = "/" + str(filterSetId)
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def create_intelliseed_filter(self, **kwargs):
        """
        Places a new IntelliSeed filter set under the given account

        :param name: Name of the filter set
        :param listType: Privacy level of list. Accepts: "PUBLIC", "PRIVATE"
        :param simulatedEngagementOption: Engagement level of the IntelliSeeds to include in the list.
        Accepts: "ALL", "Engaging", "Non-engaging"
        :param percentOfList: Percent of the list to include. Integer from 0-100.
        :param regions: List of regions to include.
        :param childAccountId: The child account to place filter

        :return: 'dict' object
        """

        data_model = {
            'name': 'name',
            'listType': 'listType',
            'simulatedEngagementOption': 'simulatedEngagementOption',
            'percentOfList': 'percentOfList',
            'regions': 'regions'
        }

        endpoint = "/filter_sets"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        data = self.translate_keys(kwargs, data_model)
        data = json.dumps(data)
        apiResponse = self.request("POST", apiUrl, params=parameters, data=data)

        return apiResponse

    def delete_intelliseed_filter(self, filterSetId, **kwargs):
        """
        Removes the IntelliSeed filter set using the filter set id provided

        :param filterSetId: The id of the IntelliSeed filter set
        :param childAccountId: The child account to narrow results

        :return: 'dict' object
        """

        endpoint = "/filter_sets/" + str(filterSetId)
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("DELETE", apiUrl, params=parameters)

        return apiResponse