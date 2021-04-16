import responses
from inboxtracker import InboxTracker


@responses.activate
def test_ping_service():
    it = InboxTracker("fake-key")
    endpoint = ""
    url = it.ping.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    output = it.ping.ping_service()
    assert output == "yay"
