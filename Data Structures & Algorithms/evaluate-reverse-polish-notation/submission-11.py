class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackWindow = []
        operations = {"+", "-", "*", "/"}

        def performOperation(oper):
            num2 = stackWindow.pop()
            top = stackWindow.pop()
            if oper == "+":
                top += num2
            elif oper == "-":
                top -= num2
            elif oper == "*":
                top *= num2  
            elif oper == "/":
                top =  int(top / num2)
            stackWindow.append(top) 

        for token in tokens:
            if token in operations:
                performOperation(token)
            else:
                stackWindow.append(int(token))

        return stackWindow[0]
        