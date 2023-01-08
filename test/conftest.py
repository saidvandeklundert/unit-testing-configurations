import pytest
from src.models import Device, NetworkData, Devices


@pytest.fixture(scope="session")
def devices():
    network_data = NetworkData(
        **{
            "ipv4_mgmt_network": ["10.0.0.0/14", "10.200.0.0/14"],
            "snmp_community": "yolo_colo",
        }
    )
    device_1 = Device(
        **{
            "hostname": "par-cbs-a-r1",
            "vendor": "cisco",
            "router_id": "192.168.1.1",
            "network_data": network_data,
        }
    )
    device_2 = Device(
        **{
            "hostname": "tok-dar-c-r2",
            "vendor": "juniper",
            "router_id": "192.168.1.2",
            "network_data": network_data,
        }
    )
    devices: Devices = Devices(devices=[device_1, device_2])
    return devices
