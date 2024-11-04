import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_by_type(self):
        node = TextNode("This is a text node", TextType.LINKS)
        node2 = TextNode("This is a text node", TextType.IMAGES)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("foo", TextType.NORMAL, "www.test.com")
        self.assertEqual(
            node.__repr__(), "TextNode(foo, normal, www.test.com)")

    def test_repr_no_url(self):
        node = TextNode("foo", TextType.ITALIC)
        self.assertEqual(
            node.__repr__(), "TextNode(foo, italic, None)")

        if __name__ == "__main__":
            unittest.main()
