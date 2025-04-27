class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        return child
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    
    def print_tree(self):
        spaces = " " * (self.get_level() * 3)
        prefix = spaces + "|__" if self.parent else ""
        print(f"{prefix}{self.data}")
        if self.children:
            for child in self.children:
                child.print_tree()

def build_electronics_tree():
    root = TreeNode("Electronics")

    tv = root.add_child(TreeNode("TV"))
    cp = root.add_child(TreeNode("Cell Phone"))
    lp = root.add_child(TreeNode("Laptop"))
    
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Samsung"))

    cp.add_child(TreeNode("Nokia"))
    cp.add_child(TreeNode("Apple"))
    cp.add_child(TreeNode("Pixel"))

    lp.add_child(TreeNode("Dell"))
    lp.add_child(TreeNode("HP"))
    lp.add_child(TreeNode("Lenovo"))
    
    return root
    
if __name__ == "__main__":
    root = build_electronics_tree()
    root.print_tree()