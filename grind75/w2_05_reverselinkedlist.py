
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return head

        # p, q, r = None, head, head.next

        # while r.next:
        #     q.next = p
        #     p = q
        #     q = r
        #     r = r.next

        # q.next = p
        # r.next = q
        # return r
        prev = None
        while head != None:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev
