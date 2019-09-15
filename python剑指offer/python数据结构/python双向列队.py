'''
端队列(或两端队列)具有从任一端添加和删除元素的功能。 Deque模块是集合库的一部分。
它具有添加和删除可以直接用参数调用的元素的方法。

'''

import collections
dequeue = collections.deque(['周一','周二'])
print(dequeue)

dequeue.append('周三')
print(dequeue)

dequeue.appendleft('周日')
print(dequeue)

dequeue.pop()
print(dequeue)

dequeue.popleft()
print(dequeue)

dequeue.reverse()
print(dequeue)