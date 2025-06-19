a=int(input("enter first number"));
b=int(input("enter second number"));
op=input(("enter a valid operation(+,-,*,/)"));

def add():
    sum=a+b;
    print(sum);

def sub():
    diff=a-b;
    print(diff);

def mul():
    pro=a*b;
    print(pro);

def div():
    q=a/b;
    print(q);

if (op=="+"):
    add();
elif (op=="-"):
    sub();
elif (op=="*"):
    mul();
elif (op=="/"):
    div();
else:
    print("enter a valid operation")
