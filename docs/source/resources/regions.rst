Regions
=======

The IntelliSeeds list accessible in InboxTracker provide insight into the performance of campaigns globally.  The
IntelliSeeds are organized into regions, which can be used to create filters.  The regions supported by InboxTracker
can be accessed using the `InboxTracker API`_, as shown below:

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.regions.get_regions()
    print(response)

.. _InboxTracker API: http://api.edatasource.com/docs/#/inbox


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
