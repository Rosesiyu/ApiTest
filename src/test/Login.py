# -- coding: utf-8 --
import unittest
import requests
import HTMLTestRunner


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://www.fitshang.com/api/device/login"

    def testLogin1(self):   #账户密码均正确
        form = {"name": "3934303530374701002a002b", "password": "fits502"}
        r = requests.post(self.url, data = form)
        self.assertTrue("null" in r.text)

    def testLogin2(self):   #仅密码为空
        form = {"name": "3934303530374701002a002b", "password": " "}
        r = requests.post(self.url, data = form)
        self.assertTrue("password" in r.text)

    def testLogin3(self):   #仅账号为空
        form = {"name": " ", "password": "fits502"}
        r = requests.post(self.url, data=form)
        self.assertTrue("name" in r.text)

    def testLogin4(self):   #账号与密码均为空
        form = {"name": " ", "password": " "}
        r = requests.post(self.url, data=form)
        self.assertTrue("password" in r.text and "name" in r.text)

    def testLogin5(self):   #仅密码错误
        form = {"name": "3934303530374701002a002b", "password": "50211"}
        r = requests.post(self.url, data=form)
        self.assertTrue("message" in r.text)

    def testLogin6(self):   #仅账号错误
        form = {"name": "02a002b", "password": "fits502"}
        r = requests.post(self.url, data=form)
        self.assertTrue("message" in r.text)

    def testLogin7(self):   #账号与密码都错误
        form = {"name": "530374701002a002b", "password": "fs502"}
        r = requests.post(self.url, data=form)
        self.assertTrue("message" in r.text)


def suite():
    loginTestCase = unittest.makeSuite(LoginTest, "test")
    return loginTestCase


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
    # unittest.main()
