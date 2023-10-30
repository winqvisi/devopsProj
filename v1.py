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

# Main program
while True:
  username = input("Enter username: ")
  password = input("Enter password: ")
  user = login(username, password)
  if user:
    print(f"user {username}")
    display_account_info(user)
  else:
    print("invalid username or password")
