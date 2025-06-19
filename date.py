import calendar
import datetime
while True:
    print("-------calendar app-------")
    print("1.show today's date :")
    print("2.show calendar for a month")
    print("3.check if a year is leap year")
    print("4.exit")
    choice=int(input("enter a number between 1 to 4 : "))

    if choice == 1:
      today = datetime.date.today()
      print("Today's date is:", today.strftime("%A, %d %B %Y"))

    elif choice== 2 :
       year=int(input("enter year : "))
       month=int(input("enter month: "))
       print("\n", calendar.month(year, month))

    elif choice== 3 :

      year = int(input("Enter year to check: "))
      if calendar.isleap(year):
        print(year, "is a leap year.")
      else:
        print(year, "is not a leap year.")

    elif choice==4:
       print("exiting,goodbye")
       break
    else:
       print("enter a valid choice")
       


