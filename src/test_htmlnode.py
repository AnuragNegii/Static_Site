import unittest

from htmlnode import HTMLNode

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
 

if __name__ == "__main__":
    unittest.main()
