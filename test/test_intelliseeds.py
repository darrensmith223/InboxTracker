import responses
from inboxtracker import InboxTracker


@responses.activate
def test_get_intelliseeds():
    it = InboxTracker("fake-key")
    endpoint = ""
    url = it.intelliseeds.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.intelliseeds.get_intelliseeds()
    assert json_output == 'yay'


@responses.activate
def test_get_last_update():
    it = InboxTracker("fake-key")
    endpoint = "/lastUpdate"
    url = it.intelliseeds.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.intelliseeds.get_last_update()
    assert json_output == 'yay'


@responses.activate
def test_get_filter_sets():
    it = InboxTracker("fake-key")
    endpoint = "/filter_sets"
    url = it.intelliseeds.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.intelliseeds.get_filter_sets()
    assert json_output == 'yay'


@responses.activate
def test_get_intelliseeds_filtered():
    it = InboxTracker("fake-key")
    filterSetId = "test-filterSetId"
    endpoint = "/" + str(filterSetId)
    url = it.intelliseeds.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.intelliseeds.get_intelliseeds_filtered(filterSetId)
    assert json_output == 'yay'


@responses.activate
def test_create_intelliseed_filter():
    it = InboxTracker("fake-key")
    endpoint = "/filter_sets"
    url = it.intelliseeds.uri + endpoint
    responses.add(
        responses.POST,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.intelliseeds.create_intelliseed_filter(
        name="name",
        listType="PUBLIC",
        simulatedEngagementOption="ALL",
        percentOfList="test-pct",
        regions=["test-region"]
    )
    assert json_output == 'yay'


@responses.activate
def test_delete_intelliseed_filter():
    it = InboxTracker("fake-key")
    filterSetId = "test-filterSetId"
    endpoint = "/filter_sets/" + str(filterSetId)
    url = it.intelliseeds.uri + endpoint
    responses.add(
        responses.DELETE,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.intelliseeds.delete_intelliseed_filter(filterSetId)
    assert json_output == 'yay'
