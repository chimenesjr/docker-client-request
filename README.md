# docker-client-request

2 containers testing communication

python

Flashk

 `$ docker build -t server ./server/.`
 
 `$ docker build -t client ./client/.`

 `$ docker run -d -p 8080:8080 --name server server`

 `$ docker run -d -p 8888:8888 --name client client`
 
 or

 `$ docker-compose up`

or

 `$ gcloud app deploy`

 or

 *****---- in progress 

 `$ docker tag python-server gcr.io/[PROJECT-ID]/python-server`

 `$ docker tag python-client gcr.io/[PROJECT-ID]/python-client`

 `$ sudo gcloud docker -- push gcr.io/[PROJECT-ID]/python-server`

 `$ sudo gcloud docker -- push gcr.io/[PROJECT-ID]/python-server`

 `$ kubectl apply -f `

 `$ kubectl expose pod python-client --type=LoadBalancer --name=my-service`
