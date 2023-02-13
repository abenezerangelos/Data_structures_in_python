'''
Title: SinglyLinedList (In-class participation
Author: Ebenezer Abate & Srini Badri (I used the slides in class as reference)
Date: Feb,06,2023
Description: This is an implementation of the Node and LinkedList data sturctures
we learned in class last week.
This submission is a class participaiton
P.S.: I understand that I have submitted it a few hours late from the time of the deadline but it seems that I have
a 24-hour grace period, so please do not take points of for lateness.
'''



class Node:
    '''
    A class representing a node that will take a value as its argument.
    Node has attributes data and next.
    '''
    def __init__(self,data):#initializing the class with field constructors
        self.data=data
        self.next=None

    def __str__(self):#modifiying the inbuilt function print output statement
        return str(self.data)
class LinkedList:
    '''
    A class representing a linkedlist data structure, which has several methods
    LinkedList has attributes such as a head and a tail.
    '''
    def __init__(self):#initialiizing the class with field attributes
        self.head=None
        self.tail=None
        self._size=0#I have decided to rename this variable since methods and attributes cannot share the same name.
    def add(self,item):

        temp=Node(item)
        temp.next=self.head
        self.head= temp
        if self.tail is None:
            self.tail=temp
        self._size+=1
    def search(self, item):
        cur=self.head
        found=-1
        loc=0
        while cur is not None and found ==-1:
            if cur.data==item:
                found=loc
            else:
                cur=cur.next
            loc+=1
        if found>-1:
            return found
        else:
            print("item is not found, doesn't exist in this list")
            return None
    def remove(self,item):
        cur=self.head
        prev=None
        found=False
        while cur is not None and not found:
            if cur.data==item:
                found=True
            else:
                prev=cur
                cur=cur.next
        if found:
            if cur==self.head:
                self.head=cur.next
                cur.next=None
                if cur==self.tail:
                    self.tail=prev
            else:
                prev.next=cur.next
                cur.next=None
                if cur==self.tail:
                    self.tail=prev
                self._size-=1
    def size(self):
        return self._size
    def is_empty(self):
        return self.head is None
    def __str__(self):
        strlist=""
        cur=self.head
        while cur is not None:
            strlist+=str(cur.data)
            strlist+="->"
            cur=cur.next
        strlist+="None"
        return strlist
    def append(self,item):
        temp=Node(item)
        if self.tail is None:
            self.tail=temp
            self._size+=1
        else:
            cur=self.tail
            cur.next=temp
            self.tail=temp
            self._size+=1
    def insert(self,index,item):
        temp=Node(item)
        cur=self.head
        i=1
        if index==0:
            temp.next=cur
            self.head=temp
        #when index=1
        else:
            while i<index:
                cur=cur.next

                i+=1
            temp.next=cur.next
            cur.next=temp
            if index==self._size:
                self.tail=temp










    def pop(self,index):
        i=0
        prev=None
        cur=self.head
        while i<index:
            prev=cur
            cur=cur.next

            i+=1
        if cur==self.head:
            self.head=cur.next
            cur.next=None
            if cur==self.tail:
                self.tail=prev
        else:
            prev.next=cur.next
            cur.next=None
            if cur==self.tail:
                self.tail=prev
            self._size-=1

 # def remove(self,item):
 #        cur=self.head
 #        prev=None
 #        found=False
 #        while cur is not None and not found:
 #            if cur.data==item:
 #                found=True
 #            else:
 #                prev=cur
 #                cur=cur.next
 #        if found:
 #            if cur==self.head:
 #                self.head=cur.next
 #                cur.next=None
 #                if cur==self.tail:
 #                    self.tail=prev
 #            else:
 #                prev.next=cur.next
 #                cur.next=None
 #                if cur==self.tail:
 #                    self.tail=prev
 #                self.size-=1





def main():

    x=LinkedList()#construct our LinkedList object and set the object to a variable
    x.add(1)#use function add to add a node with value 1 to the left(the beginning) of the linkedlist
    x.add(2)#repeat above function with value 2
    x.add(3)#repreat above functino with value 3
    x.add(4)#repreat above functino with value 4
    x.insert(1,5)#use function insert() to add value of 5 at index 1
    #can't name the method and an attribute using the same name so attribute has changed to _size
    print( x.size())#print the size of our linked list
    x.append(5)#append a node with a value of 5 to the end of our linkedList.
    x.pop(3)#function to remove whatever is in index 3 of our LinkedList
    print(x.search(5))#print the index where the first node with a value of 5 exists
    x.remove(4)#remove the first occurrence of the node with value 4 from the linked list.
    print(x.is_empty())#print a bool telling us whether or not our LinkedList is false.
    #_str_ method
    print(x)#this is the implementation of the __str__() method









if __name__=='__main__':#defining our def main(): function as main, prioritizing it so that it will be treated as the main in C or java.
    main()#execute main

