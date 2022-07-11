Spam Trap
=========

Spam traps are email addresses that are not supposed to receive email.  There are `different types`_, which can impact
your sending reputation to varying degrees.  Spam trap data are collected and reported by Inbox Tracker.

The Spam Trap module contains several classes which can be used to get spam trap data available within your Inbox
Tracker account.  The Spam Trap module includes the following classes:

* `inboxtracker.spam_trap.available_domains`
* `inboxtracker.spam_trap.domain`
* `inboxtracker.spam_trap.ip`
* `inboxtracker.spam_trap.ping`

.. _different types: https://support.emailanalyst.com/en/articles/4476832-spam-trap-types-and-sources

Available Domains
-----------------

The `available_domains` class enables a user to retrieve the domains available for spam trap reporting on the Inbox
Tracker account.  The available domains can be accessed using the `Inbox Tracker API`_, as shown below:

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.spam_trap.available_domains.get_available_domains()
    print(response)

.. _Inbox Tracker API: http://api.edatasource.com/docs/#/spam-trap

Get Available Domains
*********************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.spam_trap.available_domains.get_available_domains()

Domain
------

The `domain` class enables a user to retrieve details about spam trap hits at the domain level.  Spam trap data for a
sending domain can be accessed using the `Inbox Tracker API`_, as shown below:

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.spam_trap.domain.get_traps_by_domain(
        domain=["example.com"],
        qd="daysBack:1",
        trapSource=["ABUSIX", "CLOUDMARK", "SNDS", "GTN_PASSIVE", "GTN_ACTIVE"],
        trapType=["PRISTINE", "MIXED", "RECYCLED", "PARKED", "TYPO"]
    )
    print(response)


Group Spam Trap Data by Domain
******************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.spam_trap.domain.get_traps_by_domain(
        domain=["example.com"],
        qd="daysBack:1",
        trapSource=["ABUSIX", "CLOUDMARK", "SNDS", "GTN_PASSIVE", "GTN_ACTIVE"],
        trapType=["PRISTINE", "MIXED", "RECYCLED", "PARKED", "TYPO"]
    )


Get Spam Trap Data by Domain with Campaign Details
**************************************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.spam_trap.domain.get_domain_rollup(
        domain=["example.com"],
        qd="daysBack:1",
        trapSource=["ABUSIX", "CLOUDMARK", "SNDS", "GTN_PASSIVE", "GTN_ACTIVE"],
        trapType=["PRISTINE", "MIXED", "RECYCLED", "PARKED", "TYPO"]
    )

Get Spam Trap Data with Detailed Information
********************************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.spam_trap.domain.get_domain_rollup_details(
        domain=["example.com"],
        qd="daysBack:1",
        trapSource=["ABUSIX", "CLOUDMARK", "SNDS", "GTN_PASSIVE", "GTN_ACTIVE"],
        trapType=["PRISTINE", "MIXED", "RECYCLED", "PARKED", "TYPO"]
    )

IP
--

The `ip` class enables a user to retrieve spam trap data at the IP address level.  Spam trap data grouped by IP address
can be accessed using the `Inbox Tracker API`_, as shown below:

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.spam_trap.ip.get_traps_by_ip(
        domain=["example.com"],
        qd="daysBack:1",
        trapSource=["ABUSIX", "CLOUDMARK", "SNDS", "GTN_PASSIVE", "GTN_ACTIVE"],
        trapType=["PRISTINE", "MIXED", "RECYCLED", "PARKED", "TYPO"]
    )
    print(response)


Group Trap Hits by IP
*********************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.spam_trap.ip.get_traps_by_ip(
        domain=["example.com"],
        qd="daysBack:1",
        trapSource=["ABUSIX", "CLOUDMARK", "SNDS", "GTN_PASSIVE", "GTN_ACTIVE"],
        trapType=["PRISTINE", "MIXED", "RECYCLED", "PARKED", "TYPO"]
    )

Group Spam Trap Data by IP with Campaign Details
************************************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.spam_trap.ip.get_ip_rollup(
        domain=["example.com"],
        qd="daysBack:1",
        trapSource=["ABUSIX", "CLOUDMARK", "SNDS", "GTN_PASSIVE", "GTN_ACTIVE"],
        trapType=["PRISTINE", "MIXED", "RECYCLED", "PARKED", "TYPO"]
    )

Group Trap Hits by IP
*********************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.spam_trap.ip.get_ip_rollup_details(
        domain=["example.com"],
        qd="daysBack:1",
        trapSource=["ABUSIX", "CLOUDMARK", "SNDS", "GTN_PASSIVE", "GTN_ACTIVE"],
        trapType=["PRISTINE", "MIXED", "RECYCLED", "PARKED", "TYPO"]
    )


Ping
----

The `ping` class enables a user to verify that the Spam Trap module is accessible.  The Spam Trap ping is separate from
the Inbox Tracker ping because the Spam Trap module interfaces with a different underlying service than the primary
Inbox Tracker service.

Ping the Spam Trap Service
**************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.spam_trap.ping.ping_service()


