from random import choice

#combine functions and conditionals to get a response from the bot
def get_bot_response(user_response):

  #add some bot responses to this list
  bot_response_peperoni = ["Cool, that will be $9.95.", "Awesome. We’ll send it right over.", "Ok, I’ll add that to the list. "]
  bot_response_hawaiian = ["Alright, that is $8.89.", "That will be $8.89.", "Cool. Would you like this order delivered?"]
  bot_response_combo = ["That will be $12.99.", "Awesome. It will be ready in 10 minutes.", "Would you like a drink with that?"]

  if user_response == "peperoni":
    return choice(bot_response_peperoni)
  elif user_response == "hawaiian":
    return choice(bot_response_hawaiian)
  elif user_response == "combo":
    return choice(bot_response_combo)
  else:
    return "Sorry, we don't sell that."


print("Welcome to Moe’s Pizza! ")

user_response = ""
#TODO: we want to keep repeating until the user enters "done" what should we put here?
while True:
  user_response = input("What would you like to order?  ")
  
  # Quits program when user responds with 'done'
  if user_response == 'done':
    break

  
  bot_response = get_bot_response(user_response)
  print(bot_response)