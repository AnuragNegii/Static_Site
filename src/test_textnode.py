import unittest

from textnode import TextType, TextNode


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
        
         
if __name__ == "main" :
    unittest.main()