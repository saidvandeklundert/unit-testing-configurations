from pydantic import BaseModel
from typing import Literal
from ipaddress import IPv4Address, IPv4Network


class NetworkData(BaseModel):
    ipv4_mgmt_network: list[IPv4Network]
    snmp_community: str


class Device(BaseModel):
    hostname: str
    vendor: Literal["cisco", "juniper"]
    router_id: IPv4Address
    network_data: NetworkData


class Devices(BaseModel):
    devices: list[Device]

    def __iter__(self):
        return iter(self.devices)
