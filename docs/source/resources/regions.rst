Regions
=======

The IntelliSeeds list accessible within Inbox Tracker provides insight into the performance of campaigns at Mailbox
Providers across the globe.  The IntelliSeeds are organized by region, which can be used to create filters.  The
regions supported by Inbox Tracker can be accessed using the `Inbox Tracker API`_, as shown below:

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.regions.get_regions()
    print(response)

.. _Inbox Tracker API: http://api.edatasource.com/docs/#/inbox


Get Regions
-----------

List All Supported Regions
**************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.regions.get_regions()


Supported Regions
*****************

* ``Asia Pacific``
* ``B2B``
* ``Europe - France``
* ``Europe - Germany``
* ``Europe - Italy``
* ``Europe - Other``
* ``Europe - UK``
* ``N/A``
* ``North America - Canada``
* ``North America - US``
* ``Primary Webmail``
* ``South America``
* ``Web Appliance``
