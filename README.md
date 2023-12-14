# What's My IP

## Overview

"What's My IP" is a simple Flask application that displays your external IP address. It's designed to be run in a Docker container, making it easy to deploy and access your IP address from anywhere.
after setting it up feel free to point a subdomain to your container and to check your IP address whenever your ISP changes your IP address.

## Prerequisites

Before running the application, ensure you have the following:

- [Docker](https://docs.docker.com/get-docker/) installed on your server or machine.

## How to Use

1. **Clone the repository:**

    ```bash
    git clone https://github.com/BikeyBoi/whatsmyip.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd whatsmyip
    ```

3. **Build the Docker image:**

    ```bash
    docker build -t whatsmyip:latest .
    ```

4. **Run the Docker container:**

    ```bash
    docker run -p 5000:5000 --restart unless-stopped whatsmyip:latest
    ```

5. **Open your browser and go to [http://localhost:5000](http://localhost:5000) to view your IP address.**

## Customization

### Basic Authentication

The application uses basic authentication to restrict access. You can set the username and password by providing environment variables:

```bash
docker run -p 5000:5000 -e BASIC_AUTH_USERNAME=your_username -e BASIC_AUTH_PASSWORD=your_password --restart unless-stopped whatsmyip:latest
