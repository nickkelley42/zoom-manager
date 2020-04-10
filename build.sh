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
npm install
npm run build -- --output-path="$out"

# Add server code
cd "$root/server"
cp .htaccess "$out"
cp -r api "$out"
