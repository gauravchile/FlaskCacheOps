FROM nginx:latest

# Install curl for health checks
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy both configs into the container (you’ll use only one via docker-compose)
COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx.conf.prod /etc/nginx/nginx.conf.prod

