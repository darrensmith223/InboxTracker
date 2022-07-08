import responses
from inboxtracker import InboxTracker


@responses.activate
def test_get_available_domains():
    it = InboxTracker("fake-key")
    endpoint = ""
    url = it.spam_trap.available_domains.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.spam_trap.available_domains.get_available_domains()
    assert json_output == 'yay'

@responses.activate
def test_get_traps_by_domain():
    it = InboxTracker("fake-key")
    endpoint = ""
    url = it.spam_trap.domain.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.spam_trap.domain.get_traps_by_domain()
    assert json_output == 'yay'

@responses.activate
def test_get_domain_rollup():
    it = InboxTracker("fake-key")
    endpoint = "/rollup"
    url = it.spam_trap.domain.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.spam_trap.domain.get_domain_rollup()
    assert json_output == 'yay'

@responses.activate
def test_get_domain_rollup_details():
    it = InboxTracker("fake-key")
    endpoint = "/rollup/details"
    url = it.spam_trap.domain.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.spam_trap.domain.get_domain_rollup_details()
    assert json_output == 'yay'

@responses.activate
def test_get_traps_by_ip():
    it = InboxTracker("fake-key")
    endpoint = ""
    url = it.spam_trap.ip.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.spam_trap.ip.get_traps_by_ip()
    assert json_output == 'yay'

@responses.activate
def test_get_ip_rollup():
    it = InboxTracker("fake-key")
    endpoint = "/rollup"
    url = it.spam_trap.ip.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.spam_trap.ip.get_ip_rollup()
    assert json_output == 'yay'

@responses.activate
def test_get_ip_rollup_details():
    it = InboxTracker("fake-key")
    endpoint = "/rollup/details"
    url = it.spam_trap.ip.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.spam_trap.ip.get_ip_rollup_details()
    assert json_output == 'yay'
