import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'hoteldb')
mycursor = mydb.cursor()
total=0
item=[]
while(True):
    print("\n please select an option")
    print("1. Tea -------- 15rs")
    print("2. Coffee------20")
    print("3. Snaks-------40")
    print("4. Burger------50")
    print("5. Generate bill")
    print("6. Exit")
    ch=int(input("enter the choice"))
    if(ch==1):
        print("Added tea")
        qty=int(input("enter the quantity"))
        total+=15*qty
        item.append("tea x"+str(qty))
        #print("quantity",qty)
        #print("total",total)
    elif(ch==2):
        print("Added Coffee")
    elif(ch==3):
        print("Added Snaks")
    elif(ch==4):
        print("Added Burger")
    elif(ch==5):
        print("Generating bill")

    elif(ch==6):
        break