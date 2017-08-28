"""Tools for adding and retrieving user emails."""

import csv
import os

from s3bot import SHARED_BASE

# pylint: disable=too-few-public-methods
class UserEmailRecordDialect(csv.Dialect):
    """Simple dialect for the email record file."""
    delimiter = " "
    lineterminator = "\n"
    quoting = csv.QUOTE_NONE


class UserEmailRecord(dict):
    """A record of all user emails known to the system. This is a subclass
    of dict, so all dict methods are available. Note that it is not
    safe to modify more than one instance instantiated at a time, as
    data loss may occur.
    """

    email_record_path = os.path.join(SHARED_BASE, "emails.txt")
    fieldnames = ("user", "email")

    def __init__(self):
        super().__init__()

        with open(self.email_record_path, "r") as email_file:
            reader = csv.DictReader(email_file,
                                    fieldnames=self.fieldnames,
                                    dialect=UserEmailRecordDialect)
            for row in reader:
                user, email = row["user"], row["email"]
                self[user] = email

    def dump(self):
        """Dump the contents of the email record to disk."""
        with open(self.email_record_path, "w") as email_file:
            writer = csv.DictWriter(email_file,
                                    fieldnames=self.fieldnames,
                                    dialect=UserEmailRecordDialect)

            for user, email in self.items():
                writer.writerow({user: email})
