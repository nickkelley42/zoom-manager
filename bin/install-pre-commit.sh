#!/bin/bash

root="$(git rev-parse --show-toplevel)"

GITDIR="$(git rev-parse --git-dir)"
HOOKSDIR="$GITDIR/hooks"
cd "$HOOKSDIR"
if [ ! -e "pre-commit" ]; then
	ln -s "$root/bin/pre-commit"
else
	echo "Skipping linking pre-commit; pre-commit already exists"
fi
