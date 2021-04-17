Campaigns
==========

InboxTracker will track the campaigns sent from a domain and provide insights into how the campaigns are performing.
Campaign performance data within InboxTracker can be accessed using the `InboxTracker API`_, as shown below:

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.campaigns.get_campaigns(qd="daysBack:1")
    print(response)

.. _InboxTracker API: http://api.edatasource.com/docs/#/inbox


List All Campaigns
------------------

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.campaigns.get_campaigns(qd="daysBack:1")


Filter on Custom Header
***********************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.campaigns.get_campaigns(
        qd="daysBack:1",
        headerKey="x-campaign",
        headerValue="welcome",
        per_page=20
    )


Use Pagination
**************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.campaigns.get_campaigns(
        qd="daysBack:1",
        page=1,
        per_page=20
    )


Sort Results
************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.campaigns.get_campaigns(
        qd="daysBack:1",
        order="inbox"
    )


Retrieve a Campaign
-------------------

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.campaigns.get_campaign_by_id(
        campaignId=0,
        embed="gmailCategories"
    )


List IP Address Stats for Campaigns
-----------------------------------

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.campaigns.get_ip_stats(qd="daysBack:1")

