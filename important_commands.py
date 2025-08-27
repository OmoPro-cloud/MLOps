#Docker commands
#run -d --name web -p 8088:80 nginx:alpine
#docker logs web -- this logs when someone has visited a server
#docker stop (image/file_name)
#docker rm web -- deletes a container('web' in this case)
#docker run nginx

#an image is a file
#a container is a running image
#a registry is a place where you can downlaid files and applications
#dockerhub is an example of a registry

'''

Tasks

Run an ephemeral container:

Use alpine:3.19.

Inside the container, create a file /tmp/hello.txt and write your name into it.

Exit the container.

Prove the file does not exist anymore by starting a new alpine container and checking /tmp.

Work with Nginx:

Run an nginx:alpine container on port 8080.

Verify it works by visiting http://localhost:8080 in your browser.

Check its logs with docker logs.

Stop and remove the container.

Explore images & containers:

List all containers (running and stopped).

List all images on your system.

Remove the nginx:alpine image from your local system.

Show what happens if you try to run nginx:alpine again after removing it.

Mini-writeup (2–3 sentences each):

What happens to data inside an ephemeral container when it stops?

What is the difference between an image and a container?

Why do we need a registry?

'''