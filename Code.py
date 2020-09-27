name = input("Enter your name:")
month = input("What month were you born(enter as number 1-12):")
day = input("What day were you born:")
month = int(month)
day = int(day)
season = ""

if(6 <= month <=8):
  season = "Summer"
elif(9 <=month <= 11):
  season = "Fall"
elif(3 <= month <= 5):
  season = "Spring"
else:
  season = "Winter"
  
print("Hi " , name , ", you are born on " , month, "/", day, "! You are a ", season, " baby!")
