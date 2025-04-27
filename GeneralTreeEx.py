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
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.data = f"{name} ({designation})"
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
    '''
    def print_tree(self,tree_type):
        if tree_type =="name":
            p_data = self.name
        elif tree_type == "designation":
            p_data = self.designation
        elif tree_type == "both":
            p_data = self.data
        spaces = " " * (self.get_level() * 3)
        prefix = spaces + "|__" if self.parent else ""
        print(f"{prefix}{p_data}")
        if self.children:
            for child in self.children:
                child.print_tree(tree_type)
    '''
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
     root = TreeNode()

def build_management_tree():
    root = TreeNode("Nilipul", "CEO")

    cto = root.add_child(TreeNode("Chinmay", "CTO"))
    hr = root.add_child(TreeNode("Gels", "HR Head"))

    ih = cto.add_child(TreeNode("Vishwa", "Infrastructure Head"))
    ah = cto.add_child(TreeNode("Aamir", "Application Head"))

    cm = ih.add_child(TreeNode("Dhaval", "Cloud Manager"))
    am = ih.add_child(TreeNode("Abhijit", "Application Manager"))

    rm = hr.add_child(TreeNode("Peter", "Recruitment Manager"))
    pm = hr.add_child(TreeNode("Waqas", "Policy Manager"))

    return root
    
if __name__ == "__main__":
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy

