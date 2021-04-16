import responses
from inboxtracker import InboxTracker


@responses.activate
def test_get_deliverability_by_domain():
    it = InboxTracker("fake-key")
    domain = "test-domain"
    qd = "test-qd"
    endpoint = "/" + str(domain)
    url = it.deliverability.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.deliverability.get_deliverability_by_domain(domain, qd=qd)
    assert json_output == 'yay'
