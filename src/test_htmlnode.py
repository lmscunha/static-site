import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("button", "Click",  props={"type": "button"})
        self.assertEqual(node.props_to_html(), ' type="button"')

    # def test_is_none(self):
    #     node = TextNode("This is a text node", "bold")
    #     self.assertIsNone(node.url)
    #
    # def test_not_equal(self):
    #     node = TextNode("This is a text node", "bold")
    #     node2 = TextNode("This is a text node different", "bold")
    #     self.assertNotEqual(node, node2)

    if __name__ == "__main__":
        unittest.main()
