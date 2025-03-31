import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setup van de figuur en as
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# De centrale "zon" of rustpunt
sun, = ax.plot(0, 0, 'yo', markersize=12)

# Lichamen die rond de "zon" bewegen
body1, = ax.plot([], [], 'bo', markersize=8)  # Blauw lichaam
body2, = ax.plot([], [], 'go', markersize=8)  # Groen lichaam

# Posities instellen
def init():
    body1.set_data([], [])
    body2.set_data([], [])
    return body1, body2

# Animatiefunctie die de bewegingen creëert
def animate(i):
    # Parameters voor de orbitaalbeweging
    angle1 = np.radians(i)
    angle2 = np.radians(i * 1.5)  # Andere snelheid voor variatie
    
    # Posities berekenen
    x1, y1 = 5 * np.cos(angle1), 5 * np.sin(angle1)
    x2, y2 = 7 * np.cos(angle2), 7 * np.sin(angle2)
    
    body1.set_data(x1, y1)
    body2.set_data(x2, y2)
    return body1, body2

# Run de animatie
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)
plt.show()