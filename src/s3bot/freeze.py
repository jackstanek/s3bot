"""Wrapper for the freeze.sh bash script."""

import getpass
import os
import subprocess

from s3bot import SHARED_BASE
from s3bot.useremails import UserEmailRecord

FREEZE_SH_SCRIPT_PATH = os.path.join(SHARED_BASE, "freezer", "freeze.sh")

def freeze(path):
    """Queue a freeze.sh job for the specified file."""
    user = getpass.getuser()
    email = UserEmailRecord().get(user)

    if not os.access(path, os.R_OK):
        raise FileNotFoundError("could not access {}".format(path))

    cmd = ["qsub",
           "-F", path,
           "-M", email,
           "-q", "lab-long",
           FREEZE_SH_SCRIPT_PATH]

    try:
        subprocess.run(cmd)
    except subprocess.CalledProcessError as cpe:
        print("Could not queue job: return code {}".format(cpe.returncode))
