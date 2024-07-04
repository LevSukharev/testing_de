import unittest
from src.validators import password_validate, email_validate
from src.interfaceAPI import get_user
from src.settings import settings
from src.model import User


class TestValidators(unittest.TestCase):

    def test_password_validation(self):

        self.assertEqual(password_validate(r"""ABCDEFGHIJKLMNOPQRSTUVWXYZ
                                abcdefghijklmnopqrstuvwxyz
                                0123456789
                                !#$%&'()*+,- ./:;<=>?@[\]^_`{|}~"""), True)

        self.assertEqual(password_validate(r"""ABCDEFGHIJ
                                abcdefghijk
                                01234
                                !#$%&'()*+,- """), True)

        self.assertEqual(password_validate(r"""ABCDEFGHIJKLMNOPQRSTUVWXYZ
                                abcdefghijklmnopqrstuvwxyz
                                0123456789"""), False)

        self.assertEqual(password_validate(r"""ABCDEFGHIJKLMNOPQRSTUVWXYZ
                                abcdefghijklmnopqrstuvwxyz"""), False)

        self.assertEqual(password_validate(r"""ABCDEFGHIJKLMNOPQRSTUVWXYZ"""), False)

        self.assertEqual(password_validate(r"""abcdefghijklmnopqrstuvwxyz"""), False)

        self.assertEqual(password_validate(r"""0123456789"""), False)

        self.assertEqual(password_validate(r"""!#$%&'()*+,- ./:;<=>?@[\]^_`{|}~"""), False)


    def test_email_validate(self):

        self.assertEqual(email_validate('john.doe@example.com'), True)

        self.assertEqual(email_validate('jane_doe123@subdomain.example.co.uk'), True)

        self.assertEqual(email_validate('user.name+tag+sorting@example.com'), True)

        self.assertEqual(email_validate('x@example.io'), True)

        self.assertEqual(email_validate('niceandsimple@example.com'), True)

        self.assertEqual(email_validate('plainaddress'), False)

        self.assertEqual(email_validate('@missingusername.com'), False)

        self.assertEqual(email_validate('username@.com.my'), False)

        self.assertEqual(email_validate('username@com..com'), False)

        self.assertEqual(email_validate('username@domain@domain.com'), False)


class TestApi(unittest.TestCase):

    def test_obtaining(self):

        self.assertEqual(type(get_user(url_api=settings.url_api, count=1)), list)

        self.assertEqual(type(get_user(url_api=settings.url_api, count=1)[0]), User)
