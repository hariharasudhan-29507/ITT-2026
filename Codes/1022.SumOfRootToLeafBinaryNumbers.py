class Solution:
    def __init__(self):
        self.val = 0

    def method(self, root, path):
        if not root:
            return

        path.append(str(root.val))

        if not root.left and not root.right:
            self.val += int("".join(path), 2)
        else:
            self.method(root.left, path)
            self.method(root.right, path)

        path.pop()  

    def sumRootToLeaf(self, root):
        self.method(root, [])
        return self.val