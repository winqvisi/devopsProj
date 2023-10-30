class User:
  def __init__(self, username, password, accounts):
    self.username = username
    self.password = password
    self.accounts = accounts

class Account:
  def __init__(self, account_number, balance):
    self.account_number = account_number
    self.balance = balance

users = [
  User("user1", "password1", [Account("1234", 1000.0)]),
  User("user2", "password2", [Account("5678", 500.0)])
]

def login(username, password):
  for user in users:
    if user.username == username and user.password == password:
      return user
  return None

def display_account_info(user):
  for account in user.accounts:
    print(f"Account number: {account.account_number}")
    print(f"Balance: {account.balance:.2f}")

def change_password(user, new_password):
  user.password = new_password
  print("Password changed successfully.")

def create_account(user, account_number, initial_balance):
  user.accounts.append(Account(account_number, initial_balance))
  print(f"New account with Account Number {account_number} has been created.")

def transfer_balance(user, source_account_number, target_account_number, amount):
  source_account = None
  target_account = None

  for account in user.accounts:
    if account.account_number == source_account_number:
      source_account = account
    if account.account_number == target_account_number:
      target_account = account

  if source_account and target_account and source_account.balance >= amount:
    source_account.balance -= amount
    target_account.balance += amount
    print(f"Transfer successful. {amount:.2f} transferred to {target_account_number}.")
  else:
    print("Insufficient balance or invalid account number.")

# Main program
while True:
  username = input("Enter username: ")
  password = input("Enter password: ")
  user = login(username, password)
  if user:
    print(f"Welcome {username}")
    display_account_info(user)

    action = input("1. Create new account\n2. Transfer balance\n3. Change password\n4. Exit\nEnter your choice (1/2/3/4): ")
    
    if action == "1":
      account_number = input("Enter new account number: ")
      initial_balance = float(input("Enter initial balance: "))
      create_account(user, account_number, initial_balance)
    elif action == "2":
      source_account_number = input("Enter source account number: ")
      target_account_number = input("Enter target account number: ")
      amount = float(input("Enter amount to transfer: "))
      transfer_balance(user, source_account_number, target_account_number, amount)
    elif action == "3":
      new_password = input("Enter your new password: ")
      change_password(user, new_password)
    elif action == "4":
      break
    else:
      print("Invalid choice. Try again.")
  else:
    print("Invalid username or password. Try again.")
