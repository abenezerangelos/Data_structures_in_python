###################################################################################
# Title: Circular Doubly Linked List Implementation
# Author: Srini Badri
# Version: 1.0
# Description: A simple program to implement and test Circular Doubly Linked List
# implementation
###################################################################################

# Node class definition
class Node:
    def __init__(self, value=0):
        '''
        Define and initialize data attributes
        '''
        self.data = value
        self.next = None
        self.prev = None

    def __str__(self):
        '''
        Return string representation of Node's data
        '''
        return str(self.data)

# Circular Doubly Linked List (DLL) class definition
class CDLL:
    def __init__(self):
        '''
        Creates a new circular doubly linked list that is empty.
        '''
        self.head = None
        self.length = 0

    def __str__(self):
        '''
        Creates and returns a string representation of the circular doubly linked list.
        '''
        if self.head is None:
            list_str = "None"
        else:
            curr_node = self.head
            list_str = " <-> " + str(curr_node.data)
            while (curr_node.next is not self.head):
                curr_node = curr_node.next
                list_str += " <-> " + str(curr_node.data)
            list_str += " <-> "

        return list_str

    def add(self, item):
        '''
        Adds a new item to the circular doubly linked list.
        '''
        temp_node = Node(item)
        if (self.head is None):
            self.head = temp_node
            self.head.prev = self.head
            self.head.next = self.head
        else:
            self.head.prev.next = temp_node
            temp_node.prev = self.head.prev
            self.head.prev = temp_node
            temp_node.next = self.head
            self.head = temp_node
        self.length += 1

    def append(self, item):
        '''
        Adds a new item to the end of the circular doubly linked list making it the last item in the list.
        '''
        # To Be Implemented.
        # return statement is used below to avoid indentation errors
        temp_node = Node(item)
        if (self.head is None):
            self.head=temp_node
            self.head.prev=self.head
            self.head.next = self.head
        else:
            self.head.prev.next = temp_node
            temp_node.prev = self.head.prev
            self.head.prev = temp_node
            temp_node.next = self.head
        self.length+=1

    def insert(self, index, item):
        '''
        Adds a new item to the circular doubly linked list at position index.
        '''
        temp_node=Node(item)
        cur_node=self.head
        counter=1
        if index==0:
            self.add(item)

        else:
            while counter<index:
                cur_node=cur_node.next
                counter+=1
            if cur_node.next==self.head:
                self.append(item)
            else:
                temp_node.next=cur_node.next
                cur_node.next.prev=temp_node
                cur_node.next=temp_node
                temp_node.prev=cur_node
                self.length += 1







        # To Be Implemented.
        # return statement is used below to avoid indentation errors

    def pop(self, index = None):
        '''
        Removes and returns the item at position index.
        If index is not specified, removes and returns the last item in the list.
        If the index is out of range, it does not update the list.
        '''
        # To Be Implemented.
        # return statement is used below to avoid indentation errors

        cur_node=self.head
        counter=0


        if index == None or index==self.size()-1:
            #this will stop right before our last node (i.e., before the cycle starts again)
            if self.size()==1:
                popped_value=self.head
                self.head=None
                self.length-=1
                return popped_value
            else:
                while cur_node.next != self.head:
                    cur_node=cur_node.next
                cur_node.prev.next=self.head
                self.head.prev=cur_node.prev

                self.length-=1
                return cur_node
        elif index==0:
            if self.size()==1:
                popped_value=self.head
                self.head=None

                self.length-=1
                return popped_value

            else:
                self.head.prev.next=self.head.next
                self.head.next.prev=self.head.prev
                self.head=self.head.next
                self.length-=1
                return self.head

        elif index>0:
            while counter<index:
                cur_node=cur_node.next
                counter+=1
            cur_node.next.prev=cur_node.prev
            cur_node.prev.next=cur_node.next
            self.length-=1
            return cur_node

        if index >= self.size():
            return IndexError("The index provided is out of range")














    def remove(self, item):
        '''
        Removes the item from the list.
        The method does not update the list if the item is not present in the list
        '''
        if (self.head is None):
            print("DLL is empty.")
            return None

        curr_node = self.head
        prev_node = self.head.prev
        next_node = self.head.next
        found = False
        i = 0

        while (i < self.length) and not found:
            if curr_node.data == item:
                found = True
            else:
                prev_node = curr_node
                curr_node = next_node
                next_node = next_node.next
            i += 1

        if found:
            if curr_node is self.head:
                if next_node is not self.head:
                    next_node.prev = self.head.prev
                    self.head.prev.next = next_node
                    curr_node.prev = None
                    curr_node.next = None
                    self.head = next_node
                else:
                    self.head = None
            elif curr_node is self.head.prev:
                if (prev_node is not self.head):
                    prev_node.next = self.head
                    self.head.prev = prev_node
                    curr_node.prev = None
                    curr_node.next = None
                else:
                    self.head.prev = self.head
                    self.head.next = self.head
            else:
                prev_node.next = curr_node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                curr_node.prev = None
                curr_node.next = None
            self.length -= 1

        return found

    def search(self, item):
        '''
        Searches for the item in the list. It needs the item and returns the index of the item (-1 if not found).
        '''
        # To Be Implemented.
        # return statement is used below to avoid indentation errors
        cur_node = self.head
        counter=0

        if self.length==0:
            return IndexError("The linked list is empty and so therefore one cannot search for items")
        else:
            for i in range(self.length):
                if cur_node.data==item:
                    return counter
                cur_node=cur_node.next
                counter+=1




        return -1


    def __getitem__(self, index):
        '''
        Retrieves and returns the data element at a given position index of the circular doubly linked list using indexing.
        '''
        # To Be Implemented.
        # return statement is used below to avoid indentation errors
        counter=0
        cur_node = self.head
        while counter<index:
            cur_node=cur_node.next
            counter +=1

        return cur_node.data

    def __setitem__(self, index, item):
        '''
        Adds a new item to the circular doubly linked list using assignment operation at the given position index.
        '''
        # To Be Implemented.
        # return statement is used below to avoid indentation errors
        counter = 0
        cur_node = self.head
        while counter < index:
            cur_node = cur_node.next
            counter += 1
        cur_node.data=item


    def __delitem__(self, index):
        '''
        Deletes data from the list at the given index position
        '''
        # To Be Implemented.
        # return statement is used below to avoid indentation errors

        self.pop(index)

    def is_empty(self):
        '''
        The method checks if the list is empty and return a boolean value.
        '''
        # To Be Implemented.
        # return statement is used below to avoid indentation errors
        if self.head is not None:
            return False
        if self.head is None:
            return True



    def size(self):
        '''
        Returns the number of items in the list.
        '''
        # To Be Implemented.
        # return statement is used below to avoid indentation errors

        return self.length

    def __len__(self):
        '''
        Returns the number of items in the list. Overrides the len() function
        '''
        return self.length

    def __iter__(self):
        '''
        Returns and iterator object created by the generator method
        '''
        return self.generator()

    def generator(self):
        '''
        Creates a reference for forward iteration. Execution pauses during each loop and returns the current node data
        '''
        curr_node = self.head
        i = 0
        while (i < self.length):
            yield curr_node.data
            curr_node = curr_node.next
            i += 1

    def __reversed__(self):
        '''
        Creates an iterator object. Execution pauses during each loop and returns the current node data
        '''
        # To Be Implemented.
        # return statement is used below to avoid indentation errors
        curr_node = self.head.prev
        for i in range(self.length):
            yield curr_node.data
            curr_node=curr_node.prev



# Main method testing the circular doubly Linked List with sample data
def main():
    dll = CDLL()


    # Generate sample data and add to the circular doubly linked list
    for i in range(100, 200, 11):
        dll.add(i)
    print("circular doubly linked list after add operations:")
    print(dll,"\n",dll.length, "\n")

    for i in range(100, 200, 11):
        print("index for", i, ": ", dll.search(i))
    print("\n")

    # Remove sample data from circular doubly linked list using remove() method
    for j in range(100, 200, 11):
        dll.remove(j)
    print("circular doubly linked list after remove operations:")
    print(dll,"\n",dll.length, "\n")

    # Generate sample data and append to the circular doubly linked list
    for i in range(200, 300, 11):
        dll.append(i)
    print("circular doubly linked list after append operations:")
    print(dll,"\n",dll.length, "\n")

    # Remove and print sample data from circular doubly linked list using pop() method
    print("circular doubly linked list items removed during pop operations:")
    for j in range(0, len(dll)):
        print(dll.pop(), end = ", ")
    print("\n\ncircular doubly linked list after pop operations:")
    print(dll,"\n",dll.length, "\n")

    # Generate sample data and insert it to the circular doubly linked list
    index = 0
    for i in range(300, 400, 11):
        dll.insert(index, i)
        index += 1
    print("circular doubly linked list after insert operations:")
    print(dll,"\n",dll.length, "\n")

    # Remove and print sample data from circular doubly linked list using pop() method
    print("circular doubly linked list items removed during pop operations:")
    for j in range(0, len(dll)):
        print(dll.pop(), end = ", ")
    print("\n\ncircular doubly linked list after pop operations:")
    print(dll,"\n",dll.length, "\n")

    # Generate sample data and append to the circular doubly linked list
    for i in range(400, 500, 11):
        dll.append(i)
    print("circular doubly linked list after append operations:")
    print(dll, "\n",dll.length,"\n")

    # Get data from circular doubly linked list using indexing
    print("circular doubly linked list data elements accessed using indexing:")
    for i in range(0, len(dll)):
        print(dll[i], end=", ")
    print("\n")

    # Update date in circular doubly linked list using indexing
    i = 0
    for j in range(500, 600, 11):
        dll[i] = j
        i += 1
    print("circular doubly linked list after update operations:")
    print(dll, "\n",dll.length,"\n")

    # Delete data from circular doubly linked list using indexing
    for i in range(len(dll)-1, -1, -1):
        del(dll[i])
    print("circular doubly linked list after delete operations:")
    print(dll, "\n")

    # Check if circular doubly linked list is empty
    print("List is empty? : ", dll.is_empty(), "\n")

    # Generate sample data and append to the circular doubly linked list
    for i in range(600, 700, 11):
        dll.append(i)
    print("circular doubly linked list after append operations:")
    print(dll, "\n")

    # Get data from circular doubly linked list using an Iterator
    print("circular doubly linked list elements using iterator:")
    for data in dll:
        print("node: " + str(data), end=", ")
    print("\n")

    # Get data in reverse from circular doubly linked list using an Iterator
    print("circular doubly linked list elements in reverse using iterator:")
    for data in reversed(dll):
        print("node: " + str(data), end=", ")
    print("\n")


if __name__ == "__main__":
    main()

