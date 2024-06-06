class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str) -> None:
        """
        With dummy nodes we would be adding unnecessary code.
        We initialize the cur node to the homepage string
        """
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None: 
        """
        Here is really important to take into account that the node "homepage" was created.
        """
        self.cur.next = ListNode(url, self.cur) # By declaring "prev" and "next" we are allowing the link declaration to take place in one line.
        self.cur = self.cur.next # We update the cur node.

    def back(self, steps: int) -> str:  
        while self.cur.prev and steps > 0: # We this we make sure we end up stopping as soon as we reach the last node or the desired number of steps.
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val
    
    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
        