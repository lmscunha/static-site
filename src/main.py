from textnode import TextNode


def main():
    text_node = TextNode("foo", "NORMAL", "www.test.com")
    print(text_node.__repr__())


main()
