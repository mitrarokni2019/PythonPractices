""" linked_list.py

Mitra Rokni
mitra.rokni.0545@student.uu.se
Reviewed by: Kieran
Date reviewed:18/5/2022
"""

from distutils.command.build_scripts import first_line_re


class LinkedList:
    
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ      
        
            
    def __init__(self):
        self.first = None

    
    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ
            
    def __in__(self, x):           # Discussed in the section on operator overloading 
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False 
        return False

    
    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)
    
    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')            
    
    ###################################################################################################################################
    #   To be implemented
    ###################################################################################################################################
    ######################### Exercise 1  ################################# DONE
    def length(self):                                        #1 Optional
        return self._length(self.first)

    def _length(self, r):
        if r is None:
            return 0
        else:
            return 1+ self._length(r.succ)
    '''
    # iterative with while-loop
    def length(self):
        if self.first is None:
            return 0 
        else:
            count=0
            f=self.first
            while f:
                count= count+1
                f=f.succ
            return count
    '''
    ######################### Exercise 2  ################################# DONE
    
    def mean(self):                                          #2 Optional
        sum =self.sum(self.first)
        n= self.length()
        return sum/n

    def sum(self, r):
        if r is None:
            return 0
        else:
            return r.data + self.sum(r.succ)

    '''
    # iterative with while-loop
    def mean(self):
        if self.first is None:
            return 0 
        else:
            sum=0
            f=self.first
            while f:
                sum= sum + f.data
                f=f.succ
            n= self.length()
            return sum/n
    '''
    ######################### Exercise 3  ################################# NOT WORKING
    # here when i tested below most of the codes work good but in test.py i got error.
    #  i realized whenwe reach the last node it et into trouble also another problem was 
    # that i did not  return the value . since it is otional i decide to skip this part and move on...
    def remove_last(self):                              #3 Optional
        if self.first is None:
            return 0 
        else:
            f= self.first
            while f.succ:
                f=f.succ
            



        pass
    
    '''
#1: my code in recursive way ==== not working            #3 Optional
    def remove_last(self):
        if self.first is None:
            return self.first
        else:
            return self._remove_last(self.first)


    def _remove_last(self, f):
        if f.succ is None:
            f= None
            return f
        else: 
            f.succ= self._remove_last(f.succ)
            return f
 
#2:  my code  for practice ==== not working                 #3 Optional
    def remove_last(self):                                   
        head = self.first
        previous_head = head
        if head.succ is not None:
            while(head.succ is not None):
                previous_head  = head
                head = head.succ
            previous_head.succ = None
        else:
            self.remove(self.first.data)

    
#3:  code in iterative way  ==== not working  ( help from a friend )   #3 Optional
    def remove_last(self):                                  
        head=0
        if self.first.succ is  None:
            return self.remove(self.first.data)
        else:
            head= self.first
            
            while(head.succ is not None):
                head = head.succ
            self.remove(head.data)  
            return head.data
    '''
    
    ######################### Exercise 4  #################################  DONE
                              
    # recursive method       Done   use this one 
    def remove(self, x):                                              #4 Compulsory
        return self._remove (self.first, x)
        
    def _remove (self,r, x):
        if r is  None or r.succ is None:
            return False
        if r.data==x:
            r= r.succ
            return True
        elif r.succ.data ==x :
            r.succ=r.succ.succ
            return True

        else:
            return self._remove(r.succ, x)
    '''    
    # Iterative way  Done
    def remove(self, x):                                    
        if (self.first.data == x):
            self.first = self.first.succ
            return True
        previous_head = self.first
        head = self.first.succ
        while head is not None:
            if (head.data == x):
                previous_head.succ = head.succ
                return True
            previous_head = head
            head = head.succ
        return False  

    ''' 
    ######################### Exercise 5  ################################# DONE
    #recursive method
    def count(self, x):                                      #5 Optional
        return self._count(self.first, x)
    
    def _count(self, r, x):
        if r is  None:
            return 0
        elif r.data ==x:
            return 1+self._count(r.succ, x)
        else:
            return self._count(r.succ, x)  
    '''
    # iterative way for practice
    def count(self,x):
        lst=[]
        head= self.first
        if self.first  is None:
            return 0
        else:
            if head.data ==x:
                head=head.succ
                return lst.append(x)
                
            else:
                while (head.succ is not None):
                
                    if head.succ.data ==x:
                        lst.append(x)
                        head=head.succ
                    else:
                        head=head.succ
                
        return lst
    
    '''
    
    ######################### Exercise 6  ################################# DONE
    def to_list(self):                                       #6 Compulsory
        list=[]
        self._to_list(self.first, list)
        return list
    
    def _to_list(self, r, list):
        if r is  None: 
            return False
        else:
            list.append(r.data)
            return self._to_list(r.succ, list)
    ######################### Exercise 7  ################################# DONE
    def remove_all(self, x):                                 #7 Compulsory
        if self.first.data ==  None:
            return False
        else:
            self.first = self._remove_all(x, self.first)
            
    def _remove_all(self, x, f):
        if f == None:
            return f

        elif f.data == x:
            f= self._remove_all(x,f.succ)
            return f 

        else:
            f.succ= self._remove_all(x, f.succ)
            return f

    ######################### Exercise 8  ################################# DONE
    def __str__(self):                                       #8 Compulsory
        return '(' + ', '.join([str(x) for x in self]) + ')'
    ######################### Exercise 9  ################################# DONE
    
    '''
    # this one does not working .Failed in test.py
    def merge(self, lst):                                    #9 Compulsory
        merged = LinkedList()
        pointer = merged.first        
        while True:
            if self.first is None:
                pointer.succ = lst.first
                break
            if lst is None:
                pointer.succ = self.first
                break
            if self.first.data <= lst.first.data:
                pointer.succ = self.first
                self.first = self.first.succ
            else:
                pointer.succ = lst.first
                lst.first = lst.first.succ
            pointer = pointer.succ
        merged.remove(-float("inf"))
        return merged
    '''
    # working and Done
    def merge(self, lst):         # Compulsory  Done
        lst2 = iter(lst)
        if lst2 is None:
            return LinkedList()
        if self.first is None:
            return self.insert(lst2)
        else:
            for key in lst2:
                self.insert(key)
    

    ######################### Exercise 10  ################################# ? 
    def __getitem__(self, ind):                              #10 Compulsory
        h = self.length()
        if ind >= h:
            raise IndexError("Index out of range.")
        current = self.first
        for x in range(ind):
            current = current.succ
        return current.data
    ######################### Exercise 11  #################################  ?
class Person:                                                #11 Compulsory to complete
    def __init__(self,name, pnr):
        self.name = name
        self.pnr = pnr
        
        
    def __str__(self):
        return f"{self.name}:{self.pnr}" 
    
 
    def __equal__(self, obj):
        return self.pnr == obj.pnr
    
    def __less__(self, obj):
        return int(self.pnr) < int(obj.pnr)

    def __less_equal__(self, obj):
        return self.__less__(obj) or self.__equal__(obj)

    



#############################   FINISH     #################################
def main():
    lst = LinkedList()
    for x in [1,2,3,4,5, 7,33]:
        lst.insert(x)
    lst.print()
    print(lst.length())
    print(lst.mean())
    print(lst.to_list())
    print(lst.__str__())
    print("count 3:",lst.count(3))
    lst.remove(3)
    print("remove 3:", lst) 
    
    print("count 5:",lst.count(5))
    
    lst.remove_all(5)
    #print("remove all 5:" , lst)
    print("count 5:",lst.count(3))
    #rint(lst)
    print("rrrrrrrrrrrrrrrrrrrrrrrrr")
    #lst.remove_last()
    print(lst)
    #lst.remove_last()
    print(lst)
    print("\nthat's it")
    
    print("*******************class person ***********************")
    person1 = Person('medi', 133)
    person2 = Person('sara', 99)
    person3= Person('mitra', 100)
    result= Person.__less__(person2,person3)
    print("out1", result)

    print("out2", Person.__str__(person1))


    
    


if __name__ == '__main__':
    main()
     


    

