class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None


def get_arr(head):
    arr = []
    while head is not None:
        arr.append(head.data)
        head = head.next
    return arr


def build_ll(arr):
    if len(arr) == 0:
        return None
    node = LinkedList(arr[0])
    node.next = build_ll(arr[1:])
    return node

def get_tail(head):
    while head.next is not None:
        head = head.next
    return head
