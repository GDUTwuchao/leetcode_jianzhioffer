
'''
所有排序算法参照wiki：
https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95
'''


#冒泡排序
'''
O(n^2)


'''
def bubbleSort(list):
    for iter_num in range(len(list)-1, 0, -1):
        for idx in range(iter_num):
            if list[idx] > list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
    return list


#合并排序
'''
O(nlogn)，需要额外O(n)的空间

递归法（Top-down）
1.申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
2.设定两个指针，最初位置分别为两个已经排序序列的起始位置
3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
4.重复步骤3直到某一指针到达序列尾
5.将另一序列剩下的所有元素直接复制到合并序列尾

迭代法（Bottom-up）
原理如下（假设序列共有 {\displaystyle n} n个元素）：

1.将序列每相邻两个数字进行归并操作，形成 {\displaystyle ceil(n/2)} {\displaystyle ceil(n/2)}个序列，
排序后每个序列包含两/一个元素
2.若此时序列数不是1个则将上述序列再次归并，形成 {\displaystyle ceil(n/4)} {\displaystyle ceil(n/4)}个序列，
每个序列包含四/三个元素
3.重复步骤2，直到所有元素排序完毕，即序列数为1
'''
def merge(left, right):
    result = []
    if left and right :
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


def mergeSort(list):
    if len(list)<=1:
        return list
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)



#插入排序
'''
O(n^2)

1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果该元素（已排序）大于新元素，将该元素移到下一位置
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5
'''
def insertSort(list):
    if len(list) == 1:
        return list
    for i in range(1,len(list)):
        for j in range(i,0,-1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1],list[j]

            else:
                break
    return list



#选择排序
'''
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。
'''
def selectSort(list):
    for i in range(len(list)-1):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] >= list[j]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list



#堆排序
'''
若以升序排序说明，把数组转换成最大堆积(Max-Heap Heap)，这是一种满足最大堆积性质(Max-Heap Property)的二叉树：
对于除了根之外的每个节点i, A[parent(i)] ≥ A[i]。
重复从最大堆积取出数值最大的结点(把根结点和最后一个结点交换，把交换后的最后一个结点移出堆)，
并让残余的堆积维持最大堆积性质


通常堆是通过一维数组来实现的。在数组起始位置为0的情形中：
父节点i的左子节点在位置 (2i+1)
父节点i的右子节点在位置 (2i+2)
子节点i的父节点在位置floor((i-1)/2)


在堆的数据结构中，堆中的最大值总是位于根节点（在优先队列中使用堆的话堆中的最小值位于根节点）。
堆中定义以下几种操作：
最大堆调整（Max Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
创建最大堆（Build Max Heap）：将堆中的所有数据重新排序
堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算
'''
def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

# 创建最大堆

    for start in range((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

# 堆排序
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst


#快速排序
def quickSort(list):
    if len(list) <= 1:
        return list
    left, right, mid = [], [], []
    pivot = list[0]
    for i in list:
        if i == pivot:
            mid.append(i)
        elif i > pivot:
            right.append(i)
        else:
            left.append(i)
    return quickSort(left) + mid + quickSort(right)







list = [15,2,31,4,7,23,11]
print(bubbleSort(list))
print(insertSort(list))
print(mergeSort(list))
print(selectSort(list))
print(heap_sort(list))
print(quickSort(list))