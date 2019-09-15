


'''
堆是一种特殊的树结构，其中每个父节点小于或等于其子节点。 然后它被称为最小堆(Min Heap)。
如果每个父节点大于或等于其子节点，则称它为最大堆(Max Heap)。
实施优先级队列是非常有用的，在该队列中，具有较高权重的队列项目在处理中具有更高的优先级。

堆是通过使用python内建的名称为heapq的库创建的。

heapify - 此函数将常规列表转换为堆。 在结果堆中，最小的元素被推到索引位置0。但是其余的数据元素不一定被排序.
heappush - 这个函数在堆中添加一个元素而不改变当前堆。
heappop - 该函数返回堆中最小的数据元素。
heapreplace - 该函数用函数中提供的新值替换最小的数据元素


'''
import heapq
# H = [21,31,45,23,1,22,19]
# heapq.heapify(H)
# print(H)
# heapq.heappush(H,8)
# print(H)
# heapq.heappop(H)
# print(H)
# heapq.heapreplace(H,7)
# print(H)

# 实现最小堆排序
def minHeapSort(data):
    l1 = []
    for i in data:
        heapq.heappush(l1, i)
    print(l1)
    return [heapq.heappop(l1) for i in range(len(l1))]

print(minHeapSort([21,13,45,29,1,4,0,22]))