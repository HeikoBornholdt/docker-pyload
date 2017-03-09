#!/bin/sh
set -e

envsubst < /default.conf > /usr/share/pyload/module/config/default.conf

exec "$@"
