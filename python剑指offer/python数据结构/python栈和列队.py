#使用list表示stack，使用append方法表示push，是有pop表示pop方法

#python list实现队列，可以使用insert()和pop()方法添加和移除元素

class Queue:
    def __init__(self):
        self.queue = []

    def addToQueue(self,  data):
        if data not in self.queue:
            print('queue中添加数据 {}'.format(data))
            self.queue.insert(0, data)
            return True
        return False

    def removeFrimQueue(self):
        if len(self.queue)>0:
            print('queue中删除数据 {}'.format(self.queue.pop()))
            # return self.queue.pop()
        else:
            print('No elements in Queue!')



class Stack:
    def __init__(self):
        self.stack = []

    def addToStack(self, data):
        self.stack.append(data)
        print('stack中添加数据 {}'.format(data))

    def removeFromStack(self):
        if len(self.stack)>0:
            print("stack中删除数据 {}".format(self.stack.pop()))
        else:
            print('stack is None')



thequeue = Queue()
thestack = Stack()
for i in range(10):
    thequeue.addToQueue(i)
    thestack.addToStack(i)
print(thequeue.queue)
print(thestack.stack)
for j in range(11):
    thequeue.removeFrimQueue()
    thestack.removeFromStack()