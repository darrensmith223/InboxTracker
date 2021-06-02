Ping
====

Pinging the Inbox Tracker service enables you to verify that the service is available, which can be useful when
troubleshooting, as shown below:

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.ping.ping_service()
    print(response)


If the service is available, `ping_service()` will return the string `pong`.


Ping the Inbox Tracker Service
------------------------------

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.ping.ping_service()

