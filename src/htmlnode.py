class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child class should implement this")

    def props_to_html(self):
        str_prop = ''
        for key, value in self.props.items():
            str_prop += f' {key}="{value}"'
        return str_prop

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, \
                {self.props})"
