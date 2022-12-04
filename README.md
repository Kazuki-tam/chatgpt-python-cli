# ChatGPT CLI with Python

This is a sample repository to use ChatGPT by CLI command.

## How to use

### 1. Create a `.env` file
You need to create a `.env` file in `chatgpt` directory.

### 2. Create a Docker image, build a container, and start the container

```bash
docker compose up -d --build
```

### 3. Connect to container

```bash
docker compose exec python3 bash
```

### 4. Execute python file
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
