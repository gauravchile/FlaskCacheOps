from flask import Flask, jsonify, render_template, request
import redis, os, socket, datetime, logging

app = Flask(__name__)

# ---------------------------------
# Redis Configuration
# ---------------------------------
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
cache = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

# ---------------------------------
# Global Variables
# ---------------------------------
start_time = datetime.datetime.utcnow()

# ---------------------------------
# Logging Configuration
# ---------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# ---------------------------------
# Helper Functions
# ---------------------------------
def get_cache_status():
    """Check if Redis is available."""
    try:
        cache.ping()
        return "Redis ✅"
    except redis.exceptions.ConnectionError:
        return "Memory ⚡ (Redis unavailable)"


def get_visits():
    """Fetch and increment visits in Redis."""
    try:
        visits = int(cache.get("visits") or 0)
        visits += 1
        cache.set("visits", visits)
        return visits
    except redis.exceptions.ConnectionError:
        return 0


# ---------------------------------
# Routes
# ---------------------------------
@app.before_request
def log_request_info():
    logging.info(f"Request received on {request.path} from {request.remote_addr}")


@app.route('/health')
def health():
    """Healthcheck endpoint for Docker."""
    status = "healthy ✅" if get_cache_status() == "Redis ✅" else "degraded ⚠️"
    return jsonify({
        "service": "FlaskCacheOps API",
        "status": status,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }), 200


@app.route('/')
def index():
    """Root endpoint returning JSON status."""
    uptime = datetime.datetime.utcnow() - start_time
    container_name = os.environ.get("HOSTNAME", socket.gethostname())  # ✅ fixed
    visits = get_visits()

    data = {
        "cached": True,
        "environment": "production",
        "host": container_name,
        "message": f"Hello from container {container_name} 👋",
        "service": "FlaskCacheOps API",
        "status": "healthy ✅",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "uptime": str(uptime).split(".")[0],
        "version": "v1.0.0",
        "visits": visits
    }
    return jsonify(data)


@app.route('/dashboard')
def dashboard():
    """Visual dashboard with cache info."""
    uptime = datetime.datetime.utcnow() - start_time
    container_name = os.environ.get("HOSTNAME", socket.gethostname())  # ✅ fixed
    cache_status = get_cache_status()
    visits = get_visits()

    data = {
        "cached": True,
        "environment": "production",
        "host": container_name,
        "message": f"Hello from container {container_name} 👋",
        "service": "FlaskCacheOps API",
        "status": "healthy ✅",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "uptime": str(uptime).split(".")[0],
        "version": "v1.0.0",
        "visits": visits
    }

    return render_template(
        "dashboard.html",
        data=data,
        container_name=container_name,
        cache_status=cache_status
    )


# ---------------------------------
# Entry Point
# ---------------------------------
if __name__ == "__main__":
    logging.info("🚀 Starting FlaskCacheOps API...")
    app.run(host="0.0.0.0", port=5000)

