import pysnooper

#@pysnooper.snoop()
def bubble_sort(mylist):
    lst_len = len(mylist)
    for i in range(lst_len - 1):
        for j in range(lst_len - 1 - i):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

    return mylist


#增加change变量，记录一趟排序中是否发生位置交换
#如果没有交换，则表示已经有序。是冒泡排序的一种优化

def bubble_sort2(mylist):
    lst_len = len(mylist)

    for i in range(lst_len - 1):
        change = 0
        for j in range(lst_len - 1 - i):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
                change += 1
        if change == 0:
            break

    return mylist




def quick_sort(mylist):

    if len(mylist) < 2:
        return mylist

    base = mylist[0]
    left = []
    right = []

    for i in range(1, len(mylist)):
        if mylist[i] <= base:
            left.append(mylist[i])
        else:
            right.append(mylist[i])

    return quick_sort(left) + [base] + quick_sort(right)


#@pysnooper.snoop()
#方法一：申请新的newlist，空间复杂度O(n)
def insert_sort1(mylist):
    if len(mylist) < 2:
        return mylist

    newlist = []
    newlist.append(mylist[0])

    for i in mylist[1:]:
         for j in range(len(newlist)):
             if i < newlist[j]:
                 newlist.insert(j, i)
                 break
             #如果待插入元素比newlist里的元素都大，则不会在if语句中跳出，
             #会遍历到newlist末尾，直接append就可以了
             if j == len(newlist)-1:
                 newlist.append(i)

    return newlist

#方法二：不申请新的newlist
def insert_sort2(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1, n):
        # 控制将拿到的元素放到前面有序序列中正确位置的过程
        for i in range(j, 0, -1):
            # 如果比前面的元素小，则往前移动
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            # 否则代表比前面的所有元素都小，不需要再移动
            else:
                break
    print(alist)

def merge_sort(mylist):
    pass


lst = [21,78,9,34,12,65,1]
lst2= [1]
lst3 = [5,3]

#bubble_sort(lst)
#print(quick_sort(lst))
#print(bubble_sort2(lst))
insert_sort2(lst3)