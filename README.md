# iQA Test suites
## Description
iQA test suite use messaging-abstration API for writing tests 
and messaging-components for test integration with end software.

Test suites is based on py.test tests runner but can be used any framework.

## Needed
1. Deploy the topology
2. Describe the topology in Ansible Inventory file
3. Related to test runner (Write conftest.py where is also needed describe parts from Ansible Inventory)
    - Fixture for broker, client, router
4. Write tests (with messgaging-abstraction call)

It's designed for testing messaging services.

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
- native (core)
- nodejs (cli-rhea)
- python (cli-proton-python)

#### Broker []
- Artemis (AMQ7)
- ActiveMQ AMQ6
- Qpid Broker

#### TLS []
- tls10
- tls11
- tls12
- tls13

#### Inventory 
- Path to Ansible inventory with hosts

# TODO
- inventory hosts
- topology instance
- xtlog
    - pytest way -> implement pytest-logging/pytest-logger