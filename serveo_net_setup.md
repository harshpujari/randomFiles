# Serveo.net Port Forwarding Setup Guide

This guide provides detailed instructions on how to set up port forwarding using `serveo.net`.

## Prerequisites

1. Ensure you have `ssh` installed on your machine.
2. A service running locally that you want to expose (e.g., a web server on port 8000).

## Steps

### 1. Verify SSH Installation

First, make sure SSH is installed on your system. Open a terminal and run:

```sh ssh -V```

This should return the version of SSH installed. If SSH is not installed, you will need to install it. On macOS, SSH is usually pre-installed.

### 2. Start Your Local Service
Ensure your local service is running. For example, if you have a web server running on port 8000, start it as you normally would.

### 3. Set Up Port Forwarding with Serveo.net
Use the ssh command to create a tunnel from a remote port on Serveo.net to your local service.  
```ssh -R 80:localhost:8000 serveo.net```   
This command will forward all traffic on port 80 of serveo.net to port 8000 on your local machine. When the command is executed, you should see output similar to: