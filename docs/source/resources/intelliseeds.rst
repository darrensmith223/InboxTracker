Intelliseeds
============

IntelliSeeds are virtual users who interact with email in their inbox to provide realistic modeling, based on
engagement profiles from the InboxTracker consumer panel.  Learn more about `IntelliSeeds here`_.  IntelliSeeds are
organized into a list that can be retrieved and included as recipients in campaigns to provide deliverability
performance insight, such as inbox and spam folder placement.  The list of IntelliSeeds can be accessed using the
`InboxTracker API`_, as shown below:


.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.intelliseeds.get_intelliseeds()
    print(response)

.. _InboxTracker API: http://api.edatasource.com/docs/#/inbox
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

Text about Filter Sets.  What they are.  How to use them.  Why you should care.

Filter Sets are stored IntelliSeed lists that have customized with filters.  Filter Sets allow you to create multiple
IntelliSeed lists with different characteristics, and store them for reuse.  For example, you may wish to have a
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


Retrieve Intelliseeds From a Filter Set
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


