class WebPage:
    def __init__(self, address=None):
        self.address  = address
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = WebPage()
        self.tail = WebPage()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.activePage = None
        self.visit(homepage)
        
    def visit(self, url: str) -> None:
        self.clearForwardHistory()
        newPage = WebPage(url)
        newPage.next = self.tail
        newPage.prev = self.tail.prev
        self.tail.prev.next = newPage
        self.tail.prev = newPage
        self.activePage = newPage
        

    def back(self, steps: int) -> str:
        currentPage = self.activePage
        while currentPage.prev and steps >= 0:
            if steps == 0:
                self.activePage = currentPage
                return self.activePage.address
            currentPage = currentPage.prev
            steps -= 1
        print(f"Backward steps left: {steps}, currentPage: {currentPage.next.address}")
        self.activePage = currentPage.next
        return self.activePage.address
        
    def forward(self, steps: int) -> str:
        currentPage = self.activePage
        while currentPage.next and steps >= 0:
            if steps == 0:
                self.activePage = currentPage
                return self.activePage.address
            currentPage = currentPage.next
            steps -= 1
        print(f"Forward steps left: {steps}, currentPage: {currentPage.prev.address}")
        self.activePage = currentPage.prev
        return self.activePage.address
    
    def clearForwardHistory(self):
        if self.activePage:
            self.activePage.next = self.tail
            self.tail.prev = self.activePage
        



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)