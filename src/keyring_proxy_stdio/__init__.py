from typing import override

from jaraco.classes import properties
from keyring_proxy.backend import ProxyBackend
from keyring_proxy.stdioproxy import DEFAULT_EXE_PATH, StdioClient
from keyring_proxy.transport import TransportClient

PRIORITY = 9.9


class StdioProxyBackend(ProxyBackend):
    exe = DEFAULT_EXE_PATH

    @override
    def _get_transport(self) -> TransportClient:
        return StdioClient.from_path(self.exe)

    @properties.classproperty
    def priority(cls):
        return PRIORITY
