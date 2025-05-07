from textnode import TextNode


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(repr(node))


if __name__ == "__main__":
    main()
