from unittest import mock
from src.generate_config import main


@mock.patch("src.generate_config.get_devices_data")
def test_main(get_devices_data_mock, devices):
    get_devices_data_mock.return_value = devices
    configurations = main()
    print(configurations)
    assert isinstance(configurations, list)
