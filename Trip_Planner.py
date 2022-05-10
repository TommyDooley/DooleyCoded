def trip_planner_welcome(name):
  print(f"Welcome to Trip Planner v1.0, {name}!")

trip_planner_welcome("Tommy")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(5.5)
print(estimate)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print(f"Your trip starts off in {origin}")
  print(f"And you are traveling to {destination}")
  print(f"You will be traveling by {mode_of_transport}")
  print(f"It will take approximately {str(estimated_time)} hours")

destination_setup("Joe's House", "Mama's House", estimate)