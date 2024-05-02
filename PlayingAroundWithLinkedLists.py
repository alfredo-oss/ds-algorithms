from LinkedList.Creation import LinkedList

# Create an empty linked list
my_list = LinkedList()

# Insert nodes at the tail
my_list.insertTail(1)
my_list.insertTail(2)
my_list.insertTail(3)

# Get the values of the linked list
values = my_list.getValues()
print(values)
