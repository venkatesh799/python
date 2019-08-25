# Venkatesh Thirunagiri
# ------ SINGLE lINKED lIST -------------

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new=Node(data)
        if self.head == None:
            self.head=new
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new
    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end="-->")
                n=n.next
    def length(self):
        if self.head is None:
            return 0
        else:
            n=self.head
            count=0
            while n is not None:
                count+=1
                n=n.next
            return count
    def insert_at_begining(self,data):
        new = Node(data)
        new.next=self.head
        self.head=new
    def insert_at_specified(self,data,index):
        new=Node(data)
        if index == 1:
            self.insert_at_begining(data)
        elif index > self.length():
            print("Index Out Of Bounds")
        else:
            i=1
            k=self.length()
            n=self.head
            while i < k-1:
                n=n.next
            new.next=n.next
            n.next=new
        
                
l=LinkedList()
l.insert("C")
l.insert_at_begining("PYTHON")
l.insert_at_specified("AI",2)
l.display()
print("\nlength is :",l.length())

# OUTPUT:  PYTHON-->AI-->C-->
#          length is : 3
