import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode()       
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_1(self):
        node = HTMLNode(None, None, None, {
            "href": "https://www.google.com", 
            "target": "_blank",
        })       
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("p", "the text inside a para", None, {
            "href": "https://www.google.com", 
            "target": "_blank",
        })       
        self.assertEqual(node.__repr__(), "HTMLNode(p, the text inside a para, children: None, {'href': 'https://www.google.com', 'target': '_blank'})")
    
    def test_LeafNode_repr(self):
        node = LeafNode( "p", "This is the Text")
        self.assertEqual(
            node.__repr__(), "LeafNode(p, This is the Text, None)"
        )

    def test_LeafNode(self):
        node = LeafNode( "p", "This is the Text")
        node1 = LeafNode( "p", "This is the Text")
        self.assertEqual(
            node.__repr__(), node1.__repr__()
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_ParentNode(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_ParentNode_props(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],{
                "href": "https://www.google.com", 
                "target": "_blank",
            })
        self.assertEqual(node.to_html(),'<p href="https://www.google.com" target="_blank"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
