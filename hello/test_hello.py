"""sample test"""
import unittest

from hello import hello


class TestHello(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        self.assertEqual(hello('world'), 'bye world')

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(hello(u'world'), u'bye world')
