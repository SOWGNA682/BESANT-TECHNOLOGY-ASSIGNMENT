def mango():
    print("welcome to the varities of mangoes")
    var=input("do you want to buy a varities of mangoes?:")
    if var == "yes":
        per_kg=50
        fullname=input("enter your fullname: ")
        mobile_number=int(input("enter your number: "))
        number_of_kgs=int(input("enter number of kgs you want: "))
        total_amount=per_kg*number_of_kgs
        print(f"hi {fullname} your mobile number is {mobile_number} your amount is{total_amount} ")
        
    else:
        print("thank you")
        
def banana():
    print("welcome to the varities of banana")
    var=input("do you want to buy a varities of banana?:")
    if var == "yes":
        per_dozen=25
        fullname=input("enter your fullname: ")
        mobile_number=int(input("enter your number: "))
        number_of_dozens=int(input("enter number of dozens you want: "))
        total_amount=per_dozen*number_of_dozens
        print(f"hi {fullname} your mobile number is {mobile_number} your amount is{total_amount} ")
        
    else:
        print("thank you")
        
def  milk():
    print("welcome to the varities of milk")
    var=input("do you want to buy a varities of milk?:")
    if var == "yes":
        per_liter=100
        fullname=input("enter your fullname: ")
        mobile_number=int(input("enter your number: "))
        number_of_liters=int(input("enter number of liters you want: "))
        total_amount=per_liter*number_of_liters
        print(f"hi {fullname} your mobile number is {mobile_number} your amount is{total_amount} ")    
    else:
        print("thank you")
        
def  vegetables():
    print("welcome to the varities of vegetables")
    var=input("do you want to buy a varities of vegetables?:")
    if var == "yes":
        per_kg=50
        fullname=input("enter your fullname: ")
        mobile_number=int(input("enter your number: "))
        number_of_kgs=int(input("enter number of kgs you want: "))
        total_amount=per_kg*number_of_kgs
        print(f"hi {fullname} your mobile number is {mobile_number} your amount is{total_amount} ")    
    else:
        print("thank you")

def pulses(): 
    print("welcome to the varities of pulses")
    var=input("do you want to buy a varities of pulses?:")
    if var == "yes":
        per_kg=50
        fullname=input("enter your fullname: ")
        mobile_number=int(input("enter your number: "))
        number_of_kgs=int(input("enter number of kgs you want: "))
        total_amount=per_kg*number_of_kgs
        print(f"hi {fullname} your mobile number is {mobile_number} your amount is{total_amount} ")    
    else:
        print("thank you") 

def millets():
    print("welcome to the varities of millets")
    var=input("do you want to buy a varities of millets?:")
    if var == "yes":
        per_kg=50
        fullname=input("enter your fullname: ")
        mobile_number=int(input("enter your number: "))
        number_of_kgs=int(input("enter number of kgs you want: "))
        total_amount=per_kg*number_of_kgs
        print(f"hi {fullname} your mobile number is {mobile_number} your amount is{total_amount} ")    
    else:
        print("thank you")        
      
            
def main():
    print("welcome to the varities")
    print("1.mango")
    print("2.banana")
    print("3.milk") 
    print("4.vegetables") 
    print("5.pulses") 
    print("6.millets")
    choose_number=int(input("enter your choice:")) 
    if choose_number==1:
        mango()
    elif choose_number==2:
        banana()
    elif choose_number==3:
        milk()
    elif choose_number==4:
        vegetables()
    elif choose_number==5:
        pulses()
    elif choose_number==6:
        millets()
    else:
        print("invalid choice")
main()  
     
       

    
    
        
