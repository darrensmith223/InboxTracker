[![Build Status](https://travis-ci.com/darrensmith223/InboxTracker.svg?branch=main)](https://travis-ci.com/darrensmith223/InboxTracker)
[![Documentation Status](https://readthedocs.org/projects/inboxtracker/badge/?version=latest)](https://inboxtracker.readthedocs.io/en/latest/?badge=latest)


# InboxTracker
Python library for Inbox Tracker



# Documentation
Documentation for [InboxTracker Python Client](https://inboxtracker.readthedocs.io/en/latest/)

[Inbox Tracker API Documentation](http://api.edatasource.com/docs/#/inbox)


# Installation

Install from Pypi using pip:

```code-block:: bash
$ pip install inboxtracker
```

You may need to use `pip3` to install.


# Authentication

You will need an API key to use the Inbox Tracker API.  To get an API key, contact support through the [Inbox Tracker app](https://app.emailanalyst.com/bin/#/login). 

Once you have an API key, you can pass it to the InboxTracker class:

```python
    from inboxtracker import InboxTracker
    it = InboxTracker("API_KEY")
```

# How to Use

You can use the underlying Inbox Tracker API with the classes in the `inboxtracker` module:

* `inboxtracker.campaigns`
* `inboxtracker.deliverability`
* `inboxtracker.domains`
* `inboxtracker.intelliseeds`
* `inboxtracker.ping`
* `inboxtracker.regions`
* `inboxtracker.seeds`


For example, we can retrieve deliverability data for all of the campaigns from the previous day using the `inboxtracker.campaigns` class:

```python
    from inboxtracker import InboxTracker

    it = InboxTracker("API_KEY")

    response = it.campaigns.get_campaigns(qd="daysBack:1")
    print(response)
```

For a complete list of classes and functions, see the [Inbox Tracker Python documentation](https://inboxtracker.readthedocs.io/en/latest/api.html).


# Contribute

1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
2. Fork the [repository](https://github.com/darrensmith223/InboxTracker) on GitHub and make your changes in a branch on your fork
3. Write a test which shows that the bug was fixed or that the feature works as expected.
4. Send a pull request.