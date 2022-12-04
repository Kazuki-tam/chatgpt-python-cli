# ChatGPT CLI with Python

This is a sample repository to use ChatGPT by CLI command.

## How to use

### 1. Create an `.env` file

### 1. Create a Docker image, build a container, and start the container

```bash
docker compose up -d --build
```

### 2. Connect to container

```bash
docker compose exec python3 bash
```

### 3. Execute python file
```bash
python -m chatgpt
```

### Other Commands

Delete container

```bash
exit
docker compose down
```

Restart container

```bash
docker compose up -d
```
