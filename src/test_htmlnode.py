import unittest
from htmlnode import HTMLNode

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

if __name__ == "main":
    unittest.main()
