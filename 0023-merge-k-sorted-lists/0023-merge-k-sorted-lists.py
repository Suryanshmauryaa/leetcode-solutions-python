import heapq
ListNode.__lt__ = lambda self, other: self.val < other.val

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for head in lists:
            if head:
                heapq.heappush(heap, head)
                
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            smallest_node = heapq.heappop(heap)
            current.next = smallest_node
            current = current.next
            
            if smallest_node.next:
                heapq.heappush(heap, smallest_node.next)
                
        return dummy.next