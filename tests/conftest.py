# pylint: disable=invalid-name
# pylint: disable=protected-access
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from copy import deepcopy

import pytest
from cucumber_tag_expressions import parse


pytest_plugins = ("pytester",)


def pytest_collection_modifyitems(config, items):
    if 'tags' in config.option:
        raw_tags = config.option.tags
        for item in items:
            item_tags = [marker.name for marker in item.own_markers]
            if not parse(raw_tags).evaluate(item_tags):
                item.add_marker(pytest.mark.not_in_scope)
