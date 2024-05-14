from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, children, tag=None,  props=None):
        super().__init__()
        self.children = children
        self.tag = tag
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag provided")
        if self.children is None:
            raise ValueError("Invalid children value")
        curr_html = ''
        for el in self.children:
            curr_html += el.to_html()
        return f"<{self.tag}>{curr_html}</{self.tag}>"
