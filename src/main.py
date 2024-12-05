from textnode import TextNode, TextType

def main():
    text = TextNode("This is my Text", TextType.BOLD, "hooho.com")
    print(text)

if __name__ == "__main__":
    main()
