"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_jira.tap import TapJira

SAMPLE_CONFIG = {
    "start_date": "2023-01-01T00:00:00Z",
}

# Run standard built-in tap tests from the SDK:
TestTapJira = get_tap_test_class(
    TapJira,
    config=SAMPLE_CONFIG,
    suite_config=SuiteConfig(),
)
