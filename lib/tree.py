class Tree:
    def __init__(self, structure):
        self.structure = structure

    def get_element_by_id(self, element_id):
        return self._find_element(self.structure, element_id)

    def _find_element(self, node, element_id):
        # Check if the current node matches the ID
        if node.get('id') == element_id:
            return node

        # If the node has children, search in them
        for child in node.get('children', []):
            found = self._find_element(child, element_id)
            if found:
                return found

        return None


# Example test usage
class TestStack:
    def test_get_element_by_id(self):
        tree = Tree(
            {
                'tag_name': 'body',
                'id': None,
                'children': [
                    {
                        'tag_name': 'div',
                        'id': 'main',
                        'children': [
                            {
                                'tag_name': 'h1',
                                'id': 'heading',
                                'text_content': 'Title',
                                'children': []
                            },
                            {
                                'tag_name': 'h2',
                                'id': None,
                                'text_content': 'Subtitle',
                                'children': []
                            }
                        ]
                    }
                ]
            }
        )

        assert tree.get_element_by_id('heading') == {
            'tag_name': 'h1',
            'id': 'heading',
            'text_content': 'Title',
            'children': []
        }

        assert tree.get_element_by_id('nope') is None


# Run the test
test_stack = TestStack()
test_stack.test_get_element_by_id()
