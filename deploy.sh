#!/bin/bash

root="$(git rev-parse --show-toplevel)"
cd "$root"

./build.sh

source config.sh

rsync -a public/ "$DEPLOYHOST":"$DEPLOYPATH"
