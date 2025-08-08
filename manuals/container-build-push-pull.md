# Container Build, Push, and Pull

## Docker Registry (Private Container Registry)

### Create a Registry Container

```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

This command runs a Docker container that acts as a private registry for storing Docker images. Here's a breakdown of the command:
- `-d`: Runs the container in detached mode (in the background)
- `-p 5000:5000`: Maps port 5000 of your host machine to port 5000 of the container
- `--restart=always`: Ensures the registry starts automatically if the server reboots
- `--name registry`: Gives the container a memorable name
- `registry:2`: The official Docker registry image to use

### Create a Registry with Persistent Storage

For production use, you should mount a volume to persist registry data even if the container is removed:

```bash
docker run -d -p 5000:5000 --restart=always --name registry \
  -v /opt/registry:/var/lib/registry \
  registry:2
```

This command adds persistent storage:
- `-v /opt/registry:/var/lib/registry`: Mounts a host directory (`/opt/registry`) to the container's data directory (`/var/lib/registry`)
- All pushed images will be stored in `/opt/registry` on your host machine
- Data persists even if you stop, remove, or recreate the registry container

Make sure the host directory exists and has proper permissions:

```bash
sudo mkdir -p /opt/registry
sudo chown -R 1000:1000 /opt/registry
```

**Command breakdown:**
- `sudo`: Run the command with administrator privileges
- `chown`: Change ownership of files and directories
- `-R`: Recursive flag - applies the ownership change to all subdirectories and files
- `1000:1000`: Sets both user ID and group ID to 1000
  - First `1000`: User ID (UID) - typically the first regular user on Linux systems
  - Second `1000`: Group ID (GID) - typically the primary group of that user
- `/opt/registry`: The target directory path

**Why this matters:**
The Docker registry container runs as user ID 1000 internally. Without proper ownership, the registry won't be able to write to the mounted volume, causing permission errors when pushing images.

### List Containers from a Registry

```bash
curl http://192.168.0.134:5000/v2/_catalog | jq . 
```

Response:
```json
{
  "repositories": [
    "my-pthon-app-amd64",
    "my-python-app"
  ]
}
```

### List Container Image Tags

```bash
curl http://192.168.0.134:5000/v2/my-python-app/tags/list | jq . 
```

Response:
```json
{
  "name": "my-python-app",
  "tags": [
    "latest"
  ]
}
```

### Push a Container to the Registry

To push a container image to your private registry, first tag your image with the registry's address, then push it:

```bash
docker tag my-python-app:latest 192.168.0.134:5000/my-python-app:latest
docker push 192.168.0.134:5000/my-python-app:latest
```

- `docker tag`: Tags the image with the registry's address so Docker knows where to push it
- `docker push`: Uploads the image to your registry

### Pull a Container from the Registry

To pull the image from your private registry:

```bash
docker pull 192.168.0.134:5000/my-python-app:latest
```

This downloads the image to your local Docker environment.

**Notice:**
If you are using a self-hosted Docker registry, you may need to configure Docker to allow insecure registries. This is necessary if your registry does not use HTTPS.

You can reverse proxy your registry with Nginx or Apache to enable HTTPS, but if you want to use HTTP for testing, follow these steps:

```bash
sudo nano /etc/docker/daemon.json
```

Add the following lines to allow insecure registries:

```json
{
  "insecure-registries": [
    "192.168.0.134:5000"
  ]
}
```

Then restart the Docker service:

```bash
sudo systemctl restart docker
```

## Multi-Architecture Container Builds

### Build for a Specific Architecture

```bash
docker buildx build --platform linux/amd64 -t 192.168.0.134:5000/my-python-app-amd64:latest-amd64 --push .
```

This command builds a Docker image for the specified platform (in this case, `linux/amd64`) and pushes it to your private registry. Here's a breakdown of the command:

- `docker buildx build`: Uses Docker Buildx to build the image
- `--platform linux/amd64`: Specifies the target platform for the image (can be `linux/amd64`, `linux/arm64`, etc.)
- `-t 192.168.0.134:5000/my-python-app-amd64:latest-amd64`: Tags the image for your registry and architecture (can be DockerHub or a private registry)
- `--push`: Automatically pushes the built image to the registry
- `.`: Specifies the build context (current directory) with the Dockerfile and other necessary files

### Build for Multiple Architectures

You can build and push for multiple architectures by specifying a comma-separated list:

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t 192.168.0.134:5000/my-python-app:multiarch --push .
```

This will create and push images for both `amd64` and `arm64` platforms under the same tag.

