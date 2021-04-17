Domains
=======

InboxTracker will track the performance of mailings sent from all of the sending domains on your InboxTracker account.
The sending domains that are currently tracked in your InboxTracker account can be accessed with the
`InboxTracker API`_, as shown below:

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.domains.get_available_domains()
    print(response)

.. _InboxTracker API: http://api.edatasource.com/docs/#/inbox


List All Available Domains
--------------------------

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.domains.get_available_domains()

