import responses
from inboxtracker import InboxTracker


@responses.activate
def test_get_campaigns():
    it = InboxTracker("fake-key")
    qd = "test-qd"
    endpoint = ""
    url = it.campaigns.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.campaigns.get_campaigns(qd=qd)
    assert json_output == 'yay'

@responses.activate
def test_get_campaign_by_id():
    it = InboxTracker("fake-key")
    campaignId = "test-campaign"
    embed = "test-embed"
    endpoint = "/" + str(campaignId)
    url = it.campaigns.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.campaigns.get_campaign_by_id(campaignId, embed=embed)
    assert json_output == 'yay'

@responses.activate
def test_get_ip_stats():
    it = InboxTracker("fake-key")
    qd = "test-qd"
    endpoint = "/sendingIps"
    url = it.campaigns.uri + endpoint
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    json_output = it.campaigns.get_ip_stats(qd=qd)
    assert json_output == 'yay'
