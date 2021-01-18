import unittest
from app import main, home_work


class TestClass(unittest.TestCase):
    def setUp(self):

        self.date_url = 'http://date.jsontest.com/'
        self.ip_url = 'http://ip.jsontest.com/'

    def test_date_work_successfully(self):

        self.assertTrue(main(self.date_url))

    def test_empty_url(self):

        self.assertFalse(main())

    def test_no_date_in_response(self):

        with self.assertRaises(Exception):
            main(self.ip_url)

    def test_home_work(self):

        self.assertIsNotNone(home_work())
