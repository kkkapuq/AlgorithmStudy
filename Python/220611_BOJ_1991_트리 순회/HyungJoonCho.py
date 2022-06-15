'''
전위 : 루트 -> 왼 -> 오
중위 : 왼 -> 루트 -> 오
후위 : 왼 -> 오 -> 루트
'''

import sys

n = int(input())
tree = {}

for _ in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]
    
# 전위, 루 왼 오
def preorder(root):
    if root != '.':
        print(root, end = '')
        preorder(tree[root][0])
        preorder(tree[root][1])

# 중위, 왼 루 오
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

# 후위, 왼 오 루
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')