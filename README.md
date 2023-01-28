# GPT CLI with Python

This is a sample repository to use GPT-3 by CLI command.

## Status

[![Release (latest by date)](https://img.shields.io/github/v/release/Kazuki-tam/gpt-python-cli)](https://github.com/Kazuki-tam/gpt-python-cli/releases/tag/v0.0.1)
[![Issues](https://img.shields.io/github/issues/Kazuki-tam/gpt-python-cli)](https://github.com/Kazuki-tam/gpt-python-cli/issues)
![Maintenance](https://img.shields.io/maintenance/yes/2023)
![Release date](https://img.shields.io/github/release-date/Kazuki-tam/gpt-python-cli)

## How to use

### 1. Create a `.env` file
You need to create a `.env` file in `gpt` directory.

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
python -m gpt
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
