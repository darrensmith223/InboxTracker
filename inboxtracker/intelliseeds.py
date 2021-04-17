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

        :param int childAccountId:  The child account to narrow results
        :param str type:  The type of IntelliSeed list to pull.

            Accepts:  ``PUBLIC``, ``PRIVATE``, ``EXCLUSIVE``. Default is ``PRIVATE``
        :param int percentOfList:  The integer percent, 1-100, of the IntelliSeed list to pull. Default is 100
        :param str simulatedEngagementOption:  Which engagement types of IntelliSeed accounts to include.

            Accepts:  ``ALL``, ``ENGAGING``, and ``NON_ENGAGING``.  Default is ``ALL``

        :param regions:  List of strings.  The regions to include IntelliSeed accounts from.
            For options, See
            `Current Regions <https://inboxtracker.readthedocs.io/en/latest/resources/regions.html#supported-regions>`_

            Default is all regions.

        :return:  A ``list`` object of ``dict`` containing details of an IntelliSeed address, including email address,
            location, and ISP.
        """

        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_last_update(self, **kwargs):
        """
        Get the time of the last update to IntelliSeed List

        :param int childAccountId:  The child account to narrow results

        :return:  A ``list`` object of 'dict' containing the account ID and last update date of the IntelliSeed list.
        """

        endpoint = "/lastUpdate"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_filter_sets(self, **kwargs):
        """
        Get the list of IntelliSeed filter sets configured for an account

        :param int childAccountId: The child account to narrow results

        :return: A ``list`` object of 'dict' containing details of a filter set, such as the name of the IntelliSeed
            list.
        """

        endpoint = "/filter_sets"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_intelliseeds_filtered(self, filterSetId, **kwargs):
        """
        Gets the latest IntelliSeed list associated with the filter set id provided

        :param int filterSetId: The id of the IntelliSeed filter set
        :param int childAccountId: The child account to narrow results

        :return: A ``list`` object of 'dict' containing details of the specified filter set, such as the name and ID of
            the IntelliSeed list.
        """

        endpoint = "/" + str(filterSetId)
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def create_intelliseed_filter(self, **kwargs):
        """
        Places a new IntelliSeed filter set under the given account

        :param str name: Name of the filter set
        :param str listType: Privacy level of list.

            Accepts: ``PUBLIC``, ``EXCLUSIVE``, ``PRIVATE``
        :param str simulatedEngagementOption: Engagement level of the IntelliSeeds to include in the list.

            Accepts: ``ALL``, ``ENGAGING``, ``NON_ENGAGING``
        :param int percentOfList: Percent of the list to include. Integer from 0-100.
        :param regions: List of strings.  The regions to include.  For options, See
            `Current Regions <https://inboxtracker.readthedocs.io/en/latest/resources/regions.html#supported-regions>`_
        :param int childAccountId: The child account to place filter

        :return: A ``dict`` object containing the details of the crated IntelliSeed list, such as the name and ID.
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

        :param int filterSetId: The id of the IntelliSeed filter set
        :param int childAccountId: The child account to narrow results

        :return: A ``dict`` object containing the details of the deleted IntelliSeed list, such as the name and ID.
        """

        endpoint = "/filter_sets/" + str(filterSetId)
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, self.param_model)
        apiResponse = self.request("DELETE", apiUrl, params=parameters)

        return apiResponse