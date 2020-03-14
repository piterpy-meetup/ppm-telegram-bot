import logging
import os
import sys

from pip._vendor.packaging.version import Version

def is_poetry_version_valid(poetry_version: str, latest_tag: str) -> bool:
    """Validate if Poetry version is greater than the latest tag."""
    return Version(poetry_version) > Version(latest_tag)


if __name__ == '__main__':
    poetry_version, latest_tag = sys.argv[1], sys.argv[2]
    if is_poetry_version_valid(poetry_version, latest_tag):
        sys.exit(0)
    logger = logging.getLogger()
    logger.error('Poetry version "%s" must be greater than the latest tag "%s"' % (poetry_version, latest_tag))
    sys.exit(1)
