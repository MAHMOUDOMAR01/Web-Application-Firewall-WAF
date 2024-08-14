import unittest
from waf.checker import (
    check_for_sql_injection,
    check_for_xss,
    check_for_lfi,
    check_for_rfi,
    check_for_csrf
)

class TestWAFChecks(unittest.TestCase):

    def test_sql_injection(self):
        self.assertTrue(check_for_sql_injection("SELECT * FROM users WHERE username='admin'"))
        self.assertTrue(check_for_sql_injection("' OR '1'='1' --"))
        self.assertFalse(check_for_sql_injection("Hello World"))

    def test_xss(self):
        self.assertTrue(check_for_xss("<script>alert('XSS')</script>"))
        self.assertTrue(check_for_xss("<img src='x' onerror='alert(1)'>"))
        self.assertFalse(check_for_xss("Hello World"))

    def test_lfi(self):
        self.assertTrue(check_for_lfi("../../etc/passwd"))
        self.assertTrue(check_for_lfi("/etc/shadow"))
        self.assertFalse(check_for_lfi("Hello World"))

    def test_rfi(self):
        self.assertTrue(check_for_rfi("http://malicious.com"))
        self.assertTrue(check_for_rfi("https://malicious.com"))
        self.assertFalse(check_for_rfi("Hello World"))

    def test_csrf(self):
        self.assertTrue(check_for_csrf("<input type='hidden' name='csrf_token' value='token'>"))
        self.assertTrue(check_for_csrf("csrf_token=abc123"))
        self.assertFalse(check_for_csrf("Hello World"))

if __name__ == '__main__':
    unittest.main()
