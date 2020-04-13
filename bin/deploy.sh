#!/bin/bash

set -e

root="$(git rev-parse --show-toplevel)"

"$root/bin/build.sh"

source "$root/config.sh"

echo "Deploying to $DEPLOYHOST:$DEPLOYPATH"
rsync -a "$root/public/" "$DEPLOYHOST":"$DEPLOYPATH"
echo "Done"
