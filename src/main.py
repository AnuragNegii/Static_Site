from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

def main():
    list_ofsm = []
    delimiter = "'"
    text = "this 'is 'the' text"
    splitter = text.split(delimiter)
    if len(splitter) % 2 == 0:
        raise Exception("This is an error")
    for i in range(len(splitter)):
        if i%2 != 0:
            list_ofsm.append("text_type")            
        else:
            list_ofsm.append("text")            
    print(splitter)
    print(list_ofsm)

if __name__ == "__main__":
    main()
