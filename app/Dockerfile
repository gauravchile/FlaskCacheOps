# ===============================
# FlaskCacheOps - Flask Build Image
# ===============================

# Stage 1: Build dependencies
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user -r requirements.txt

# Stage 2: Production runtime
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local/

COPY . .

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

ENV PATH=/root/.local/bin:$PATH
ENV FLASK_ENV=production

# Healthcheck for container status
HEALTHCHECK CMD curl -f http://localhost:5000/health || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers=3", "--timeout", "120"]

