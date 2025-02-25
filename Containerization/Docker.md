# Docker and Docker Compose Installation
```bash
sudo dnf -y install dnf-plugins-core
sudo dnf-3 config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl enable --now docker
sudo docker run hello-world
sudo systemctl start docker
sudo systemctl enable docker
docker --version
```

- Installed Docker and Docker Compose.
- Enabled and started the Docker service.
- Verified the installation by running `hello-world`.

---

# Writing a Dockerfile
```bash
mkdir my-nginx
cd my-nginx
echo "<h1>Welcome to My Custom Nginx Container</h1>" > index.html
nano Dockerfile
```
**Dockerfile:**
```dockerfile
# Use the official Nginx base image
FROM nginx:latest

# Set working directory inside the container
WORKDIR /usr/share/nginx/html

# Copy the custom index.html to the container
COPY index.html index.html

# Expose port 80 (Nginx default port)
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
```
```bash
docker build -t my-nginx:v1 .
```


- Created a new directory for the Nginx Docker project.
- Wrote a simple `Dockerfile` to serve a custom `index.html`.
- Built the Docker image with the tag `my-nginx:v1`.

---

# Running the Nginx Container
```bash
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
docker images
docker run -d -p 8080:80 --name my-nginx-container my-nginx:v1
```

- Added the current user to the Docker group to run Docker without `sudo`.
- Ran `hello-world` again to verify the changes.
- Listed available images.
- Ran the Nginx container on port 8080.

---

# Pushing and Pulling Docker Images from Docker Hub
```bash
docker login
docker tag my-nginx:v1 riyasawant/my-nginx:v1
docker push riyasawant/my-nginx:v1
docker pull riyasawant/my-nginx:v1
```

- Logged into Docker Hub.
- Tagged the local `my-nginx:v1` image with the Docker Hub repository.
- Pushed the image to Docker Hub.
- Pulled the image back from Docker Hub to verify it was uploaded successfully.

---

# Setting Up a Local Docker Registry
```bash
docker run -d -p 5000:5000 --name my-registry registry:2
docker tag my-nginx:v1 localhost:5000/my-nginx:v1
docker push localhost:5000/my-nginx:v1
docker pull localhost:5000/my-nginx:v1
```

- Ran a private Docker registry on port 5000.
- Tagged and pushed an image to the local registry.
- Pulled the image from the local registry to verify it works.

---

# Checking Local Registry Contents
```bash
curl -X GET http://localhost:5000/v2/_catalog
curl -X GET http://localhost:5000/v2/my-nginx/tags/list
```

- Queried the local Docker registry for available repositories and tags.

---

# Docker Compose Installation and Verification
```bash
docker compose version
sudo dnf install docker-compose-plugin
docker compose version
```

- Checked for Docker Compose.
- Installed the Docker Compose plugin.
- Verified the installation.

---

# Setting Up a Docker Compose Project
```bash
mkdir my_docker_compose_project
cd my_docker_compose_project
nano docker-compose.yml
```

- Created a new directory for a Docker Compose project.
- Opened `docker-compose.yml` for editing.

---

# Running Docker Compose Services
```bash
docker compose up -d
docker ps
```

- Started services defined in `docker-compose.yml` in detached mode.
- Listed running containers to verify the services were up.

---

# Connecting to PostgreSQL Container
```bash
docker exec -it postgres_container psql -U myuser -d mydatabase
```

- Connected to the PostgreSQL container using `psql`.

---

# Managing Docker Compose Services
```bash
nano docker-compose.yml
docker compose up -d
docker ps
```

- Edited `docker-compose.yml`.
- Restarted the services using Docker Compose.
- Verified the running containers.

---

# Command History Check
```bash
history
```

- Displayed the history of executed commands.

