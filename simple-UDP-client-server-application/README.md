# UDP Echo Client/Server Application

This repository contains a simple UDP echo client/server application implemented in Python. The client sends a message to the server, and the server echoes the message back to the client.

## Usage

### Server

To start the UDP server, run the following command in your terminal:

```bash
$ python3 echo-server.py --port=<PORT_NUMBER>
```

Replace `<PORT_NUMBER>` with the desired port number.

### Client

To run the UDP client, execute the following command:

```bash
$ python3 echo-client.py --port=<PORT_NUMBER>
```
Replace `<PORT_NUMBER>` with the same port number used to start the server.

## Example

### Starting the Server

```
$ python3 echo-server.py --port=9900
Starting up echo server on localhost port 9900
Waiting to receive message from client
```

### Running the Client

```
$ python3 echo-client.py --port=9900
Connecting to localhost port 9900
Sending Test message. This will be echoed
received Test message. This will be echoed
Closing connection to the server
```

## How it Works

The server listens for incoming messages on the specified port and echoes back any message it receives from the client. The client creates a socket, connects to the server, sends a message, and then waits for the echoed response. The interaction happens over UDP protocol, providing a lightweight and connectionless communication mechanism.
