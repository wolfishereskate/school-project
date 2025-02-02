def isempty(stk):
    if stk==[] :
        return True
    else:
        return False
def Push(stk,elt):
    stk.append(elt)
    print(stk)
    print('eelement inserted successfully')
def Pop(stk):
    if isempty(stk):
        print('underflow')
    else: print(stk.pop())
def Seek(stk):
    if isempty(stk):
        print('underflow')
    else: 
        print('top element',stk[-1])
def Display(stk):
    a=stk[::-1]    
    print(a)
stack=[]
while True:
    print('........available stack oprations.......')
    print('          1.push')
    print("          2.pop")
    print('          3.seek')
    print('          4.display')
    print('          5.end')
    x=int(input('enter operation number '))    
    if x==1:
        element=input('entter eelement u want to add ')
        Push(stack,element)
    if x==2:
        Pop(stack)
    if x==3:
        Seek(stack)
    if x==4:
        Display(stack)     
    elif x==5:
        break