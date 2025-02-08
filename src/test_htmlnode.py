import unittest

from htmlnode import HTMLNode

attr_dict = {"href": "boot.dev", "target": "_blank"}


class TestHTMLNode(unittest.TestCase):
    def test_isInstance(self):
        node = HTMLNode("<a>", "Mr. Boots!", None, attr_dict)    
        self.assertIsInstance(node, HTMLNode)
    
    
        
    