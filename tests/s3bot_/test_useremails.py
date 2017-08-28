"""Tests for the user email tool."""

import unittest
from unittest import mock
from io import StringIO

from s3bot.useremails import UserEmailRecord

class TestUserEmailRecord(unittest.TestCase):
    """Tests for user email lookup."""
    def setUp(self):
        self.user = "person"
        self.email = "me@example.com"
        self.record = "{} {}".format(self.user,
                                     self.email)

        self.mocked_open = mock.MagicMock(
            return_value=StringIO(initial_value=self.record))

    def test_user_email_found(self):
        """Test that an existing email is found correctly."""
        with mock.patch("s3bot.useremails.open", self.mocked_open):
            record = UserEmailRecord()
            email = record.get("person")
            self.assertEqual(email, self.email)

    def test_email_record_dump(self):
        """Test that emails can be loaded and dumped successfully."""
        newname, newemail = "newguy", "new@example.com"
        with mock.patch("csv.DictWriter.writerow") as mock_csv_writerow:
            with mock.patch("s3bot.useremails.open", self.mocked_open):
                record = UserEmailRecord()
                record[newname] = newemail

                new_mock_file = StringIO()
                self.mocked_open.return_value = new_mock_file
                record.dump()
                mock_csv_writerow.assert_any_call({self.user: self.email})
                mock_csv_writerow.assert_any_call({newname: newemail})
