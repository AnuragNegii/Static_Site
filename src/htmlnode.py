


class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method Not implemented")

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        html = ""
        for k,v in self.props.items():
            html +=f' {k.replace('"','')}="{v}"'
        return html 
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            return ValueError("All leafNode must have values")
        if not self.tag:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return  f"LeafNode({self.tag}, {self.value}, {self.props})" 

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError("ALl ParentNode must have tags")
        if not self.children:
            raise ValueError("ALl ParentNode must have Children")
        children_text = ""
        for child in self.children:
            children_text += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_text}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
