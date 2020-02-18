#!/usr/bin/python3
# -*-codig=utf8-*-

class Node(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)   #return的必须是一个字符串，作为print的参数


class LinkedList(object):
    def __init__(self, head = None):
        self.head = head


    #对LinkedList类可以使用了len()函数求长度
    def __len__(self):
        # 功能：输入头节点，返回链表长度
        curr = self.head
        counter = 0
        while curr:
            counter += 1
            curr = curr.next
        return counter

    # return的必须是一个字符串，作为print的参数
    def __str__(self):
        if self.head is None:
            return "linklist empty"

        link_node_val = ""
        cur_node = self.head
        while cur_node:
            link_node_val += str(cur_node.val)
            if cur_node.next:
                link_node_val += "--->"

            cur_node = cur_node.next
        return link_node_val


    def insert_to_front(self, data):
        if not data:
            return None
        insert_node = Node(data, self.head)
        self.head = insert_node
        return insert_node

    def append(self, data):
        if not data:
            return None
        append_node = Node(data)
        if self.head is None:
            self.head = append_node
            return append_node
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = append_node
        return append_node


    def reverse(self):
        if self.head is None:
            return None

        if self.head.next is None:
            return self.head

        p_node = self.head
        q_node = p_node.next
        p_node.next = None

        while q_node:
            r_node = q_node.next
            q_node.next = p_node
            p_node = q_node
            q_node = r_node

        self.head = p_node
        return self.head


    def delete_node(self, data):
        if self.head is None:
            return None
        if data == self.head.val:
            self.head = self.head.next

        pre_node = self.head
        curr_node = pre_node.next
        while curr_node:
            if curr_node.val != data:
                pre_node = curr_node
                curr_node = curr_node.next
            else:
                pre_node.next = curr_node.next
                #注意重新赋值，否则死循环
                curr_node = curr_node.next
                continue

        return self.head





node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

def printList(node):
    while node:
        print(node)
        node = node.next
printList(node1)


link_lst = LinkedList()
print(link_lst)
print("link list length is:%d" % len(link_lst))


link_lst.append(4)
print(link_lst)
print("link list length is:%d" % len(link_lst))


link_lst.insert_to_front(5)
print(link_lst)
print("link list length is:%d" % len(link_lst))


link_lst.insert_to_front(6)
print(link_lst)
print("link list length is:%d" % len(link_lst))


link_lst.insert_to_front(7)
link_lst.insert_to_front(7)
print(link_lst)
print("link list length is:%d" % len(link_lst))

print("reverse list is:\n")
link_lst.reverse()
print(link_lst)

delete_val = 7
print("delete data %s:\n" % delete_val)
link_lst.delete_node(delete_val)
print(link_lst)



