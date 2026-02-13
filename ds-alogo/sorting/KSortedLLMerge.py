
import heapq
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def list_to_linked_list(lists):
    linked_lists = []
    for list in lists:
        if list is not None:
            head = None
            tail = None
            for value in list:
                if head is None:
                    head = LinkedListNode(value)
                    tail = head
                else:
                    tail.next = LinkedListNode(value)
                    tail = tail.next
            linked_lists.append(head)
    return linked_lists

def linked_list_to_list(head):
    list = []
    node = head
    while node is not None:
        list.append(node.value)
        node = node.next
    return list


def merge_k_lists(llists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    dummy = LinkedListNode(-1)
    tail = dummy
    min_heap = []

    for i, head in enumerate(llists):
        if head is not None:
            min_heap.append((head.value, i, head))

    heapq.heapify(min_heap)
    while min_heap:
        value, i, node = heapq.heappop(min_heap)
        tail.next = node
        tail = tail.next
        if node.next is not None:
            heapq.heappush(min_heap, (node.next.value, i, node.next))
    return dummy.next

if __name__ == '__main__':
    lists = [
        [1, 3, 5],
        [3, 4],
        [7]
    ]
    linked_lists = list_to_linked_list(lists)
    result = merge_k_lists(linked_lists)
    result_list = linked_list_to_list(result)
    print(result_list)
