import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "this is a paragraph")
        self.assertEqual(
            node.__repr__(),
            'HTMLNode(p, this is a paragraph, None, None)')

    def test_repr_with_prop(self):
        node = HTMLNode("a", None, None, {"href": "wwww.test.com"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(a, None, None, {'href': 'wwww.test.com'})")

    def test_props_to_html(self):
        node = HTMLNode("a", None, None, {"href": "wwww.test.com"})
        self.assertEqual(node.props_to_html(), ' href="wwww.test.com"')

    def test_props_to_html_more_then_one_props(self):
        node = HTMLNode("a", None, None, {
                        "href": "wwww.test.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(),
                         ' href="wwww.test.com" target="_blank"')

        if __name__ == "__main__":
            unittest.main()
