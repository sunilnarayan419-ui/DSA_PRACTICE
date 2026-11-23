class Solution:
    def swapPairs(self, head):
        # Create a dummy node
        dummy = ListNode(0)
        dummy.next = head

        # Previous node
        prev = dummy

        while prev.next and prev.next.next:

            # Identify the two nodes
            first = prev.next
            second = first.next

            # Swap the nodes
            first.next = second.next
            second.next = first
            prev.next = second

            # Move to the next pair
            prev = first

        return dummy.next
