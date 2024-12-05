from htmlnode import HTMLNode
from textnode import TextNode, TextType

def main():
    text = TextNode("This is my Text", TextType.BOLD, "hooho.com")
    html =  HTMLNode("p", "the text inside a para", None, {
    "href": "https://www.google.com", 
    "target": "_blank",
})       
    print(html)

if __name__ == "__main__":
    main()
