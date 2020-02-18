import pysnooper

#@pysnooper.snoop()

#递归方式，传入的数组长度一直在变，所以不能返回正确的下标，返回True或False比较好
def binary_search(lst, val):
    if not lst:
        return False

    mid = (len(lst) - 1) // 2


    if val == lst[mid]:
        return True
    elif val < lst[mid]:
        return binary_search(lst[0:mid], val)   #注意return回来
    else:
        return binary_search(lst[mid+1:], val)  #注意return回来



#非递归方式，start和end值可以正确计算位置，所以可以返回下标值
def binary_search_2(lst, val):
    n = len(lst)
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if val == lst[mid]:
            return mid
        elif val < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return None



my_list = [1, 2]
val = 3

res = binary_search(my_list, val)
print("binary_search:%s" % res)

res2 = binary_search_2(my_list, val)
print("binary_search_2:%s" % res2)

