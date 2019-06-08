# docker-client-request

2 containers testing communication

python

Flashk

 `docker build -t server ./server/.`
 
 `docker build -t client ./client/.`

 `docker run -d -p 8080:8080 server`

 `docker run -d -p 8888:8888 client`
 
 or

 `docker-compose up`
