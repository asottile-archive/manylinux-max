from __future__ import annotations

import os
import re

PATTERN = re.compile(r'^(\d+).(\d+)$', re.ASCII)


def manylinux_compatible(major: int, minor: int, arch: str) -> bool:
    var = os.environ.get('MANYLINUX_MAX')
    if var is None:
        return True

    parsed = PATTERN.match(var)
    if parsed is None:
        raise ValueError(f'invalid MANYLINUX_MAX, expected `#.##` got `{var}`')
    return (major, minor) <= (int(parsed[1]), int(parsed[2]))
