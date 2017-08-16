"""Wrapper for the freeze.sh bash script."""

from s3bot import SHARED_LOCAL_ROOT

import os
import subprocess

FREEZE_SH_SCRIPT_PATH = os.path.join(SHARED_LOCAL_ROOT, "freezer", "freeze.sh")

def freeze(path):
    """Queue a freeze.sh job for the specified file."""
    pass
