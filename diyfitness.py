food={"Rice":[28,2.7,0.3,199],"Egg":[0.38,6,5,266],"Idli":[8,2,0,39],"Dal":[28,2.7,0.3,199],"Roti":[28,2.7,0.3,199],"Paratha":[28,2.7,0.3,199],"Momos":[28,2.7,0.3,199],"Potato":[28,2.7,0.3,199],"Pasta":[28,2.7,0.3,199],"Paneer":[28,2.7,0.3,199],"Chicken":[28,2.7,0.3,199],"Curry":[28,2.7,0.3,199],"Fish":[28,2.7,0.3,199],"Mutton":[28,2.7,0.3,199],"Biryani":[28,2.7,0.3,199]}
types=["Carbohydrates","Proteins","Fats","Calories"]

b=1
l=1
s=1
d=1
carb,prot,fat,cal=0,0,0,0
breakfast=[]
lunch=[]
snacks=[]
dinner=[]
total={"Carbohydrate":"","Proteins":"","Fats":"","Calories":""}
for x in range(0,51):
    print("-",end="")
print()
print("welcome To Food Tracker")
for x in range(0,51):
    print("-",end="")
print()
print("BREAKFAST : ")
while(b==1):
    n=input("Enter What you ate= ")
    if n=="":
        print("Opps!! You didnt enter anything, Enter again")
        continue
    name=n.capitalize()
    breakfast.append(name)
    r=int(input("Wanna Add more to the list 1.yes 0.no= "))
    if r==0:
          b=0
for x in range(0,51):
    print("-",end="")
print()
print("LUNCH")
while(l==1):
    n=input("Enter What you ate= ")
    if n=="":
        print("Opps!! You didnt enter anything, Enter again")
        continue
    name=n.capitalize()
    lunch.append(name)
    r=int(input("Wanna Add more to the list 1.yes 0.no= "))
    if r==0:
          l=0
for x in range(0,51):
    print("-",end="")
print()
print("SNACKS")
while(s==1):
    n=input("Enter What you ate= ")
    if n=="":
        print("Opps!! You didnt enter anything, Enter again")
        continue
    name=n.capitalize()
    snacks.append(name)
    r=int(input("Wanna Add more to the list 1.yes 0.no= "))
    if r==0:
          s=0
for x in range(0,51):
    print("-",end="")
print()
print("DINNER")
while(d==1):
    n=input("Enter What you ate= ")
    if n=="":
        print("Opps!! You didnt enter anything, Enter again")
        continue
    name=n.capitalize()
    dinner.append(name)
    r=int(input("Wanna Add more to the list 1.yes 0.no= "))
    if r==0:
          d=0
for x in range(0,51):
    print("-",end="")
print()
print("Note: The Quantities Displayed will be per 100 grams")
for x in range(0,51):
    print("-",end="")
print()
print("BREAKFAST:")
for x in range(0,51):
    print("-",end="")
print()
for billy in breakfast:
    for i,j in food.items():
        if i == billy:
            print("You chose :",i)
            for x in range(0,51):
                print("-",end="")
            print()
            c=0
            for k in j:
                print(types[c]," = ",k," units")
                c+=1
            for x in range(0,51):
                print("-",end="")
            print()
print("LUNCH")
for x in range(0,51):
    print("-",end="")
print()
for billy in lunch:
    for i,j in food.items():
        if i == billy:
            print("You chose :",i)
            for x in range(0,51):
                print("-",end="")
            print()
            c=0
            for k in j:
                print(types[c]," = ",k," units")
                c+=1
            for x in range(0,51):
                print("-",end="")
            print()
print("SNACKS")
for x in range(0,51):
    print("-",end="")
print()
for billy in snacks:
    for i,j in food.items():
        if i == billy:
            print("You chose :",i)
            for x in range(0,51):
                print("-",end="")
            print()
            c=0
            for k in j:
                print(types[c]," = ",k," units")
                c+=1
            for x in range(0,51):
                print("-",end="")
            print()
print("DINNER")
for x in range(0,51):
    print("-",end="")
print()
for billy in dinner:
    for i,j in food.items():
        if i == billy:
            print("You chose :",i)
            for x in range(0,51):
                print("-",end="")
            print()
            c=0
            for k in j:
                print(types[c]," = ",k," units")
                c+=1
            for x in range(0,51):
                print("-",end="")
            print()
def calculate_carb(food,billy):#---- to calculate carbs
    return food[billy][0] 
def calculate_Proteins(food,billy):#---- to calculate proteins
    return food[billy][1] 
def calculate_Fats(food,billy):#---- to calculate fats
    return food[billy][2] 
def calculate_Calories(food,billy):#---- to calculate Calories
    return food[billy][3] 


for billy in breakfast:
    if billy in food.keys():
        carb+=calculate_carb(food,billy)
        prot+=calculate_Proteins(food,billy) 
        fat+=calculate_Fats(food,billy)
        cal+=calculate_Calories(food,billy)


for billy in lunch:
    if billy in food.keys():
        carb+=calculate_carb(food,billy)
        prot+=calculate_Proteins(food,billy) 
        fat+=calculate_Fats(food,billy)
        cal+=calculate_Calories(food,billy)


for billy in snacks:
    if billy in food.keys():
        carb+=calculate_carb(food,billy)
        prot+=calculate_Proteins(food,billy) 
        fat+=calculate_Fats(food,billy)
        cal+=calculate_Calories(food,billy)


for billy in dinner:
    if billy in food.keys():
        carb+=calculate_carb(food,billy)
        prot+=calculate_Proteins(food,billy) 
        fat+=calculate_Fats(food,billy)
        cal+=calculate_Calories(food,billy)
print("Total Carbohydrate intake : ",carb," units")
print("Total Protein intake : ",prot," units")
print("Total Fats intake : ",fat,"units")
print("Total Calorie gained : ",cal,"units")
print("THANK YOU FOR USING THIS SOFTWARE")

            




    



