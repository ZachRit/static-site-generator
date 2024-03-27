import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_convert_props(self):
        node = HTMLNode(
            "div",
            "This is a test",
            None,
            {"class": "button", "margin": "small"}
        )
        node2 = ' class="button" margin="small"'
        self.assertEqual(node.props_to_html(), node2)

    def test_leaf_node(self):
        node = LeafNode(
            "p",
            "This is a paragraph of text"
        )
        node2 = "<p>This is a paragraph of text</p>"
        self.assertEqual(node.to_html(), node2)

    def test_to_html_no_tag(self):
        node = LeafNode(
            None,
            "This should be rendered as is"
        )
        node2 = "This should be rendered as is"
        self.assertEqual(node.to_html(), node2)

    def render_leaf_html(self):
        node = LeafNode(
            "div",
            "Hello world. This is a div",
            {"class": "hello", "id": "world"}
        )
        node2 = '<div class="hello" id="world">Hello world. This is a div</div>'
        self.assertEqual(node.to_html(), node2)

if __name__ == "main":
    unittest.main()
