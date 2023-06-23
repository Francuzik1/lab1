class Node:
    def __init__(self, name_dataval=None, num_dataval=None):
        self.name_dataval = name_dataval
        self.num_dataval = num_dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def finder_number(self, name):
        printval = self.headval
        while printval.name_dataval != name:
            printval = printval.nextval
        else:
            print(printval.num_dataval)

    def finder_name(self, number):
        printval = self.headval
        while printval.num_dataval != number:
            printval = printval.nextval
        else:
            print(printval.name_dataval)


list = SLinkedList()
list.headval = Node("Mon", "1")
e2 = Node("Tue", "2")
e3 = Node("Wed", "3")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval = None
list.finder_number("Tue")
list.finder_name("1")
