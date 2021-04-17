Seeds
=====

Traditional Seeds are a data source that InboxTracker leverages to provide insight into the performance of campaigns.
Traditional Seeds are email addresses that senders can include as recipients in their mailings and are used by
InboxTracker to provide a number of deliverability insights and metrics, such as inbox placement and email
authentication.  The current list of Traditional Seeds can be retrieved programmatically, as shown below:

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.seeds.get_seeds()
    print(response)

.. _InboxTracker API: http://api.edatasource.com/docs/#/inbox


Using Seed Lists
----------------

Retrieve Current Seed List
**************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.seeds.get_seeds()


Retrieve Last Update Time
*************************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.seeds.get_last_update()


Retrieve Seed Usage
*******************

.. code-block:: python

    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    it.seeds.get_usage()


