
def hasCycle(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False

    fast = head.next.next
    slow = head.next
    while fast and fast.next and fast != slow:
        fast = fast.next.next
        slow = slow.next

    return fast == slow
