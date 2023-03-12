"""
    Simulate a free falling object onto the surface of a neutron star
"""
# Lander: one that lands (especially: a space vehicle that is designed to land on a celestial body)
class Lander:
    def __init__(self, position: float, velocity: float, acceleration: float) -> None:
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        return;

def main() -> None:
    # Declare some relevant constants
    MSUN: float = 1.9891E30
    KM: float = 1e+3
    MILLISEC: float = 1e-3
    G: float = 6.67384e-11

    # Define physical properties of neutron star
    ns_mass = 2 * MSUN
    ns_radius = 12 * KM 

    # Define lander object
    pos: float = 10*ns_radius  # Initialize position at 120 km above surface 
    acc: float = (-G*ns_mass)/(pos**2)
    lander = Lander(position=pos, velocity=0.0, acceleration=acc)

    # Simulation config
    time_step: float = 5e-6
    time: float = 0.0
    istep: int = 0

    # Write data to file
    with open("out.data", "w") as outFile:
        print("pos = %4.3e vel = %4.3e acc = %4.3e\n" % \
            (lander.position / ns_radius, lander.velocity, lander.acceleration)
        )

        while (abs(lander.position) > ns_radius) and (istep < 1000):
            lander.acceleration = - G * ns_mass / (lander.position ** 2)
            lander.velocity += lander.acceleration * time_step
            lander.position += lander.velocity * time_step 
            time += time_step
            istep += 1

            print("time = %3.2e (ms), pos = %3.2e (R), vel = %3.2e (m/s), acc = %3.2e (m/s^2)\n" % \
                (time / MILLISEC, lander.position / ns_radius, lander.velocity, lander.acceleration)
            )

            outFile.write("{:.2e} {:.2e} {:.2e} {:.2e}\n".format(time / MILLISEC,
                                                             lander.position / ns_radius,
                                                             lander.velocity,
                                                             lander.acceleration
                                                             )
            )

    return None 


if __name__ == "__main__":
    main()