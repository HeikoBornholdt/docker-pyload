# pyLoad Docker Image

This docker image contains latest stable pyload installed on top of ubuntu xenial.

## Setup

You have to setup pyload first:
`````
docker run -it --rm -v $PWD/pyload:/etc/pyload wainox/docker-pyload pyLoadCore --setup
`````

## Run

You can run pyload now:
`````
docker run -it --rm -p 8000:8000 -v $PWD/pyload:/etc/pyload wainox/docker-pyload pyLoadCore
`````

## Advanced

### Manage Users
You can manage users via webinterface or this command:
`````
docker run -it --rm -v $PWD/pyload:/etc/pyload wainox/docker-pyload pyLoadCore --user
`````

### Secure Webinterface

You have to generate a ssl key & certificate:
`````
docker run -it --rm -v $PWD/pyload:/etc/pyload wainox/docker-pyload openssl genrsa -out /etc/pyload/ssl.key 2048
docker run -it --rm -v $PWD/pyload:/etc/pyload wainox/docker-pyload openssl req -new -x509 -key /etc/pyload/ssl.key -days 3650 -sha256 -out /etc/pyload/ssl.crt
`````

Now you can enable ssl/https in pyload config and restart the docker container.
