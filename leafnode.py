from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None,  props=None):
        super().__init__(tag, value, props=props)
        self.value = value
        self.tag = tag
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"{self.value}"
