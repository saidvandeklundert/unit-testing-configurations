from pydantic import BaseModel, validator
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

    @validator("hostname")
    def hostname_must_consist_of_four_parts(cls, hostname: str):
        """Validate the hostname"""
        parts = hostname.split("-")
        if len(parts) != 4:
            raise ValueError("hostname field must contain 4 parts")
        if not parts[-1].isdigit():
            raise ValueError("last part of the hostname must be a digit")

        return hostname


class Devices(BaseModel):
    devices: list[Device]

    def __iter__(self):
        return iter(self.devices)
