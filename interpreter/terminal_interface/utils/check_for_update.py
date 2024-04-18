import pkg_resources
from packaging import version
from security import safe_requests


def check_for_update():
    # Fetch the latest version from the PyPI API
    response = safe_requests.get(f"https://pypi.org/pypi/open-interpreter/json", timeout=60)
    latest_version = response.json()["info"]["version"]

    # Get the current version using pkg_resources
    current_version = pkg_resources.get_distribution("open-interpreter").version

    return version.parse(latest_version) > version.parse(current_version)
