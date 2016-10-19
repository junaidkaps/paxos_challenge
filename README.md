#Paxos Code Challenge for Junaid 
This repository is a submission for the Paxos Code Challenge. Instructions and answers to the code challenge questions can be found below. 

##Pull image from Dockerhub and Run:
1. ```docker pull junaidkaps/paxos_challenge:latest```
2. ```docker run -d -p 443:443 --name=paxosApp --restart=always --log-opt max-file=2 --log-opt max-size=1k junaidkaps/paxos_challenge:latest```

## Available Application Commands: 
 
1. /POST a message to the application and obtain 256SHA: 
```
curl -i -X POST -H "Content-Type: application/json" -d '{"message":"foo"}' https://localhost/messages -k
```
2. /GET the original message (string specified in #1) using the 256SHA obtained in #1: 
```
curl -i https://localhost/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae -k
```
3. Return a 404 if an non-existent 256SHA is used in #2: 
```
curl -i https://localhost/messages/iWillReturn404 -k
```

This application was created using the Flask framework and is run using the stand-alone Tornado WSGI container. 

##Notes on Application Requirements: 
1. The service should be restarted if it crashes: This was acheived using docker's ```--restart=always``` flag as indicated in the command above. 
2. Capture the logs and have them rotate: The docker container logs were captured in json format and rotated using the following constraints: 
```
--log-opt max-file=3 --log-opt max-size=1k.
```
The rotation can be viewed under the /var/lib/docker/container/containerID/ - The file will only rotate once it reaches a size of 1K and it will only rotate upto 3 files. 
The application logs all requests that are made to the application. Run a few requests to allow the log output to reach 1K to see the rotation. 

3. Configure SSL for the service: While HTTPS is supported in this application, the certificate and key provided are self-signed samples. As a result, curl will throw
the following error: 
```
curl: (60) SSL certificate problem: self signed certificate
``` 
In order to avoid this error disable certificate validation by using the -k option as noted in the commands above. 

References: 
1. Python Flask Documentation 
2. Python Tornado Documentation 
3. Hashlib

##Code Challenge Question: 
Include at least a few sentences to answer the following question: How would your
implementation scale if this were a high throughput service, and how could you improve
that?

```
There are several ways this implementation can be scaled. While the application was created using Flask's development server, it has been coupled with the 
standalone Tornado WSGI server. The Tornado server is suited for Production environments while the Flask development server is not. Since the container is 
currently using the Tornado server instead of the Flask development server it is already suitable for a production deployment. That being said, several 
other factors will affect the scalability of the application. This includes and is not limited to vertical scalability, horizontal scalability and the
 usage of external database(s). For vertical scability it would be important to look at the resources (CPU, MEM, etc) of the underlying host the application 
is running on. Meanwhile, for horizontal scalability there are many things that can be done including but not limited to fronting several identical application 
servers with a load balancer or segregating requests across different servers. Finally, the current implementation stores data in memory. An actual noSQL or SQL 
database would be required to make this fully ready for production. 
```
## Optional: To build the application locally and run: 
1. ```docker build -t <imageName>```
2. ```docker run -d -p 443:443 --name=paxosApp --restart=always --log-opt max-file=2 --log-opt max-size=1k <imageName>```

##Optional: Run using docker-compose: 
1. ```docker-compose up -d```

#Authors
Junaid Kapadia 

# License
Copyright © 2016. All Rights Reserved


