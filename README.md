[![build status](https://github.com/asottile/manylinux-max/actions/workflows/main.yml/badge.svg)](https://github.com/asottile/manylinux-max/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/manylinux-max/main.svg)](https://results.pre-commit.ci/latest/github/asottile/manylinux-max/main)

manylinux-max
=============

dynamically cap the version of manylinux when installing from pip

## installation

```bash
pip install manylinux-max
```

## usage

install this package before trying to install other packages.

set the `MANYLINUX_MAX` environment variable to limit the candidate manylinux
versions.

this is useful (for example) when using `pip install --target` to build a zip
for aws lambda (which has an old libc version -- and likely a different libc
version than your host machine).

```bash
pip install manylinux-max
MANYLINUX_MAX=2.26 pip install --target src -r requirements.txt
```

## example error that you may encounter from aws lambda

```
ImportError: /lib64/libc.so.6: version `GLIBC_2.28' not found (required by /var/task/cryptography/hazmat/bindings/_rust.abi3.so)
```
