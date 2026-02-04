FROM python:3.14-slim

# Set environment variable(filesystem hygiene & correct real-time logging)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
COPY backend/pyproject.toml backend/uv.lock ./
RUN uv sync --frozen --no-dev
COPY backend/ .
EXPOSE 8000
CMD [ "uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]
