import simpy
import random


# Define the car wash environment
class CarWash:
    def __init__(self, env, num_servers):
        self.env = env
        self.server = simpy.Resource(env, capacity=num_servers)

    def wash_car(self, car):
        yield self.env.timeout(random.uniform(5, 15))  # Time it takes to wash a car


# Define the car arrival process
def car_arrival(env, car_id, carwash):
    print(f"Car {car_id} arrives at time {env.now}")

    with carwash.server.request() as request:
        yield request  # Request a server
        print(f"Car {car_id} enters the car wash at time {env.now}")
        yield env.process(carwash.wash_car(car_id))  # Simulate car wash
        print(f"Car {car_id} leaves the car wash at time {env.now}")


# Simulation function
def simulate_car_wash(env, num_servers, sim_time):
    carwash = CarWash(env, num_servers)
    car_id = 0

    while env.now < sim_time:
        car_id += 1
        env.process(car_arrival(env, car_id, carwash))
        interarrival_time = random.expovariate(1.0 / 10)  # Random car arrival rate
        yield env.timeout(interarrival_time)


# Run the simulation
env = simpy.Environment()
env.process(simulate_car_wash(env, num_servers=8, sim_time=100))
env.run()
