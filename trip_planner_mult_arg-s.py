
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print(" First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("France", "Germany", "Denmark")#задаю аругменти -позиційно

trip_planner("Denmark", "France", "Germany")#rewriting arguments positionally 

trip_planner (first_destination="Iceland",
final_destination="Germany",
second_destination="India")
#rewring arguments by keywards

trip_planner("Brooklyn", "Queens")
#2 arguments -new, 3rd- by default -3rd line






