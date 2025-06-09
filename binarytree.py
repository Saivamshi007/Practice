from collections import deque
class TreeNode():
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


class BinaryTree():
    def __init__(self):
        self.root = None
    def insert(self,val):
        newNode = TreeNode(val)
        if not self.root:
            self.root = newNode
            return
        curr = self.root
        while True:
            if val<curr.val:
                if curr.left is None:
                    curr.left = newNode
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = newNode
                    return
                curr = curr.right

    def recursive_insert(self,val):
        self.root = _recursive_insert(self.root,val)

    def _recursive_insert(self,node,val):
        if not node:
            return TreeNode(val)
        if node.val<val:
            node.left = self._recursive_insert(node.left,val)
        else:
            node.right = self._recursive_insert(node.right,val)


    #tree traversal
    def inorder(self):
        self._inorder_(self.root)
        print()

    def _inorder_(self,node):
        if not node:
            return
        self._inorder_(node.left)
        print(node.val,end=" ")
        self._inorder_(node.right)
        print()
    def preorder(self):
        self._preorder_(self.root)
        print()
    def _preorder_(self,node):
        if not node:
            return
        print(node.val,end=" ")
        self._preorder_(node.left)
        self._preorder_(node.right)
    
    def post_order(self):
        self._post_order(self.root)
        print()

    def _post_order(self,node):
        if not node:
            return
        self._post_order(node.left)
        self._post_order(node.right)
        print(node.val,end=' ')
    
    def nonrec_postorder(self):
        curr = self.root
        stack = []
        last_visited = False

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                peak_node = stack[-1]

                if peak_node.right and last_visited!=peak_node.right:
                    curr = peak_node.right
                else:
                    print(peak_node.val,end=" ")
                    last_visited = stack.pop()
        print()
    def nonrec_preorder(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.val,end = " ")
            
            if node.left:
                stack.append(node.letf)
            if node.right:
                stack.append(node.right)

        
            





    def nonrec_indorder(self):
        curr = self.root
        stack =[]
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            print(curr.val,end=" ")
            curr = curr.right
        print()
    
    def bfs(self):
        queue = deque()
        queue.append(self.root)
        count = 0
        while queue:
            node = queue.popleft()
            print(node.val,end="->")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def tree_height(self):
        queue = deque()
        queue.append(self.root)
        height = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node  = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            height+=1
        return height 
    def max_sum(self):
        queue = deque()
        queue.append(self.root)

        max_sum = 0
        while queue:
            level_size = len(queue)
            temp_sum = 0
            for _ in range(level_size):
                
                node = queue.popleft()
                temp_sum = temp_sum+node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(temp_sum)
            max_sum = max(max_sum,temp_sum)   
        return max_sum       
        




              




                

tree = BinaryTree()
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(3)
tree.insert(1)
tree.insert(7)
tree.insert(8)
# tree.inorder()
# tree.nonrec_indorder()
print("Pre order")
# tree.preorder()
# tree.post_order()
print("Non recursive post order")
# tree.nonrec_postorder()
tree.bfs()
# tree.preorder()
print("Height of the tree: ",tree.tree_height())

print("Max sum: ",tree.max_sum())
