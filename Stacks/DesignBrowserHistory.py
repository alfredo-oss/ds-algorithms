class BrowserHistory:
    def __init__(self, homepage: str):
        self.i = 0 # This pointer will indicate the position of the current page.
        self.len = 1 # This pointer will indicate the real lenght of the array.
        self.history = [homepage] # Declaration of the array that will hold the array of strings, initially it is just set to homepage.

    def visit(self, url: str) -> None:
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else: 
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i + 1
        
    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0) # We select the maximum value between ("the current page" - "the steps declared by the user") and 0 which conforms with the requirement that you can't go out of bounds.
        return self.history[self.i] # We return the value that is present at the string array
    
    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.len-1) # Taking the minimum is actually easier than declaring an if statement managing some edge case, it adds that beautiful layer of abstraction
        return self.history[self.i]