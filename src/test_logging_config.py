# tests/test_logging_config.py
import unittest
from logging_config import logger

class TestLoggingConfig(unittest.TestCase):
    def test_logger_creation(self):
        self.assertIsNotNone(logger)

    def test_log_formatter(self):
        formatter = logger.handlers[0].formatter
        self.assertEqual(formatter._fmt, '%(asctime)s; %(name)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    unittest.main()