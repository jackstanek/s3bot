"""Tools for adding and retrieving user emails."""

import csv
import os

from s3bot import SHARED_BASE

class UserEmailRecord(dict):
    """A record of all user emails known to the system. This is a subclass
    of dict, so all dict methods are available. Note that it is not
    safe to modify more than one instance instantiated at a time, as
    data loss may occur.
    """

    email_record_path = os.path.join(SHARED_BASE, "emails.txt")

    def __init__(self):
        super().__init__()

        with open(self.email_record_path, "r") as email_file:
            reader = csv.reader(email_file, delimiter=' ')
            for row in reader:
                user, email = row
                self[user] = email

    def dump(self):
        """Dump the contents of the email record to disk."""
        with open(self.email_record_path, "w") as email_file:
            writer = csv.writer(email_file, delimiter=' ')
            for user, email in self.items():
                writer.writerow([user, email])
