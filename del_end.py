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
n1=Node("Nira")
n2=Node("My name is billa")
n3=Node("Mangatha da")
n4=Node("king of the sea")
n5=Node("neeyum naanum anbe")
n6=Node("see you again")
n7=Node("Va asura vaa")
n8=Node("vaadi pulla vaadi")
n9=Node("Manamaganin Sathiyam")
n10=Node("unnodu sernthu")
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
n7.next=n8
n8.next=n9
n9.next=n10
print("Orginal Linked List")
head=n1
display(head)

print("\n Deletion at the End")
temp=head
while temp.next.next:
    temp=temp.next
temp.next=None
display(head)
