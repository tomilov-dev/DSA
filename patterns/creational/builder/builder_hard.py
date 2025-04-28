from abc import ABC
from abc import abstractmethod
from typing import Any


class ServerConfig:
    def __init__(self) -> None:
        self.server_name: str = ""
        self.ip_address: str = ""
        self.os: str = ""
        self.cpu: str = ""
        self.ram: str = ""
        self.hdd: str = ""
        self.backup: bool = False

        self.network_interfaces: list[str] = []
        self.installed_apps: list[str] = []
        self.security_settings: dict[str, Any] = {}

    def set_server_name(self, server_name: str) -> None:
        self.server_name = server_name

    def set_ip_address(self, ip_address: str) -> None:
        self.ip_address = ip_address

    def set_os(self, os: str) -> None:
        self.os = os

    def set_cpu(self, cpu: str) -> None:
        self.cpu = cpu

    def set_ram(self, ram: str) -> None:
        self.ram = ram

    def set_hdd(self, hdd: str) -> None:
        self.hdd = hdd

    def set_backup(self, backup: bool) -> None:
        self.backup = backup

    def add_network_interface(self, network_interface: str) -> None:
        self.network_interfaces.append(network_interface)

    def add_installed_app(self, installed_app: str) -> None:
        self.installed_apps.append(installed_app)

    def add_security_setting(
        self,
        security_setting_name: str,
        security_setting_value: str,
    ) -> None:
        self.security_settings[security_setting_name] = security_setting_value


class ServerConfigBuilder(ABC):
    def __init__(self) -> None:
        self._config = ServerConfig()

    @abstractmethod
    def build_server_name(self, server_name: str) -> None:
        pass

    @abstractmethod
    def build_ip_address(self, ip_address: str) -> None:
        pass

    @abstractmethod
    def build_os(self, os: str) -> None:
        pass

    @abstractmethod
    def build_cpu(self, cpu: str) -> None:
        pass

    @abstractmethod
    def build_ram(self, ram: str) -> None:
        pass

    @abstractmethod
    def build_hdd(self, hdd: str) -> None:
        pass

    @abstractmethod
    def build_backup(self, backup: bool) -> None:
        pass

    @abstractmethod
    def build_network_interface(self, network_interfaces: list[str]) -> None:
        pass

    @abstractmethod
    def build_installed_app(self, installed_apps: list[str]) -> None:
        pass

    @abstractmethod
    def build_security_setting(self, security_settings: dict[str, Any]) -> None:
        pass


class LinuxServerConfigBuilder(ServerConfigBuilder):
    def build_server_name(self, server_name: str) -> None:
        self._config.set_server_name(server_name)

    def build_ip_address(self, ip_address: str) -> None:
        self._config.set_ip_address(ip_address)

    def build_os(self, os: str) -> None:
        self._config.set_os(os)

    def build_cpu(self, cpu: str) -> None:
        self._config.set_cpu(cpu)

    def build_ram(self, ram: str) -> None:
        self._config.set_ram(ram)

    def build_hdd(self, hdd: str) -> None:
        self._config.set_hdd(hdd)

    def build_backup(self, backup: bool) -> None:
        self._config.set_backup(backup)

    def build_network_interface(self, network_interfaces: list[str]) -> None:
        for network_interface in network_interfaces:
            self._config.add_network_interface(network_interface)

    def build_installed_app(self, installed_apps: list[str]) -> None:
        for installed_app in installed_apps:
            self._config.add_installed_app(installed_app)

    def build_security_setting(self, security_settings: dict[str, Any]) -> None:
        for security_setting_name, security_setting_value in security_settings.items():
            self._config.add_security_setting(
                security_setting_name,
                security_setting_value,
            )


class ServerConfigDirector:
    def __init__(self, builder: ServerConfigBuilder) -> None:
        self._builder = builder

    def construct_server_config(self, config: dict[str, Any]) -> None:
        self._builder.build_server_name(config["server_name"])
        self._builder.build_ip_address(config["ip_address"])
        self._builder.build_os(config["os"])
        self._builder.build_cpu(config["cpu"])
        self._builder.build_ram(config["ram"])
        self._builder.build_hdd(config["hdd"])
        self._builder.build_backup(config["backup"])
        self._builder.build_network_interface(config["network_interfaces"])
        self._builder.build_installed_app(config["installed_apps"])
        self._builder.build_security_setting(config["security_settings"])
