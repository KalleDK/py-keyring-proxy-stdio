from typing import override

from jaraco.classes import properties
from keyring_proxy.stdioproxy import DEFAULT_EXE_PATH, RuntimeTransport
from keyring_proxy.transport import ProxyBackend, TransportClient

PRIORITY = 9.9


class StdioProxyBackend(ProxyBackend):

    exe = DEFAULT_EXE_PATH

    @override
    def _get_transport(self) -> TransportClient:
        return RuntimeTransport.from_path(self.exe)

    @properties.classproperty
    def priority(cls):
        return PRIORITY
