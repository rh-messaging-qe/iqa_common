# Abstraction Messaging of Middleware [AMOM_API] (messaging_abstraction)
## Description
Abstract classes for messaging components like broker, clients, messages, queue, topics, routes.

## Abstracts API for:
- Protocol
- Message
- Broker
- Router
- Client 
  - Sender
  - Receiver
  - Connector

## Another abstract implementation
- Queue
- Addresses
- Routing logic
  - Anycast
  - Multicast
  - Mixed (multicast + anycast) 