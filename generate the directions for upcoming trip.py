#Task - create a program that allows our users to generate the directions for their upcoming trip!

def generate_trip_instructions(location): #location -  це параметр,який буде заповнено аргументом
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location) #після get to має бути пробуск,а тоді закриття лапок, бо текст зіллється
  
generate_trip_instructions("Central Park") # central park - це аргумент. ним заповнюється параметр

generate_trip_instructions("Grand Central Station")
