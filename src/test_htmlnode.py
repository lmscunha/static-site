import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_button(self):
        node = HTMLNode("button", "Click", [HTMLNode(
            "p", "Test text")], props={"type": "button"})
        self.assertEqual(node.props_to_html(), ' type="button"')

    def test_eq_a(self):
        node = HTMLNode("a", "Website", props={"href": "https://website.com"})
        self.assertEqual(node.props_to_html(), ' href="https://website.com"')

    def test_eq_canvas(self):
        node = HTMLNode("canvas", "Alternative text", props={
                        "width": "120", "height": "80"})
        self.assertEqual(node.props_to_html(), ' width="120" height="80"')

    def test_is_none(self):
        node = HTMLNode("a", "Website", props={"href": "https://website.com"})
        self.assertIsNone(node.children)

    def test_not_equal(self):
        node = HTMLNode("a", "Website", props={"href": "https://website.com"})
        node2 = HTMLNode("button", "Click",  props={"type": "button"})
        self.assertNotEqual(node, node2)

    if __name__ == "__main__":
        unittest.main()
