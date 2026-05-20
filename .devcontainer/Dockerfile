FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

# Astral公式の方法で uv を一発インストール
COPY --from=ghcr.io/astral-sh/ruff:latest /ruff /usr/local/bin/ruff
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /workspace