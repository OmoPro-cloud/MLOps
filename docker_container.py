'''
#Run an ephemeral docker container, create the file and then exit
docker run --rm alpine:3.19 sh -c echo Yemi Akomolafe /tmp/hello.txt

#Start a new container and check /tmp
docker run --rm alpine:3.19 sh -c ls /tmp

#Run nginx container and host it on port 8080
docker run -d --name nginx-test -p 8080:80 nginx:alpine
           ------ check https://localhost:8080 to see if live ------

#Check logs
docker logs nginx-test

#Stop and remove container
docker stop nginx-test
docker rm nginx-test

#List all containers, both running and stopped
docker ps -a

#List all local images
docker images

#Remove the nginx:alpine image
docker rmi nginx:alpine

Questions:

1: What happened to data inside an ephemeral container when it stops?
- Any data you create inside the container disappears once it stops. There’s no lasting record unless you set up persistence explicitly
2: What is the difference between an image and a container?
- An image is a static blueprint. A container is the active version of that blueprint, with a writable layer you can modify during runtime
3: Why do we need a registry?
A registry is a central hub where images are stored and shared. It makes it easy to reuse, distribute, and collaborate on images without rebuilding everything from scratch

'''