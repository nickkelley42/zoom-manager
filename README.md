# Zoom Manager

A webapp to let multiple users manage meetings on a single Zoom account.

Still very much in development! Features I intend to add include:
* Multi-user authentication. Provide security and user management
* View meetings schedule
* Create new meeting
* Get meeting link - open from app

## Setup

### Requirements

* Node.js/NPM - preferably using NVM to track the LTS version
* Python 3
* A web server that can handle rewrite rules and running Python as a CGI 
	script.

### Configuration

Store configuration in `config.sh` in the project root. `config.sh` 
stores access information for the Zoom API and the server on which this 
app will be hosted. An example file should look like:

```
#!/bin/bash

export ZOOMAPIKEY=keykeykey
export ZOOMAPISECRET=secret
export DEPLOYHOST=hostname
export DEPLOYPATH=path
```

## Development

The frontend is written using Ember.js. All javascript code is run 
through ESLint; run bin/install-pre-commit to run ESLint as a pre-commit 
hook.

The backend is written in Python, and sends JSON responses to the 
frontend.
