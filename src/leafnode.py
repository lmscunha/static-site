from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None,  props=None):
        super().__init__()
        self.value = value
        self.tag = tag
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError('Invalid value')
        if self.tag:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"{self.value}"
    def text_node_to_html_node(self, text_node):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, \
                {self.props})"
