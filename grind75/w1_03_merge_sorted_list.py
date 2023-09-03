
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2
    if not list2:
        return list1
    dummy =  ListNode(0)
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail.next.next = None
        tail = tail.next
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return dummy.next

