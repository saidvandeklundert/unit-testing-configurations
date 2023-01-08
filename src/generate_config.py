from jinja2 import Environment, FileSystemLoader
from .models import Device, Devices
import requests
from pathlib import Path

CURRENT_DIR = Path(__file__).parent.as_posix()


def get_devices_data() -> list[Device]:
    api_response_str = requests.get("https://ssot/inventory/")
    devices: Devices = Devices.construct(**api_response_str.json())
    return devices


def render(device: Device) -> str:
    file_loader = FileSystemLoader(f"{CURRENT_DIR}\\templates")
    env = Environment(loader=file_loader)
    template = env.get_template("main.j2")
    output = template.render(data=device.dict())
    output = "\n".join([line for line in output.splitlines() if line.strip()])
    return output


def main() -> list[str]:
    configurations: list[str] = []
    devices = get_devices_data()

    for device in devices:
        configuration = render(device=device)
        configurations.append(configuration)

    return configurations


if __name__ == "__main__":
    main()
