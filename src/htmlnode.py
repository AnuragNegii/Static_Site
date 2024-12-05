


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
