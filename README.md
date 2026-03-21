#  Docker Compose – Complete Guide 

##  What is Docker Compose?

Docker Compose is a tool used to define and run **multi-container Docker applications** using a YAML file.

Instead of running multiple `docker run` commands, you define everything in one file:

```yaml
services:
  app:
  db:
````

---

## Why Use Docker Compose?

* Manage multi-container apps easily
* Define infrastructure as code
* Simplify development & testing
* One command to start everything

---

## ️ Key Concepts

###  1. Services

Each container is called a service.

```yaml
services:
  fastapi:
  redis:
```

---

### 2. Networks

* Default network is created automatically
* Services communicate using **service names**

```python
redis://redis:6379
```

---

###  3. Volumes

Used for **data persistence**

```yaml
volumes:
  - redis_data:/data
```

---

###  4. Environment Variables

```yaml
env_file:
  - .env
```

---

###  5. Ports

```yaml
ports:
  - "8000:8000"
```

Format:

```
HOST_PORT:CONTAINER_PORT
```

---

###  6. depends_on

```yaml
depends_on:
  - redis
```

Controls startup order (not readiness)

---



#  Ports vs Expose

| Feature                | ports | expose            |
| ---------------------- | ----- | ----------------- |
| Accessible from host   | Yes | No              |
| Internal communication | Yes   | Yes         |
| Use case               | APIs  | Internal services |

---

#  Volume Types

## 1. Named Volume (Production)

```yaml
volumes:
  redis_data:
```

## 2. Bind Mount (Development)

```yaml
- ./app:/app
```

## 3. tmpfs (Memory)

```yaml
tmpfs:
  - /data
```

---


## YAML File Fields Explained

| Field         | Meaning                                                                 |
|---------------|-------------------------------------------------------------------------|
| `services`    | Defines each container (service) in the application.                    |
| `image`       | Docker image to use for the container.                                  |
| `build`       | Instructions to build an image from a Dockerfile.                       |
| `ports`       | Maps host ports to container ports (`HOST:CONTAINER`).                  |
| `volumes`     | Mounts storage (named, bind, or tmpfs) for persistence or sharing.      |
| `environment` | Environment variables passed into the container.                        |
| `env_file`    | External `.env` file containing environment variables.                  |
| `networks`    | Defines custom networks for communication between services.             |
| `depends_on`  | Specifies startup order of services (not readiness).                    |
| `command`     | Overrides the default command in the image.                             |
| `restart`     | Policy for restarting containers (`always`, `on-failure`, etc.).        |

---

# Docker Compose Commands Cheat Sheet 

### Start Services
```bash
docker compose up
```
Starts all services defined in `docker-compose.yml` in the foreground.

```bash
docker compose up -d
```
Starts services in **detached mode** (runs in background).

```bash
docker compose up --build
```
Rebuilds images before starting containers.

```bash
docker compose up -d --build
```
Rebuilds images and runs containers in background.

---

### Stop Services
```bash
docker compose stop
```
Stops running containers but does **not remove them**.

---

### Remove Containers
```bash
docker compose down
```
Stops and removes containers, networks, and default volumes.

```bash
docker compose down -v
```
Also removes **named volumes** created by Compose.

```bash
docker compose down --rmi all
```
Removes containers, volumes, and **images** built by Compose.

---

### Restart
```bash
docker compose restart
```
Restarts all running services.

---

###  Build
```bash
docker compose build
```
Builds images defined in the Compose file.

```bash
docker compose build --no-cache
```
Builds images **without using cache** (fresh build).

---

### Status
```bash
docker compose ps
```
Shows status of containers (running, stopped, ports, etc.).

---

###  Logs
```bash
docker compose logs
```
Displays logs from all services.

```bash
docker compose logs -f
```
Streams logs in real time (follow mode). Eg. using fastapi app
```bash
services:
  fastapi:
    build: .
    ports:
      - "8000:8000"
```

```bash
docker compose logs fastapi
```
Shows logs only for the `fastapi` service.

---

###  Exec into Container
```bash
docker compose exec fastapi sh
```
Opens a shell inside the `fastapi` container.

```bash
docker compose exec fastapi bash
```
Opens a Bash shell (if available in the container).

---

###  Run One-off Command
```bash
docker compose run fastapi ls
```
Runs a one-time command (`ls`) inside the `fastapi` container.

---

### Validate Config
```bash
docker compose config
```
Validates and prints the final configuration (after resolving variables).

---

### Scale Services
```bash
docker compose up --scale fastapi=3
```
Runs **3 replicas** of the `fastapi` service.

---

### Cleanup
```bash
docker system prune -a
```
Removes unused containers, networks, images, and volumes.  
*Dangerous**: deletes everything not actively used.

---
