import unittest

from TryPydantic.from_xml import User
from tests import TESTS_DIR


class TestMain(unittest.TestCase):

    def test_main(self):
        file_path = TESTS_DIR / 'data' / "user.xml"
        file_content = file_path.read_text()
        user = User.from_xml(file_content)
        self.assertEqual(user.Id, 2138)
        self.assertEqual(user.LoggedIn, True)
