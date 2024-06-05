class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str) -> None:
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.home_page = ListNode(homepage)
        self.left.next = self.home_page
        self.home_page.prev = self.left
        self.home_page.next = self.right
        self.right.prev = self.home_page

    def visit(self, url: str) -> None:
        node, prev, next = ListNode(url), self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def back(self, steps: int) -> str: 
        node = self.left.next
        while node and steps > 0:
            node = node.next
            steps -= 1
        if node == self.right or not node:
            return self.right.prev.val    
        return node.val
    
    def forward(self, steps: int) -> str:
        node = self.right.prev
        while node and steps > 0:
            node = node.prev
            steps -= 1
        if node == self.left or not node:
            return self.left.next
        return node.val
        