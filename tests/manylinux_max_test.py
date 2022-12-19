from __future__ import annotations

import os
from unittest import mock

import pytest

from _manylinux import manylinux_compatible


def test_default_is_allow_all():
    assert manylinux_compatible(2, 28, 'x86_64') is True


def test_incompatible_based_on_environment_variable():
    with mock.patch.dict(os.environ, {'MANYLINUX_MAX': '2.26'}):
        assert manylinux_compatible(2, 28, 'x86_64') is False
        assert manylinux_compatible(2, 26, 'x86_64') is True


def test_environment_variable_is_garbage():
    with mock.patch.dict(os.environ, {'MANYLINUX_MAX': 'garbage'}):
        with pytest.raises(ValueError) as excinfo:
            manylinux_compatible(2, 28, 'x86_64')

    msg, = excinfo.value.args
    assert msg == 'invalid MANYLINUX_MAX, expected `#.##` got `garbage`'
