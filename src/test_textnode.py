import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_assertEqual(self):
        first = TextNode("This", TextType.LINK, "boot.dev")
        second = TextNode("This", TextType.LINK, "boot.dev")
        self.assertEqual(first, second)
    def test_assertNotEqual(self):
        first = TextNode("Not text", TextType.ITALIC, None)
        second = TextNode("This is text", TextType.ITALIC, None)
        self.assertNotEqual(first, second)
    def test_not_valid_texttype(self):
        node1 = TextNode("This is text", "BOLD", "boot.dev")
        self.assertNotIn(node1.text_type, TextType)
    def test_valid_texttype(self):
        node1 = TextNode("This is text", TextType.IMAGE, "boot.dev")
        self.assertIn(node1.text_type, TextType)
    def test_not_valid_URL(self):
        node1 = TextNode("This is text", TextType.CODE, 1)
        self.assertFalse(node1.url is str)
    

if __name__ == "__main__":
    unittest.main()
    