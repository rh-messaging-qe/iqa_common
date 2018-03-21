# iQA Test suites
## Description
iQA test suite is based on py.test runner and it's designed for testing messaging services.

## Objectives
- Modular
- Scalable
- Abstract

## Included projects
 - These project will be split to separated project

### AMOM (Abstraction Messaging Of Middleware)
- Abstract classes
- Protocols
- Message
- Client (Sender, Receiver, Connector)
- Broker
- Router
- Node

### Components
- Node
- Node Execution (Ansible, Executor)
- Brokers (Artemis, QPID..)
- Router (Qpid Dispatch)
- Clients (Python proton), CLI (RHEA, Python Proton, JMS)
- IQA Instance (should be split)


## HOW TO
### Create & activate virtual environment
```
virtualenv3 venv
source venv/bin/activate
```
### Install dependencies
```
pip install -r requirements.txt
```

### Run self tests
```
./venv/bin/py.test tests-suite/selftests \
--sender native --sender nodejs --sender python \
--receiver native --receiver nodejs --receiver python \
--router dispatch --router interconnect \
--broker artemis --broker amq7  --broker amq6 \
--tls tls10 --tls tls11 --tls tls12 --tls tls13 \
--inventory /home/enkeys/ansible/hosts \
-s --verbose
```
#### Sender []
- native (core), nodejs, python 

#### Receiver []
- native (core), nodejs, python

#### Broker []
- artemis, amq7, amq6

#### TLS []
- tls10, tls11 tls12, tls13

#### Inventory 
- Path to Ansible inventory with hosts

# TODO
- inventory hosts
- topology instance
- xtlog
    - pytest way -> implement pytest-logging/pytest-logger