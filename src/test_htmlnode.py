import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_parent_node(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "This is the first paragraph"), LeafNode("b", "This is some bold text")],
        )
        node2 = '<div><p>This is the first paragraph</p><b>This is some bold text</b></div>'
        self.assertEqual(node.to_html(), node2)

    def test_nested_parent_node(self):
        node = ParentNode(
                "div",
                [
                    ParentNode("div", [LeafNode("b", "bold text"), LeafNode("i", "italic text")]),
                    LeafNode("p", "paragraph text")
                ],
            )
        node2 = '<div><div><b>bold text</b><i>italic text</i></div><p>paragraph text</p></div>'
        self.assertEqual(node.to_html(), node2)

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "main":
    unittest.main()
