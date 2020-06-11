"""Exceptions"""


class TestRailError(Exception):
    """Base Exception"""


class TestRailConfigurationError(TestRailError):
    """Configuration Exception"""


class TestRailAPIError(TestRailError):
    """Base API Exception"""


class StatusCodeError(TestRailAPIError):
    """Status code Exception"""
