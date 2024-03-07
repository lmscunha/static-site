class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_t_node):
        return (self.text == other_t_node.text) and \
            self.text_type == other_t_node.text_type and \
            self.url == other_t_node.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
