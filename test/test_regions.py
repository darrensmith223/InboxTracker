import responses
from inboxtracker import InboxTracker


@responses.activate
def test_get_regions():
    it = InboxTracker("fake-key")
    endpoint = ""
    url = it.regions.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.regions.get_regions()
    assert json_output == 'yay'
