import unittest

from html import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.node = HTMLNode(
            tag="div", value="Hello, World!", children=[], props={"class": "container"}
        )

    def test_initialization(self):
        self.assertEqual(self.node.tag, "div")
        self.assertEqual(self.node.value, "Hello, World!")
        self.assertEqual(self.node.children, [])
        self.assertEqual(self.node.props, {"class": "container"})

    def test_props_to_html(self):
        expected_props = ' class="container"'
        self.assertEqual(self.node.props_to_html(), expected_props)

    def test_repr(self):
        expected_repr = "HTMLNode (tag = div, value = Hello, World!, children = [], props = {'class': 'container'})"
        self.assertEqual(repr(self.node), expected_repr)


if __name__ == "__main__":
    unittest.main()
