import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq_to_html_tag(self):
        node = LeafNode("Some Text", "p")
        self.assertEqual(node.to_html(), '<p>Some Text</p>')

    def test_eq_to_html_text(self):
        node = LeafNode("Some Text")
        self.assertEqual(node.to_html(), 'Some Text')

    def test_raise_Val_err(self):
        node = LeafNode(None)
        self.assertRaises(ValueError, node.to_html)

    if __name__ == "__main__":
        unittest.main()
