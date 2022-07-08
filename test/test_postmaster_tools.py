import responses
from inboxtracker import InboxTracker


@responses.activate
def test_get_domain_perf():
    it = InboxTracker("fake-key")
    endpoint = "/domain"
    url = it.postmaster_tools.yahoo.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.postmaster_tools.yahoo.get_domain_perf()
    assert json_output == 'yay'

@responses.activate
def test_get_ip_perf():
    it = InboxTracker("fake-key")
    endpoint = "/ip"
    url = it.postmaster_tools.yahoo.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.postmaster_tools.yahoo.get_ip_perf()
    assert json_output == 'yay'

@responses.activate
def test_get_volume_over_time():
    it = InboxTracker("fake-key")
    endpoint = "/volume/over-time"
    url = it.postmaster_tools.yahoo.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.postmaster_tools.yahoo.get_volume_over_time()
    assert json_output == 'yay'
