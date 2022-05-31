
#Calculate how much energy a 1 kg bomb has

bomb_mass = int(input("Bomb Mass: "))

def get_energy(mass, c=3*10**8):
  return mass*c**2

bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")
#-----------------------------------------------------------------------------------------------

#Calculate the force and work for a train

train_mass = int(input("Train Mass: "))
train_acceleration = int(input("Train Acceleration: "))
train_distance = int(input("Train Distance: "))

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print(f"The GE train supplies {train_force} Newtons of force.")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")
