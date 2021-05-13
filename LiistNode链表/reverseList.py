"""
反转一个单链表。
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
做不出来的原因分析：
我想的是走到尾结点处，把尾结点值赋给新链表，然后删掉尾结点，head是可以后移的（pre=head,head=head.next），但是pre不能前移
"""
# class Solution:
#     def reverseList(self, head: ListNode):
#         pre = head
#         h = ListNode(None)
#         node = h.next
#         # 删除尾结点
#         while pre != None:
#             while head.next != None:
#                 pre = head
#                 head = head.next
#             node = ListNode(head.val)
#             pre.next = None
#             head = pre
"""
论坛思路：是一个链表从前往后更改链表指针域的指向 的操作！其实核心代码是删除头结点的操作
注意：1.头结点和头指针是不一样的
pre = ListNode(None)就是定义了一个头结点
pre = None是定义了一个头指针

"""
class Solution:
    def reverseList(self, head: ListNode):
        # pre = ListNode(None)
        pre = None
        cur = head
        while cur:
            # 避免丢失后面的链
            temp = cur.next
            # 删除头结点的操作是pre = cur.next
            cur.next = pre
            #后移pre cur
            pre = cur
            cur = temp
        return pre


