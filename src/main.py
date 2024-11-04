from textnode import TextNode, TextType


def main():
    text_node = TextNode("foo", TextType.NORMAL, "www.test.com")
    print(text_node.__repr__())


main()
