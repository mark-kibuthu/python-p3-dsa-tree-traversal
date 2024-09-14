class Tree:
    def __init__(self, node):
        # Initialize the tree with the values from the given dictionary node
        self.tag_name = node.get('tag_name')
        self.id = node.get('id')
        self.text_content = node.get('text_content')
        self.children = [Tree(child) for child in node.get('children', [])]

    def get_element_by_id(self, target_id):
        # Check if the current node's id matches the target id
        if self.id == target_id:
            return {
                'tag_name': self.tag_name,
                'id': self.id,
                'text_content': self.text_content,
                'children': [child.get_element_by_id(None) for child in self.children if child]
            }

        # Recursively check the children
        for child in self.children:
            result = child.get_element_by_id(target_id)
            if result:
                return result
        return None
