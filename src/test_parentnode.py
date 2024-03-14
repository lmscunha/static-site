import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_eq_to_html_tag(self):
        node = ParentNode([
            LeafNode("Bold text", "b",),
            LeafNode("Normal text", None,),
            LeafNode("italic text", "i",),
            LeafNode("Normal text", None),
        ], "p")
        self.assertEqual(node.to_html(
        ), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    if __name__ == "__main__":
        unittest.main()
