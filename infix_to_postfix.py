import stack_linked_list
def infix_to_postfix(infix):
    operator = stack_linked_list.stack()
    postfix = ""
    for i in infix:
        if i == " ":
            continue
        if i in ("*","/"):
            while operator.peek() and operator.peek() in ("*","/"):
                postfix+=operator.pop()
            operator.push(i)
        elif i in ("+","-"):
            while operator.peek() and operator.peek() in ("+","-","*","/"):
                postfix+=operator.pop()
            operator.push(i)
        elif i == "(":
            operator.push(i)
        elif i == ")":
            while operator.peek()!="(":
                postfix+=operator.pop()
            operator.pop()
        else:
            postfix+=i
    while operator.count>0:
        postfix+=operator.pop()
    return postfix

print(infix_to_postfix("A * ( B + C ) - D * F - E"))
