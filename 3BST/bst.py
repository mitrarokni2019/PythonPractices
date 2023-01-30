""" bst.py

Mitra Rokni
mitra.rokni.0545@student.uu.se
Reviewed by: Kieran 
Date reviewed:18/05/2022
"""


from linked_list import LinkedList
import random
#from sklearn import tree

class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root
    
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r
    
    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)
    
    
    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)
    
#####################################################################################################################################
#   Methods to be completed
#####################################################################################################################################
    ######################### Exercise 12  ################################# NOT WORKING
    #insert method without using recursion.                         #1 *Optional*
    ''' 
    def insert(self, key):
        if self.root is None:
            return self.Node(key)
        
        n = self.root
        while n :
            if key < n.key:
                n = n.left
            else:
                n = n.right
        
        if key <= n.key:
            n.key.left= self.Node(key)
        else :
            n.key.right= self.Node(key)
    '''        
    ######################### Exercise 13  ################################# NOT WORKING
    #contains method with recursion instead of iteration.           #2 *Optional* 
    ''' 
    def containe(self,k):
        self._containe(self.root,k)

    def _containe(self, k,r ):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

        pass
    '''    
    ######################### Exercise 14  ################################# DONE
    def height(self):                                               #3 *Compulsory*                       
        return self._height(self.root)
        
    def _height(self,r):
        if r is None:
            return 0
        else:
            return 1+  max(self._height(r.left), self._height(r.right))

    ######################### Exercise 15  ################################# DONE
    def remove(self, key):                                          #4 *Compulsory*
        self.root = self._remove(self.root, key)

    def _remove(self, r, key):                      
        if r is None:
            return None
        elif key < r.key:
            r.left = self._remove(r.left,key)
            # r.left = left subtree with k removed
        elif key> r.key:
            r.right= self._remove(r.right,key)
            # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                x=r.right
                r= None
                return x
            elif r.right is None:  # Also easy case
                x= r.left
                r= None
                return x
            # This is the tricky case.
            x= self.next_value(r.right)               # Find the smallest key in the right subtree
            r.key= x.key                              # Put that key in this node
            r.right=self._remove(r.right, x.key)      # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above
    
    def next_value(self,r):
        x=r
        while not (x.left is None):
            x= x.left
        return x
    ######################### Exercise 16  ################################# DONE
    def __str__(self):                                              #5 *Compulsory*                     
        return "<" + self._to_str(self.root)[1:].strip() + ">"


    def _to_str(self, r):
        if r is None:
            return ""
        return self._to_str(r.left) + ", " + str(r.key) + self._to_str(r.right)

    ######################### Exercise 17  ################################# DONE
    def to_list(self):                                              #6 *Compulsory*
        return self._to_list(self.root)

                  
    def _to_list(self, r):                         
        if r is None:
            return []
        return self._to_list(r.left) + [r.key] + self._to_list(r.right)
    ######################### Exercise 18  ################################# DONE
    
    def to_LinkedList(self):                                        # 7 *Compulsory*  
        lst = LinkedList()
        for data in self:
            lst.insert(data)
        return lst
    
    '''
    string = ""                                                     #7 *Compulsory*
    def to_LinkedList(self):                      
        self._to_LinkedList(self.root)
        self.convert_str(self.root)
        return "(" + BST.string[1:].strip() + ")"


    def convert_str(self, r):
        if r:
            self.convert_str(r.left)
            BST.string += (", " + str(r.key))
            self.convert_str(r.right)
    
    def _to_LinkedList(self, r):
        if (r is None) | ((r.left is None) & (r.right is None)):
            return
        if not (r.left is None):
            self._to_LinkedList(r.left)
            x = r.right
            r.right = r.left
            r.left = None
            y = r.right
            while not (y.right is None):
                y = y.right
            y.right = x
        self._to_LinkedList(r.right)
    '''
    ######################### Exercise 19  ################################# ?
    def ipl(self):                                                  #8 *Compulsory*
        ipl_value = 0
        ipl_value = self._ipl(self.root, 0)
        return ipl_value

    def _ipl(self, r, level):
        if r is None:
            return level
        print("level", level) 
        left= self._ipl(r.left, level + 1)
        print("l*",left, r.left,level)
        right = self._ipl(r.right, level + 1)
        print("r*",right,r.right,level)
        result= left+right-1
        return result
    ######################### Exercise 20  ################################# 
    def random_tree(n):                                             #9  *Useful*
        f = BST()
        for i in range(n):
            f.insert(random.random())
        return f

    ######################### Exercise 21  ################################# 
    #                                                               #10  *Useful*
    """
    What is the generator good for?
    1. computing size?     answer: YES. 
    2. computing height?   answer: NO.
    3. contains?           answer: YES. 
    4. insert?             answer: NO.
    5. remove?             answer: NO.

    """
#############################   FINISH     #################################

def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print("****")
    print( t.ipl())
    print("****")

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")

    print("******************TO_LINKEDLIST*****************")
    bst = BST()
    for x in [5, 3, 8, 1, 4, 6, 9, 2, 7]:
        bst.insert(x)
    print(bst.to_LinkedList())

    print("******************IPL**************************")
    bst = BST()
    for x in [5, 3, 8, 1, 4, 6, 9, 2, 7]:
        bst.insert(x)
    print(bst.ipl())

    print("********************random_tree*************************")
    #t = random_tree(131310)
    #print(t.height())
    #print(t.ipl()/t.size())
    
    #################################################################################




if __name__ == "__main__":
    main()


"""
==============================
Results for ipl of random trees
===============================
"""
