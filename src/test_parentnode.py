import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_eq_to_children_to_html(self):
        node = ParentNode([
            LeafNode("Bold text", "b",),
            LeafNode("Normal text", None,),
            LeafNode("italic text", "i",),
            LeafNode("Normal text", None),
        ], "p")
        self.assertEqual(node.to_html(
        ), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_eq_to_children_to_html_nested(self):
        node = ParentNode([ParentNode([
            LeafNode("Bold text", "b",),
            LeafNode("Normal text", None,),
            LeafNode("italic text", "i",),
            LeafNode("Normal text", None),
        ], "p")], "div")
        self.assertEqual(node.to_html(
        ), '<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>')

    def test_eq_to_children_to_html_nested_children(self):
        node = ParentNode([ParentNode([
            LeafNode("Bold text", "b",),
            ParentNode([
                LeafNode("Text Inside Parent", None,)
            ], "p"),
            LeafNode("Normal text", None,),
            LeafNode("italic text", "i",),
            LeafNode("Normal text", None),
        ], "p")], "div")
        self.assertEqual(node.to_html(
        ), '<div><p><b>Bold text</b><p>Text Inside Parent</p>Normal text<i>italic text</i>Normal text</p></div>')

    if __name__ == "__main__":
        unittest.main()
