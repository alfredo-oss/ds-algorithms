from LinkedList.Creation import ListNode
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            nxt = curr.next # We store the original linked list and its connections but the current node
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
# Helper function to convert a list into a linked list
def createLinkedList(values):
    dummy = ListNode(0)
    curr = dummy
    for value in values:
        curr.next = ListNode(value)
        curr = curr.next
    return dummy.next

solution = Solution()
test1 = [1,2,3,4,5]
head = createLinkedList(test1)
res = solution.reverseList(head)
print(res.val)