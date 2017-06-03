Solution 1 : Given by hackerrank

def check(root, min_, max_):
    return (root is None or 
            (root.data < max_ and root.data > min_ and 
             check(root.left, min_, root.data) and 
             check(root.right, root.data, max_)))

def check_binary_search_tree_(root):
    return check(root, -float('inf'), float('inf'))
	
	
	
	
Solution 2 : Solved by me

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

# http://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

def isBinarySearchTree(root):
    global arr
    arr = []
    a=[]
    
    def printInorder(root):
        global arr
        if root:

            # First recur on left child
            printInorder(root.left)

            # then print the data of node
            arr.append(root.data)

            # now recur on right child
            printInorder(root.right)
            
            return arr
            
    a = printInorder(root)
#print a

# 
#### CHECK IF THE ARRAY IS SORTED:

#if size of array is zero or one, return true.
# Check last two elements of array, 
#if they are sorted, perform a recursive call with n-1
#    else, return false.
#If all the elements will be found sorted, n will eventually fall to one, satisfying Step 1.

    def check_sorted_array(array) :
        l = len(array)
        if l == 1 or l == 0 :
            return True
        if array[l-1] > array[l-2] :
            del array[-1]
            #print array
            return check_sorted_array(array)
            
        else :
            return False
            
    return check_sorted_array(a) 
                                  