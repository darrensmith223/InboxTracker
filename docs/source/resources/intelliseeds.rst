IntelliSeeds
============

IntelliSeeds are virtual users who interact with email in their inbox to provide realistic modeling, based on
engagement profiles from the Inbox Tracker consumer panel.  Learn more about `IntelliSeeds here`_.  IntelliSeeds are
organized into a list that can be retrieved and included as recipients in your campaigns to provide deliverability
performance insight, such as inbox and spam folder placement.  The most current list of IntelliSeeds can be retrieved
using the `Inbox Tracker API`_, as shown below:


.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.intelliseeds.get_intelliseeds()
    print(response)

.. _Inbox Tracker API: http://api.edatasource.com/docs/#/inbox
.. _IntelliSeeds here: https://support.emailanalyst.com/en/articles/4495508-inside-intelliseeds-tools-and-techniques


Get IntelliSeeds
----------------

Retrieve All IntelliSeeds
*************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.intelliseeds.get_intelliseeds()


Filter IntelliSeed List
***********************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.intelliseeds.get_intelliseeds(
        type="PRIVATE",
        percentOfList=25,
        simulatedEngagementOption="ALL",
        regions=["B2B"]
    )


Using Filter Sets
-----------------

Filter Sets are stored IntelliSeed lists that have customized with filters.  Filter Sets allow you to create multiple
IntelliSeed lists with different attributes, and store them for reuse.  For example, you may wish to have a
separate list of IntelliSeeds for domestic and international mailings.


List All Filter Sets
********************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.intelliseeds.get_filter_sets()


Create a New Filter Set
***********************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.intelliseeds.create_intelliseed_filter(
        name="All Primary and B2B",
        listType="PRIVATE",
        simulatedEngagementOption="ALL",
        percentOfList=100,
        regions=["B2B", "Primary Webmail"]
    )


Retrieve IntelliSeeds From a Filter Set
***************************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.intelliseeds.get_intelliseeds_filtered(0)


Delete a Filter Set
*******************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.intelliseeds.delete_intelliseed_filter(0)


