__doc__ = "My main function"

import argparse
import matplotlib.pyplot as plt

# Definition of braking simulation function
def braking_sim(m, u, ts, v0):
    # Define required data
    g = 9.81
    a = -g * u
    time_step = ts
    t = 0.0
    s = 0.0
    v = v0
    distance = []
    velocity = []
    time = []

    # Calculation and creation of data arrays
    while v > 0.0:
        s = s + v * time_step
        distance.append(s)
        v = v + a * time_step
        velocity.append(v)
        t = t + time_step
        time.append(t)

    return distance, velocity, time

def main():
    parser = argparse.ArgumentParser(description='Braking Simulation')
    parser.add_argument('--mass', type=int, help='Vehicle mass', required=True)
    parser.add_argument('--initial_speed', type=int, help='Initial speed', required=True)
    args = parser.parse_args()

    m = args.mass
    v0 = args.initial_speed
    u_values = [0.65, 0.4, 0.2]

    fig, (graph1, graph2) = plt.subplots(2, 1, figsize=(10, 8))

    for u in u_values:
        distance, velocity, time = braking_sim(m, u, 0.1, v0)

        graph1.plot(time, velocity, label=f'u = {u}')
        graph2.plot(time, distance, label=f'u = {u}')

    graph1.set_xlabel('Time (s)')
    graph1.set_ylabel('Velocity (m/s)')
    graph1.set_title('Velocity decrease (dry, wet, icy)')
    graph1.legend()

    graph2.set_xlabel('Time (s)')
    graph2.set_ylabel('Distance (m)')
    graph2.set_title('Braking distance (dry, wet, icy)')
    graph2.legend()

    plt.show()

if __name__ == "__main__":
    main()
