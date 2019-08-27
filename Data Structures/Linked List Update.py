
# Venkatesh Thirunagiri 

#Single Linked List in Pyhton 

'''
Linked List Operations
insert()
insert_at_begining()
insert_at_last()
insert_at_specified()

delete_first()
delete_at_last()
delete_all()

length()
display()
'''

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
        print("Data inserted Sucessfully\n")
    def display(self):
        if self.head is None:
            print("List is Empty\n")
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
        k=self.length()
        if index == 1:
            self.insert_at_begining(data)
            print("Data inserted  at :",index)
        elif index == k+1:
            self.insert(data)
        elif index > k+2:
            print("\nIndex Out Of Bounds\n")
        else:
            new=Node(data)
            i=1
            n=self.head
            while i < index-1:
                n=n.next
                i+=1
            new.next=n.next
            n.next=new
            print("Data inserted   at :",index)
    def insert_at_last(self,data):
        new=Node(data)
        if self.head == None:
            print("List is Empty\n")
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new
            print("Data Inserted at Last\n")
                
    def delete_at_first(self):
        if self.head ==  None:
            print("List is Empty\n")
        else:
            n=self.head 
            self.head = n.next
            print("Deleted First Element\n")
    def delete_at_last(self):
        if self.head == None:
            print("List is Empty\n")
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None
            print("Deleted Last Element\n")
    def delete_at_specified(self,target):
        k=self.length()
        if self.head == None:
            print("List is Empty\n")
        elif target == 1:
            self.delete_at_first()
        elif target == k:
            self.delete_at_last()
        elif target > k:
            print("\nCan't Delete List has only : {0} Elements\n".format(k))
        else:
            i=1
            p=self.head
            while i < target-1:
                p=p.next
                i+=1
            q=p.next
            p.next=q.next
            q.next=None
            print("Data deleted at : {0}".format(target))
    def delete_all(self):
        if self.head == None:
            print("ooops ! List is Empty\n")
        else:
            self.head = None
            print("Linked Cleared \n")
l=LinkedList()
l.insert("A")
l.insert("B")
l.display()
l.insert_at_specified("C",1)
l.display()
l.insert_at_specified("T",11)
l.display()
l.insert_at_last("F8")
l.display()
l.insert_at_begining("V")
l.display()
l.delete_at_last()
l.display()
l.delete_at_first()
l.display()
l.delete_at_specified(l.length())
l.display()
l.delete_at_specified(10)
l.display()
l.delete_at_specified(2)
l.display()
print("Lenght is :",l.length())
l.delete_all()
l.display()

'''
OUTPUT :

Data inserted Sucessfully

Data inserted Sucessfully

A-->B-->Data inserted  at : 1

C-->A-->B-->

Index Out Of Bounds

C-->A-->B-->Data Inserted at Last

C-->A-->B-->F8-->V-->C-->A-->B-->F8-->Deleted Last Element

V-->C-->A-->B-->Deleted First Element

C-->A-->B-->Deleted Last Element

C-->A-->

Can't Delete List has only : 2 Elements

C-->A-->Deleted Last Element

C-->Lenght is : 1

Linked Cleared 

List is Empty
'''
