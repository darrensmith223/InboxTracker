Deliverability
==============

Deliverability insights enable a sender to understand and monitor how the mailings are performing after the Mailbox
Provider accepts them.  Deliverability data for a sending domain can be accessed using the `Inbox Tracker API`_, as shown
below:

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.deliverability.get_deliverability_by_domain(
        domain="example.com",
        qd="daysBack:1",
        embed="gmailCategories"
    )
    print(response)

.. _Inbox Tracker API: http://api.edatasource.com/docs/#/inbox


Get Deliverability Stats for Domain
-----------------------------------

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.deliverability.get_deliverability_by_domain(
        domain="example.com",
        qd="daysBack:1",
        embed="gmailCategories"
    )


