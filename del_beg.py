class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def display(head):
    temp = head
    while temp is not None:
        print(temp.data,end="->")
        temp = temp.next
    print("None")
n1 = Node(5)
n2 = Node(10)
n3 = Node(20)
n4 = Node(30)
n5 = Node(40)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
print("Orginal Linked List")
head=n1
display(head)
print("\n Deletion at beginning")
head=head.next
display(head)
