tasks=[]
while True:
   print("1.add task \n 2. view tasks \n 3. exit")
   choice=int(input("enter your choice : "))
   if(choice==1):
    task=input("enter task : ")
    tasks.append(task)

   elif(choice==2):
        for i, t in enumerate(tasks):
          print(f"{i+1}. {t}")

   elif(choice==3):
        break;
   else:
        print("enter a valid number")

   with open("tasks.txt", "w") as f:
    for task in tasks:
        f.write(task + "\n")

