class node:
    def __init__(self,data) -> None:
        self.data = data
        self.next=None
"""

L1=node(5)
L2=node(6)

L1.next = L2

cur =L1
while cur:
    print(cur.data ,end=" -> ")
    cur=cur.next


"""

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_node(self,data):
        new_node=node(data)
        if self.head ==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head = new_node
    def insert_node_at_pos(self,data,target):
        new_node=node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur=self.head
            prev=None
            pos=0
            while cur and pos < target:
                prev=cur
                cur=cur.next
                pos +=1
            prev.next=new_node
            new_node.next=cur
    def insert_node_at_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=new_node
    def update_node(self,data,target):
        new_node=node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur=self.head
            prev=0
            pos=0
            while cur and pos<target-1:
                prev=cur
                cur=cur.next
                pos+=1
            prev.next=new_node
            new_node.next=cur.next
    def remove_first(self):
        if not self.head:
            return
        else:
            self.head=self.head.next
    def remove_last(self):
        if not self.head:
            return
        else:
            cur=self.head
            while cur.next.next is not None:
                cur=cur.next
            cur.next=None
    
    def remove_index(self,index):
        if not self.head:
            return
        else:
            pos=0
            cur=self.head
            prev=0
            while cur is not None and pos <index-1:
                pos+=1
                prev=cur
                cur=cur.next
            prev.next=cur.next
    def remove_data(self,target):
        if not self.head:
            return
        else:
            cur=self.head
            prev=0
            while cur and cur.data != target:
                prev=cur
                cur=cur.next
            prev.next=cur.next
    def find_length(self):
        if not self.head:
            print("0")
            return
        else:
            cur=self.head
            length=0
            while cur:
                length+=1
                cur=cur.next
            print(length)
    def print_ll(self):
        if not self.head:
            print("empty")
        else:
            cur=self.head
            while cur:
                print(cur.data, end="->")
                cur=cur.next
            print()
            return
                
                
        
                
            
            
        

my_list = LinkedList()

# Insert nodes at the beginning
my_list.insert_node(5)
my_list.insert_node(6)
my_list.insert_node(7)



linked_list = LinkedList()
linked_list.insert_node(1)
linked_list.insert_node(2)
linked_list.insert_node(3)
linked_list.insert_node(4)
linked_list.insert_node(5)
linked_list.insert_node_at_pos(6,1)
linked_list.insert_node_at_end(10)
linked_list.update_node(7,2)
linked_list.remove_last()
linked_list.remove_first()
linked_list.remove_index(2)
linked_list.remove_data(2)
linked_list.find_length()
linked_list.print_ll()

cur=linked_list.head
prev=my_list.head



while cur is not None:
    print(cur.data ,end="->")
    cur=cur.next
