# 链表遍历、链表相加（引入sum值进行加和）、考虑链表长度不一样、考虑进位
class listNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def twoSum(listNode1, listNode2):
    for node in range(listNode1.val):
        if(node.next != None):
            print(node.val)
    for node in range(listNode2.val):
        if(node.next != None):
            print(node.val)

if __name__ == '__main__':
    listNode1 = listNode([2, 4, 3])
    listNode2 = listNode([5, 6, 4])
    twoSum(listNode1,listNode2)



