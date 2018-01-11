# Hieratika Documentation
[Tree](./tree.html)

Caveat : this documentation is being written from the point of view of a new set of eyes on the code, so some inferences may conflict with the accurate intent of the authors.   When the documentation has settled down into a consistent state, this warning will be removed.

[Hieratika Server Reverse Engineered Commentary](./HtkSrvRE_Commentary.md)

# Getting Started

## CODAC Core System Environment

See [PSPS README.md](https://github.com/aneto0/hieratika/blob/develop-psps/demo/server/psps/README.md)

## Ubuntu 16.04 System Environment


How to run on an Ubuntu 16.04 system which does not have CCS psps installed (single user version of hieratika)

###Download hieratika
`git clone https://github.com/aneto0/hieratika.git`

###Change to the psps branch
`git hieratika`
`git checkout -b develop-psps origin/develop-psps`

###Install all the requirements
`su`
`cd server`
`pip install -r requirements.txt`
`exit`

###Start the server
`python2.7 -m hieratika.wservermain -H 0.0.0.0 -p 7000 -i ../demo/server/psps/psps.standalone.ini`
#Or (preferred)
`gunicorn --preload -k gevent -w 8 -b 0.0.0.0:7000 'hieratika.wservermain:start(config="../demo/server/psps/psps.standalone.ini")'`

###Open either chrome or opera and point at
http://127.0.0.1:7000

# Github Pages Howto

https://stackoverflow.com/questions/8446218/how-to-see-an-html-page-on-github-as-a-normal-rendered-html-page-to-see-preview

Also consider the alternative URL features, and note the suggestion to refactor this as an orphan branch, except that I need to be able to see the files that I'm documenting.



