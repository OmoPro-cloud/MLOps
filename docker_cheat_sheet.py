# Build & run
docker build -t flask-mobilenet:1.0 .
docker run --rm -p 8080:8080 flask-mobilenet:1.0

# With compose
docker compose up --build -d
docker compose logs -f app
docker compose down

# Volumes & networks
docker volume ls
docker network ls
docker network inspect <project>_app_net

# Exec & logs
docker ps
docker logs -f mobilenet_app
docker exec -it mobilenet_app sh

'''
ASSIGNMENTS:

RESEARCH HOW TO UPLOAD YOUR CONTAINER ONTO DOCKER HUB

CREATE AN API APP LIKE THE WEATHER ONE YOU MADE, CONTAINERIZE IT(PUT IT IN A DOCKER)
'''