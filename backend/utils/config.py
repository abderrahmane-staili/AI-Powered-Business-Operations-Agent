import os

DATABASE_URL = os.getenv("DATABASE_URL", "")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
API_KEY = os.getenv("API_KEY", "")
PLAYWRIGHT_URL = os.getenv("PLAYWRIGHT_URL", "http://host.docker.internal:3000/execute")
PLAYWRIGHT_API_KEY = os.getenv("PLAYWRIGHT_API_KEY", "")
