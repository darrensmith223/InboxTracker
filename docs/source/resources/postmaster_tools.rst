Postmaster Tools
================

The Postmaster Tools module contains several classes which can be used to access reputation data provided from Mailbox
Provider Postmaster Tools platforms.  The Postmaster Tools module includes the following classes:

* `inboxtracker.postmaster_tools.yahoo`
* `inboxtracker.postmaster_tools.ping`

.. _different types: https://support.emailanalyst.com/en/articles/4476832-spam-trap-types-and-sources

Yahoo
-----

Reputation and deliverability performance data provided directly from Yahoo is available within your Inbox Tracker
account.  The Yahoo performance data can be accessed at the domain level using the `Inbox Tracker API`_, as shown below:

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.postmaster_tools.yahoo.get_domain_perf(
        domain=["example.com"],
        qd="daysBack:1"
    )
    print(response)

.. _Inbox Tracker API: http://api.edatasource.com/docs/#/postmaster-tools

Group Yahoo Performance Data by Domain
**************************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.postmaster_tools.yahoo.get_domain_perf(
        domain=["example.com"],
        qd="daysBack:1"
    )

Group Yahoo Performance Data by IP
**********************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.postmaster_tools.yahoo.get_ip_perf(
        domain=["example.com"],
        qd="daysBack:1"
    )

Get Yahoo Volume Data Over Time
*******************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.postmaster_tools.yahoo.get_volume_over_time(
        domain=["example.com"],
        qd="daysBack:1"
    )

Ping
----

The `ping` class enables a user to verify that the Postmaster Tools module is accessible.  The Postmaster Tools ping is
separate from the Inbox Tracker ping because the Postmaster Tools module interfaces with a different underlying service
than the primary Inbox Tracker service.

Ping the Postmaster Tools Service
*********************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.postmaster_tools.ping.ping_service()

