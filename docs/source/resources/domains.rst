Domains
=======

Inbox Tracker will track the performance of mailings sent from all of the sending domains on your Inbox Tracker account.
The sending domains that are currently tracked in your Inbox Tracker account can be retrieved with the
`Inbox Tracker API`_, as shown below:

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.domains.get_available_domains()
    print(response)

.. _Inbox Tracker API: http://api.edatasource.com/docs/#/inbox


List All Available Domains
--------------------------

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.domains.get_available_domains()

