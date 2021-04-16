import responses
from inboxtracker import InboxTracker


@responses.activate
def test_get_available_domains():
    it = InboxTracker("fake-key")
    endpoint = "/available"
    url = it.domains.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.domains.get_available_domains()
    assert json_output == 'yay'
