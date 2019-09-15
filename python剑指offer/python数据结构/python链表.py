class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SingelLinkedList:
    def __init__(self):
        self.head = None

    # 遍历链表
    def listprint(self):
        print('--------------遍历链表---------')
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    #在链表开头插入数据
    def atBegining(self, newdata):
        print('----------在表头插入数据----> {}'.format(newdata))
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode

    #在链表的末尾插入数据
    def atEnding(self, newdata):
        print('----------在链表末尾插入数据-------> {}'.format(newdata))
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode

    #在链表中间插入数据
    def inBetween(self, pre_node, newdata):
        print('----在 {} 后面插入 {} ---------'.format(pre_node.data,newdata))
        if pre_node is None:
            print('error!!')
        newNode = Node(newdata)
        newNode.next = pre_node.next
        pre_node.next = newNode

    #在链表中删除数据
    def removeNode(self, del_data):
        print('----删除数据 {} ----------'.format(del_data))
        if self.head is None:
            return
        if self.head.data == del_data:
            self.head = self.head.next
        else:
            pre = self.head
            cur = self.head.next
            while cur.data != del_data:
                pre = pre.next
                cur = cur.next
            pre.next = cur.next





list = SingelLinkedList()
list.head = Node('周一')
e2 = Node('周二')
e3 = Node('周四')
e4 = Node('周五')
list.head.next = e2
e2.next = e3
e3.next = e4
list.atBegining('周日')
list.atEnding('周六')
list.inBetween(e2,'周三')
list.removeNode('周四')
list.listprint()