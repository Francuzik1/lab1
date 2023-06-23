class Node:
    def __init__(self, num=None, nextval=None, earlyval=None):
        self.num = num
        self.nextval = nextval
        self.earlyval = earlyval


class SLinkedList:
    def __init__(self):
        self.headval = None

    def finder(self):
        finder_var = []
        printval = self.headval
        while printval is not None:
            if len(printval.num) == 7:
                finder_var.append(printval.num)
            printval = printval.nextval
        print(finder_var)
        return finder_var


def printList(head):
    ptr = head
    while ptr is not None:
        print(ptr.num)
        ptr = ptr.nextval


def construct(keys):
    head = None
    for i in range(len(keys)):
        head = Node(keys[i], head)
    return head


list = SLinkedList()
list.headval = Node("123")
e2 = Node("8097863")
e3 = Node("234")
e4 = Node("8994356")
e5 = Node("8456783")
list.headval.earlyval = None
list.headval.nextval = e2
e2.earlyval = list.headval.nextval
e2.nextval = e3
e3.earlyval = e2
e3.nextval = e4
e4.earlyval = e3
e4.nextval = e5
e5.earlyval = e4
printList(construct(list.finder()))
