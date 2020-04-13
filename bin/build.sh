#!/bin/bash

root="$(git rev-parse --show-toplevel)"
out="$root/public"

# Make sure we're using the correct node version
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
cd "$root"
nvm use

# Remove the old output
if [ -e "$out" ]; then
  rm -rf "$out"
fi

# Build the frontend
cd "$root/client"
if [[ "$EMBERENV" == "" ]]; then
	EMBERENV="production"
fi
npm run build -- --output-path="$out" --environment=$EMBERENV

# Add server code
cd "$root/server"
cp .htaccess "$out"
cp -r api "$out"

# Put together api config file
cd "$out/api"
source "$root/config.sh"
echo "#!/usr/bin/env python3" > config.py
echo "zoom_api_key = '$ZOOMAPIKEY'" >> config.py
echo "zoom_api_secret = '$ZOOMAPISECRET'" >> config.py
echo "db_host = '$DBHOST'" >> config.py
echo "db_name = '$DBNAME'" >> config.py
echo "db_user = '$DBUSER'" >> config.py
echo "db_pass = '$DBPASS'" >> config.py
echo "db_salt = '$DBSALT'" >> config.py

# add favicon files if they're not there already
touch "$out/favicon.ico"
