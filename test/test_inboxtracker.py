import responses
import inboxtracker


@responses.activate
def test_GetCampaignById():
    responses.add(
        responses.GET,
        "http://api.edatasource.com/v4/inbox/campaigns/test-campaign",
        status=200,
        content_type='application/json',
        body='{"results": "yay"}'
    )
    apiKey = "fake-key"
    campaignId = "test-campaign"
    response = inboxtracker.GetCampaignById(apiKey, campaignId)
    assert response == "yay"
