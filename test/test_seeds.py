import responses
from inboxtracker import InboxTracker


@responses.activate
def test_get_last_update():
    it = InboxTracker("fake-key")
    endpoint = "/lastUpdate"
    url = it.seeds.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.seeds.get_last_update()
    assert json_output == 'yay'


@responses.activate
def test_get_usage():
    it = InboxTracker("fake-key")
    endpoint = "/usage"
    url = it.seeds.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.seeds.get_usage()
    assert json_output == 'yay'


@responses.activate
def test_get_seeds():
    it = InboxTracker("fake-key")
    endpoint = ""
    url = it.seeds.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.seeds.get_seeds()
    assert json_output == 'yay'
