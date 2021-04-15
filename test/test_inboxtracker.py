import responses
import inboxtracker


@responses.activate
def test_GetCampaignById():
    campaignId = "test-campaign"
    responses.add(
        responses.GET,
        "http://api.edatasource.com/v4/inbox/campaigns/test-campaign?Authorization=fake-key",
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    apiKey = "fake-key"
    response = inboxtracker.GetCampaignById(apiKey, campaignId)
