'''
#######################EXCERCISE 1########################
Create a Tree so that it takes name and designation in data part of TreeNode class. 
Now extend print_tree function such that it can print either name tree, designation tree 
or name and designation tree both.
'''
'''
#######################EXCERCISE 2########################
modify print_tree method to take tree level as input. And that should print tree only upto that level
'''

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
    
    def print_tree(self, level=None):
        l = 0
        spaces = " " * (self.get_level() * 3)
        prefix = spaces + "|__" if self.parent else ""
        if level is None or self.get_level() <= level:
            print(f"{prefix}{self.data}")
        if self.children:
            for child in self.children:
                if l == level:
                    break
                child.print_tree(level)

def build_location_tree():
    root = TreeNode("Global")

    ind = root.add_child(TreeNode("India"))
    usa = root.add_child(TreeNode("USA"))

    guj = ind.add_child(TreeNode("Gujarat"))
    kar = ind.add_child(TreeNode("Karnataka"))

    ahm = guj.add_child(TreeNode("Ahmedabad"))
    bar = guj.add_child(TreeNode("Baroda"))
    ban = kar.add_child(TreeNode("Bangalore"))
    mys = kar.add_child(TreeNode("Mysore"))

    nj = usa.add_child(TreeNode("New Jersey"))
    cal = usa.add_child(TreeNode("California"))

    pre = nj.add_child(TreeNode("Princeton"))
    tre = nj.add_child(TreeNode("Trenton"))
    sf = cal.add_child(TreeNode("San Francisco"))
    mv = cal.add_child(TreeNode("Mountain View"))
    pa = cal.add_child(TreeNode("Palo Alto"))

    return root


if __name__ == "__main__":

    root = build_location_tree()
    root.print_tree(1)
    root.print_tree(2)
    root.print_tree(3)