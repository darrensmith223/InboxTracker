from .campaigns import Campaigns
from .deliverability import Deliverability
from .domains import Domains
from .intelliseeds import Intelliseeds
from .ping import Ping
from .regions import Regions
from .seeds import Seeds
from .postmaster_tools import PostmasterTools
from .spam_trap import SpamTrap


__version__ = '1.2.1'
inboxTrackerURI = "api.edatasource.com"

inbox_module = '/inbox'
spam_trap_module = '/spam-trap'
postmaster_tools_module = '/postmaster-tools'

class InboxTracker(object):

    def __init__(self, api_key, base_uri=inboxTrackerURI, version="4"):

        self.base_uri = 'http://' + base_uri + '/v' + version
        self.api_key = api_key
        self.campaigns = Campaigns(self.base_uri + inbox_module, self.api_key)
        self.deliverability = Deliverability(self.base_uri + inbox_module, self.api_key)
        self.domains = Domains(self.base_uri + inbox_module, self.api_key)
        self.intelliseeds = Intelliseeds(self.base_uri + inbox_module, self.api_key)
        self.ping = Ping(self.base_uri + inbox_module, self.api_key)
        self.regions = Regions(self.base_uri + inbox_module, self.api_key)
        self.seeds = Seeds(self.base_uri + inbox_module, self.api_key)
        self.spam_trap = SpamTrap(self.base_uri + spam_trap_module, self.api_key)
        self.postmaster_tools = PostmasterTools(self.base_uri + postmaster_tools_module, self.api_key)
