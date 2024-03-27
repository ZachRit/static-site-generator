import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_diff(self):
        node = TextNode("This is a bold text node", "bold")
        node2 = TextNode("This is an italic text node", "italic")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text nod with a url", "text", "https://www.google.com")
        node2 = TextNode("This is a text nod with a url", "text", "https://www.google.com")
        self.assertEqual(node, node2)

if __name__ == "main":
    unittest.main()
