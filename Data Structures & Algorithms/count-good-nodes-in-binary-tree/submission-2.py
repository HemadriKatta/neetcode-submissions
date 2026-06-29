# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        q.append((root,-float('inf')))
        res = 0
        while q:
            for i in range(len(q)):
                node, maxVal = q.popleft()
                if node:
                    if node.val >= maxVal:
                        res += 1
                    q.append((node.left,max(maxVal, node.val)))
                    q.append((node.right,max(maxVal, node.val)))
        return res








        