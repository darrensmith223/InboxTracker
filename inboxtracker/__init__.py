from .campaigns import Campaigns
from .deliverability import Deliverability
from .domains import Domains
from .intelliseeds import Intelliseeds
from .ping import Ping
from .regions import Regions
from .seeds import Seeds
from .postmaster_tools import PostmasterTools
from .spam_trap import SpamTrap


__version__ = '1.2.0'
inboxTrackerURI = "api.edatasource.com"


class InboxTracker(object):

    def __init__(self, api_key, base_uri=inboxTrackerURI, version="4"):

        self.base_uri = 'http://' + base_uri + '/v' + version + '/inbox'
        self.api_key = api_key
        self.campaigns = Campaigns(self.base_uri, self.api_key)
        self.deliverability = Deliverability(self.base_uri, self.api_key)
        self.domains = Domains(self.base_uri, self.api_key)
        self.intelliseeds = Intelliseeds(self.base_uri, self.api_key)
        self.ping = Ping(self.base_uri, self.api_key)
        self.regions = Regions(self.base_uri, self.api_key)
        self.seeds = Seeds(self.base_uri, self.api_key)
        self.spam_trap = SpamTrap(self.base_uri, self.api_key)
        self.postmaster_tools = PostmasterTools(self.base_uri, self.api_key)
