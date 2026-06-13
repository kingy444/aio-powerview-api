"""Constant values shared between tests."""

import pytest

import json
from pathlib import Path

FAKE_BASE_URL = "powerview.hub.test"

SCENE_RAW_DATA_V1_V2 = {
    "roomId": 26756,
    "name": "RGluaW5nIFZhbmVzIE9wZW4=",  # "Dining Vanes Open"
    "colorId": 0,
    "iconId": 0,
    "id": 37217,
    "order": 1,
}

SCENE_RAW_DATA_V3 = {
    "id": 37217,
    "name": "RGluaW5nIFZhbmVzIE9wZW4=",  # "Dining Vanes Open"
    "ptName": "Dining Vanes Open",
    "networkNumber": 45057,
    "color": "0",
    "icon": "0",
    "roomIds": [26756],
    "shadeIds": [],  # mocked later in test to validate v3 behavior
}


@pytest.fixture
def device_json(api_version: int) -> str:
    """Return the request_raw_data fixture for a specific device."""
    if api_version == 1:
        return "gen1/userdata.json"
    if api_version == 2:
        return "gen2/userdata.json"
    if api_version == 3:
        return "gen3/gateway/primary.json"
    # Add more conditions for different api_versions if needed
    raise ValueError(f"Unsupported api_version: {api_version}")


@pytest.fixture
def home_json(api_version: int) -> str:
    """Return the request_home_data fixture for a specific device."""
    if api_version == 1:
        return "gen1/userdata.json"
    if api_version == 2:
        return "gen2/userdata.json"
    if api_version == 3:
        return "gen3/home/home.json"
    # Add more conditions for different api_versions if needed
    raise ValueError(f"Unsupported api_version: {api_version}")


@pytest.fixture
def firmware_json(api_version: int) -> str:
    """Return the request_raw_firmware fixture for a specific device."""
    if api_version == 1:
        return "gen1/fwversion.json"
    if api_version == 2:
        return "gen2/fwversion.json"
    if api_version == 3:
        return "gen3/gateway/info.json"
    # Add more conditions for different api_versions if needed
    raise ValueError(f"Unsupported api_version: {api_version}")


@pytest.fixture
def rooms_json(api_version: int) -> str:
    """Return the get_resources fixture for a specific device."""
    if api_version == 1:
        return "gen1/rooms.json"
    if api_version == 2:
        return "gen2/rooms.json"
    if api_version == 3:
        return "gen3/home/rooms.json"
    # Add more conditions for different api_versions if needed
    raise ValueError(f"Unsupported api_version: {api_version}")


# @pytest.fixture
def scenes_json_old(api_version: int) -> str:
    """Return the get_resources fixture for a specific device."""
    if api_version == 1:
        return "gen1/scenes.json"
    if api_version == 2:
        return "gen2/scenes.json"
    if api_version == 3:
        return "gen3/home/scenes.json"
    # Add more conditions for different api_versions if needed
    raise ValueError(f"Unsupported api_version: {api_version}")


def scenes_json(api_version: int) -> dict:
    """Return parsed scenes JSON for a specific API version."""

    fixture_path = Path(__file__).parent / "fixtures"

    if api_version == 1:
        file_path = fixture_path / "gen1" / "scenes.json"
    elif api_version == 2:
        file_path = fixture_path / "gen2" / "scenes.json"
    elif api_version == 3:
        file_path = fixture_path / "gen3" / "home" / "scenes.json"
    else:
        raise ValueError(f"Unsupported api_version: {api_version}")

    with file_path.open(encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def shades_json(api_version: int) -> str:
    """Return the get_resources fixture for a specific device."""
    if api_version == 1:
        return "gen1/shades.json"
    if api_version == 2:
        return "gen2/shades.json"
    if api_version == 3:
        return "gen3/home/shades.json"
    # Add more conditions for different api_versions if needed
    raise ValueError(f"Unsupported api_version: {api_version}")
