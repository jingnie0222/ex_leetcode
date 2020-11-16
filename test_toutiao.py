import random
import time
import pysnooper

'''
产生m个n范围内的不重复随机数
'''

#时间复杂度为O(n^2)
def gen_rand_notrepeat(n, m):
    rand_list = []
    while True:
        new = random.randint(0, n)
        if new not in rand_list:
            rand_list.append(new)
        if len(rand_list) >= m:
            break
    return rand_list


#将list改为字典，可以使时间复杂度降低为O(n)
def gen_rand_notrepeat2(n, m):
    rand_dict = {}
    while True:
        new = random.randint(0, n)
        if new not in rand_dict:
            rand_dict[new] = None
        if len(rand_dict) >= m:
            break
    return rand_dict.keys()

n = 100
m = 10
rand_list = gen_rand_notrepeat(n, m)
print(rand_list)


'''
一个有序数组，判断其中是否有重复元素，如果有返回其起始和结束的位置，如果没有则返回-1, -1
'''

def is_sort_repeat(mylist):
    length = len(mylist)
    i = 0
    pos = 0  #记录重复元素的起始位置
    count = 0  #记录重复元素的个数
    repeat = False

    while i < length-1:
        if mylist[i] < mylist[i+1]:
            if not repeat:
                pos = i+1
            else:
                break
        if mylist[i] == mylist[i+1]:
            repeat = True
            count += 1
        i += 1

    if repeat:
        return pos, pos+count
    else:
        return -1,-1


def get_start(string):
    desk = [ch for ch in string]
    hand = []
    hand.insert(0, desk.pop())
    for i in range(len(desk)):
        hand.insert(0, hand.pop())
        hand.insert(0, desk.pop())
    return ''.join(hand)


#寻找出现次数超过一半的数字
#由于该数字的出现次数比所有其他数字出现次数的和还要多,基于这个条件：
#设置一个bsae，用来保存数组中遍历到的某个数字；一个count，表示当前数字的出现次数，初始化为1;
#如果下一个数字与之前base保存的数字相同，则count加1
#如果下一个数字与之前base保存的数字不同，则count减1
#每当出现次数count变为0后，用base保存下一个数字，并把count重新设为1。 直到遍历完数组中的所有数字为止
def find_data(nums):
    base = nums[0]
    count = 1

    for i in nums[1:]:
        if count == 0:
            base = i
            count = 1
            continue
        if i == base:
            count = count + 1
            continue
        if i != base:
            count = count - 1

    return  base



#给定一个字符串，输出字母出现次数第二大的字母及其次数
def find_char(str):
    str_dict = {}
    for ch in str:
        if ch in str_dict:
            str_dict[ch] += 1
        else:
            str_dict[ch] = 1
    print(str_dict)

    #str_dict.items()返回的是元组对的列表，reverse=True表示逆序排序，所以str_dict_lst[1]就是出现次数第二大元组对
    str_dict_lst = sorted(str_dict.items(), key = lambda d:d[1], reverse=True)
    print(str_dict_lst[1])

#find_char('afffccbbbb')



@pysnooper.snoop()
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)

g = foo()
print(next(g))
print("*"*20)
print(next(g))


# 一个人有一瓶药，共100颗。每天，这个人都需要吃半片这种药。
# 这个人的做法是，每次从药瓶里随机取一颗，如果是完整的一片，那么分成两半，服用半片，另外半片放回瓶中。如果正好是半片，那么直接服用。
# 假定不管是整片还是半片，药片被抓取的概率都是相同的。试写程序去模拟这200天的服药过程。
# 实例输出：
# Day 1:Pill #5
# Day 2:Pill #8
# Day 3:Pill #5
# ……
# Day 200:Pill #40

def get_pill():
    days = [i for i in range(1, 21)]
    pills = [i for i in range(1, 11)] * 2
    result = {}
    for day in days:
        pill = random.choice(pills)
        result[day] = pill
        pills.remove(pill)

    return result

ret = get_pill()
for k,v in ret.items():
    output = "Day {0}: Pill # {1}". format(k, v)
    print(output)

 
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 示例：
# 输入：["eat","tea","tan","ate","nat","bat"],
# 输出：[["ate","eat","tea"], ["nat","tan"], ["bat"]]
# 说明：
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。

def group(strs):
    str_dict = {}
    for str in strs:
        tmp = "".join(sorted(str))
        if tmp in str_dict:
            str_dict[tmp].append(str)
        else:
            str_dict[tmp] = [str]

    return [val for val in str_dict.values()]


if __name__ == "__main__":
    pass
    #test_lst = [3,3,3,3,3,3,3]
    #res = is_sort_repeat(test_lst)
    #print(res)

    #string = 'ACEBFD'
    #print(get_start(string))

    #nums = [5, 5, 5, 5, 1]
    #base = find_data(nums)
    #print(base)




