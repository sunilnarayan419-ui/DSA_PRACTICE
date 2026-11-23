import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Step 1: Insert the first node of every linked list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        # Step 2: Create a dummy node
        dummy = ListNode(0)
        current = dummy

        # Step 3: Extract the smallest node
        while heap:

            val, i, node = heapq.heappop(heap)

            # Attach the smallest node
            current.next = node
            current = current.next

            # Step 4: Insert the next node from that list
            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy.next
