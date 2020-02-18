import pysnooper
#暴力法
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_area = 0
#
#         for i in range(len(height)-1):
#             for j in range(i+1, len(height)):
#                 area = (j-i) * min(height[i], height[j])
#                 if area > max_area:
#                     max_area = area
#
#
#         return max_area



#双指针法
@pysnooper.snoop()
def maxArea(height):

    if len(height) < 2:
        return None

    if len(height) == 2:
        return min(height[0], height[1])

    max_area = 0
    i = 0
    j = len(height)-1

    while i < j:
        area = (j-i) * min(height[i], height[j])
        if area > max_area:
            max_area = area

        if height[i] <= height[j]:
            i = i+1
        else:
            j = j-1

    return max_area



lst = [1,8,6,2,5,4,8,3,7]
res = maxArea(lst)
print(res)
