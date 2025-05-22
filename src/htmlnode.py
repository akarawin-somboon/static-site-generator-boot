from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if not self.props:
            return ""
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("tag missing")
        if self.children is None:
            raise ValueError("children missing")

        children_html = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}>{children_html}</{self.tag}>"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.text:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.bold:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.italic:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.code:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.link:
        return LeafNode("a", text_node.text, {"href":text_node.url})
    elif text_node.text_type == TextType.image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("Invalid types")
