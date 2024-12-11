import unittest

from htmlnode import LeafNode
from textnode import TextType, TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node,node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.TEXT, "yrl.com")
        node2 = TextNode("This is a text node", TextType.TEXT, "yrl.com")
        self.assertEqual(node,node2)

    def test_eq_3(self):
        node = TextNode("This is a text node", TextType.BOLD, "yrl.com")
        node2 = TextNode("This is a text node", TextType.TEXT, "yrl.com")
        self.assertNotEqual(node,node2)

    def test_eq_4(self):
        node = TextNode("This is also text node", TextType.TEXT, "yrl.com")
        node2 = TextNode("This is a text node", TextType.TEXT, "yrl.com")
        self.assertNotEqual(node,node2)

    def test_eq_5(self):
        node = TextNode("This is also text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT, "yrl.com")
        self.assertNotEqual(node,node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
         
if __name__ == "main" :
    unittest.main()
