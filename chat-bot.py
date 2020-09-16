from random import choice

#combine functions and conditionals to get a response from the bot
def get_bot_response(user_response):

  #add some bot responses to this list
  bot_response_peperoni = ["omg! great!", "Keep smiling!", "I love to see you happy!"]
  bot_response_hawaiian = ["im here for you", "sending good vibes"]
  bot_response_combo = ["im here for you", "sending good vibes"]

  if user_response == "peperoni":
    return choice(bot_response_peperoni)
  elif user_response == "hawaiian":
    return choice(bot_response_hawaiian)
  elif user_response == "combo":
    return choice(bot_response_combo)
  else:
    return "I hope your day gets better"


print("Welcome to Mood Bot")
print("Please enter how you are feeling")

user_response = ""
#TODO: we want to keep repeating until the user enters "done" what should we put here?
while True:
  user_response = input("How are you feeling today?: ")
  
  # Quits program when user responds with 'done'
  if user_response == 'done':
    break

  
  bot_response = get_bot_response(user_response)
  print(bot_response)
