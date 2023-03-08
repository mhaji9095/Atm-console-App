from cardHolder import cardHolder

def print_menu():
    ### Print options to the user
    print("Please choose from one of the following options...")
    print("1. deposit")
    print("2. withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
        deposit = float(input("how much $$ would like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank you for your @@. Your new balance is: ", str(cardHolder.get_balance()))
        
    except:
        print("Invalid input")

def withdraw(cardHolder):
    try:
        withdraw = float(input("How much $$ would like to deposit: "))
        ### Check if user has enough money
        if(cardHolder.get_balance() < withdraw):
            print("Insufficient balacne :(")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("You are good to go! Thank You :)")
    except:
        print("Invalid Input")
    
def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())

if __name__ == "__main":
    current_user = cardHolder("","","","","",)

    ### Create a repo of cardHolders
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("1245690876312345", 1234, "John" , "Salley", 120,31 ))
    list_of_cardHolders.append(cardHolder("8920345897162345", 1234, "Mannie" , "Salley", 120,31 ))
    list_of_cardHolders.append(cardHolder("0987689098912645", 1454, "John" , "Wall", 550,61 ))
    list_of_cardHolders.append(cardHolder("0385748572987643", 1424, "Kobe" , "Salley", 220,33 ))
    list_of_cardHolders.append(cardHolder("9018465387612348", 1534, "Lamarcus" , "Salley", 990,31 ))

    ### Prompt user for debit card numer
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            ### Check against repo 
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            current_user = debitMatch[0]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break 
            else:
                print("Card number not recgonnized. Please try again.")
        except:
            print("Card number not recongized. Please try again.")
    
### Prompt for Pin
while True:
    try:
        userPin = int(input("Please enter your pin:").strip())
        if(current_user.get_pin() == userPin):
            break
        else:
            print("invalid PIN. Please try again.")
    except:
        print("Invalid PIn. Please try again.")
### Print options
print("Welcome ", current_user .get_firstname(), " :)")
option = 0
while (option !=4):
    print_menu()
    try:
        option = int(input())
    except:
        print("Invalid Input. Please try again.")

    if(option ==1):
        deposit(current_user)
    elif(option == 2):
        withdraw(current_user)
    elif(option == 3):
        break 
    else:
        oprion = 0

print("Thank you, Hsve a nice day :)")




    
    
