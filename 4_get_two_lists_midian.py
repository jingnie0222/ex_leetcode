import math
import pysnooper


#方法一：使用系统函数sort，时间复杂度应该是(m+n)log(m+n)，不符合题目要求
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         total_num = nums1 + nums2
#         total_num.sort()
#
#         mid = math.floor(len(total_num) / 2)
#
#         if len(total_num) % 2 == 0:
#             midian = (total_num[mid - 1] + total_num[mid]) / 2
#         else:
#             midian = total_num[mid]
#
#         return midian


#方法二：一位一位的找，直到找到中位数，没调出来。
#需要考虑奇偶数、边界问题等
def findMedianSortedArrays(nums1, nums2):

    total = len(nums1) + len(nums2)
    mid = total//2 if total % 2 == 1 else (total//2 -1)  #根据两个数组个数的奇偶，返回不同的mid值

    i, j, count = 0, 0, 0
    flag1, flag2 = True, True
    midian1 = 0  #保存中位数，奇数的时候就是中位数，偶数的时候是第一个中位数，然后再找下一个中位数
    midian2 = 0 #偶数时的第二个中位数

    while True:
        midian1 = midian2

        if i == len(nums1):  # 防止越界，表示已经到末尾
            flag1 = False

        if j == len(nums2):  # 防止越界，表示已经到末尾
            flag2 = False

        if count == mid:
            if total % 2 == 0:

                return (midian1 + midian2)/2
            else:
                return midian2

        if i < len(nums1) or j < len(nums2):
            if not flag1:
                j += 1
                midian = nums2[j]
            if not flag2:
                i += 1
                midian = nums1[i]

            if flag1 and flag2:
                if nums1[i] <= nums2[j]:
                    i += 1
                    midian = nums2[j]
                else:
                    j += 1
                    midian = nums1[i]

        count += 1


#方法三：补位法，把两个数组的缝隙都填满，这样每个数组都变成了奇数个数字，整体变成了偶数个数字。这样就不用考虑奇偶性了。

@pysnooper.snoop()
def findMedianSortedArrays3(nums1, nums2):

    if len(nums1) > len(nums2):  #必须保证nums1是最短的，否则算l_max2和r_min2的时候可能越界
        nums1 ,nums2 = nums2, nums1

    m = len(nums1)
    n = len(nums2)

    lo = 0
    hi = 2*m

    while lo <= hi:
        i = (lo+hi) // 2
        j = m + n - i

        l_max1 = float("-inf") if i==0 else float(nums1[(i-1)//2])
        r_min1 = float("inf") if i==2*m else float(nums1[i//2])

        l_max2 = float("-inf") if j==0 else float(nums2[(j-1)//2])
        r_min2 = float("inf") if j==2*n else float(nums2[j//2])

        if l_max1 > r_min2:
            hi = i - 1
        elif l_max2 > r_min1:
            lo = i + 1
        else:
            break

    return (max(l_max1, l_max2) + min(r_min1, r_min2))/2




a = [1]
b = [2,3]

res = findMedianSortedArrays3(a, b)
print(res)