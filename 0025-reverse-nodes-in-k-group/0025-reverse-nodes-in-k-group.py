class Solution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:

            # Step 1: Find the kth node
            kth = group_prev

            for i in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next

            # Step 2: Store the next group's starting node
            group_next = kth.next

            # Step 3: Reverse the current group
            prev = group_next
            curr = group_prev.next

            while curr != group_next:

                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Step 4: Connect the reversed group
            temp = group_prev.next

            group_prev.next = kth
            group_prev = temp
