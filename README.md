# Zoom Manager

A webapp to let multiple users manage meetings on a single Zoom account.

## Setup

You will need a build environment and a server. The build environment 
takes the codebase and your configuration and creates the files that you 
deploy to your production environment on the server.

Build environment requirements:
* Node.js/NPM - use NVM to ensure you're on the correct versions for 
	this project.
* Bash - should be available on any modern machine

Server requirements:
* Python 3 - must be able to run as a CGI script
* .htaccess files enabled - uses rewrite rules for both the frontend and 
	backend.
* Ability to install pip3 packages

### Configuration

Configuration is stored in a file named `config.sh` in the project root 
directory; you will have to create this yourself. Each config variable 
should be exported like this:

```
#!/bin/bash

export ZOOMAPIKEY=keykeykey
export ZOOMAPISECRET=secret
export DEPLOYHOST=hostname
export DEPLOYPATH=path
```

Required configuration fields (case-sensitive):
* `DEPLOYHOST` - The hostname of your server
* `DEPLOYPATH` - The pathname on the server to which the build should be 
	copied
* `ZOOMAPIKEY` - your Zoom app API key
* `ZOOMAPISECRET` - your Zoom app API secret
* `DBHOST` - The hostname of your database; if your database is on the 
	same server as your web host, use `localhost`
* `DBNAME` - The database name
* `DBUSER` - The database username
* `DBPASS` - The database password

### Deployment

Once your files are in place:

1. Deploy by running the `bin/deploy.sh` script.
2. Log in to your server; in the web directory, under api/, run 
	 `setup_db.py` to set up your server, and then `create_user.py` to 
	 create a user.

## Development

The frontend is written using Ember.js. All javascript code is run 
through ESLint; run bin/install-pre-commit to run ESLint as a pre-commit 
hook.

The backend is written in Python, and sends JSON responses to the 
frontend.

