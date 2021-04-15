import responses
import inboxtracker


@responses.activate
def test_GetCampaignById():
    campaignId = "test-campaign"
    apiUrl = "http://api.edatasource.com/v4/inbox/campaigns/test-campaign?Authorization=fake-key"
    responses.add(
        responses.POST,
        apiUrl,
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    apiKey = "fake-key"
    response = inboxtracker.GetCampaignById(apiKey, campaignId)
