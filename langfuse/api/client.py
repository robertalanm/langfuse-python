# This file was auto-generated by Fern from our API Definition.

from .resources.coldkeys.client import AsyncColdkeysClient, ColdkeysClient
from .resources.event.client import AsyncEventClient, EventClient
from .resources.generations.client import AsyncGenerationsClient, GenerationsClient
from .resources.hotkeys.client import AsyncHotkeysClient, HotkeysClient
from .resources.neurons.client import AsyncNeuronsClient, NeuronsClient
from .resources.score.client import AsyncScoreClient, ScoreClient
from .resources.span.client import AsyncSpanClient, SpanClient
from .resources.trace.client import AsyncTraceClient, TraceClient
from .resources.wallets.client import AsyncWalletsClient, WalletsClient


class FintoLangfuse:
    def __init__(self, *, environment: str, username: str, password: str):
        self._environment = environment
        self._username = username
        self._password = password
        self.coldkeys = ColdkeysClient(environment=self._environment, username=self._username, password=self._password)
        self.event = EventClient(environment=self._environment, username=self._username, password=self._password)
        self.generations = GenerationsClient(
            environment=self._environment, username=self._username, password=self._password
        )
        self.hotkeys = HotkeysClient(environment=self._environment, username=self._username, password=self._password)
        self.neurons = NeuronsClient(environment=self._environment, username=self._username, password=self._password)
        self.score = ScoreClient(environment=self._environment, username=self._username, password=self._password)
        self.span = SpanClient(environment=self._environment, username=self._username, password=self._password)
        self.trace = TraceClient(environment=self._environment, username=self._username, password=self._password)
        self.wallets = WalletsClient(environment=self._environment, username=self._username, password=self._password)


class AsyncFintoLangfuse:
    def __init__(self, *, environment: str, username: str, password: str):
        self._environment = environment
        self._username = username
        self._password = password
        self.coldkeys = AsyncColdkeysClient(
            environment=self._environment, username=self._username, password=self._password
        )
        self.event = AsyncEventClient(environment=self._environment, username=self._username, password=self._password)
        self.generations = AsyncGenerationsClient(
            environment=self._environment, username=self._username, password=self._password
        )
        self.hotkeys = AsyncHotkeysClient(
            environment=self._environment, username=self._username, password=self._password
        )
        self.neurons = AsyncNeuronsClient(
            environment=self._environment, username=self._username, password=self._password
        )
        self.score = AsyncScoreClient(environment=self._environment, username=self._username, password=self._password)
        self.span = AsyncSpanClient(environment=self._environment, username=self._username, password=self._password)
        self.trace = AsyncTraceClient(environment=self._environment, username=self._username, password=self._password)
        self.wallets = AsyncWalletsClient(
            environment=self._environment, username=self._username, password=self._password
        )
