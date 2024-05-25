from textnode import TextNode
from leafnode import LeafNode


def main():
    text_node = TextNode("Hello World", "bold", "https://leonardocunha.com/")
    print(text_node)


def text_node_to_html_node(text_node):
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

    if text_node.text_type == text_type_text:
        return LeafNode(text_node.text)
    elif text_node.text_type == text_type_bold:
        return LeafNode(text_node.text, 'b')
    elif text_node.text_type == text_type_italic:
        return LeafNode(text_node.text, 'i')
    elif text_node.text_type == text_type_code:
        return LeafNode(text_node.text, 'code')
    elif text_node.text_type == text_type_link:
        return LeafNode(text_node.text, 'a', f'href={text_node.url}')
    elif text_node.text_type == text_type_image:
        return LeafNode('', 'img', [f'src={text_node.url}', "alt=''"])
    else:
        raise Exception('Invalid TextNode type')


main()
