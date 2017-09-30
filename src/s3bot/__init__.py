"""s3bot, the cool tool for doing cool stuff."""

import os

# Shared local path
SHARED_BASE = os.environ.get("SHARED_BASE") or \
              os.path.join("/", "home", "mccuem", "shared", ".local")

# S3 URL
S3_BASE_URL = "https://s3.msi.umn.edu"
