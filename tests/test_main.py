import unittest

from TryPydantic.main import add_one, create_user


class TestMain(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(5), 6)

    def test_create_user(self):
        user = create_user()
        self.assertEqual(user.dict(), dict(user))
