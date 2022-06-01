import pytest

from nesteddict import merge_nested, is_included


@pytest.fixture
def dic1():
    return {
        "A": {
            "AA": 1,
            "AB": 1,
        },
        "B": {
            "BA": 1,
        }
    }


@pytest.fixture
def dic2():
    return {
        "A": {
            "AA": 2,
            "AB": 2,
        },
        "B": {
            "BB": 2,
        }
    }


@pytest.fixture
def dic3():
    return {
        "A": {
            "AA": 2,
        },
        "B": {
            "BB": 2,
        }
    }


def test_merge_nested(dic1, dic2):
    assert merge_nested(dic1, dic2) == {
            "A": {
                "AA": 2,
                "AB": 2,
            },
            "B": {
                "BA": 1,
                "BB": 2,
            }
        }


def test_is_included(dic2, dic3):
    assert is_included(dic3, dic2)
