#banksystem

menu=("1.Create Account",
      "2.Deposit Money",
      "3.Withdraw Money",
      "4.Check Account",
      "5.View all account",
      "6.Delete Account",
      "7.Count Accounts",
      "8.Exit"
)

accounts={}



def create_account():
    new_user_name=input("Please enter your name")
    if new_user_name in accounts:
        print("account already exist")
    else:
     new_user_name_passwd=int(input("enter your password you would like to enter."))
     
     accounts[new_user_name]={
        "balance":0,
        "passwd":new_user_name_passwd
     }

def deposit_money():
   user=input("enter your user name")
   if user in accounts:
      money_deposit=int(input('enter the money you would like to deposit'))
      accounts[user]["balance"] += money_deposit
      bal=accounts[user]["balance"]
      print(f"your new balance after depositing {money_deposit} is  {bal}.")
     
   else:
      print("your account is not in the bank")

def money_withdraw():
   user_withdraw=input("enter your user name")
   user_passwd=int(input("enter your password"))
   if user_withdraw in accounts and user_passwd==accounts[user_withdraw]['passwd'] and accounts[user_withdraw]["balance"]>=0:
      money_withdraw=int(input('enter the amount of money you would like to withdraw'))and money_withdraw !=0
      accounts[user_withdraw]["balance"]-=money_withdraw
      bal2=accounts[user_withdraw]["balance"]

   elif user_withdraw in accounts and user_passwd==accounts[user_withdraw]['passwd'] and accounts[user_withdraw]["balance"]<=0:
    print("your account does not have that much money.")

   elif user_withdraw in accounts and  not user_passwd==accounts[user_withdraw]['passwd'] and accounts[user_withdraw]["balance"]>=0:
    print('incorrect password')

   else:
     print("you don't have account in the bank or incorrect password.")


def check_account():
   user_check=input('enter your name')
   user_passwd_check=int(input("enter your password"))
   if user_check in accounts and user_passwd_check==accounts[user_check]["passwd"]:
      print(user_check)
      print[user_check]['balance']
      print('you are a valid user')

def delete_account():
   delete_user=input("enter the name of account you want to delete")
   del_passwd=int(input('enter the password of the account you are deleting'))
   if delete_user in accounts and del_passwd==accounts[delete_user]['passwd']:
      del accounts[delete_user]
      print("account deleted successfully.")

      






