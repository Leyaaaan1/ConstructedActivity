import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Function to plot a rectangular prism
def plot_rectangular_prism(ax, width, length, height):
    # Define vertices of the rectangular prism
    vertices = [
        [0, 0, 0], [width, 0, 0], [width, length, 0], [0, length, 0],  # Bottom
        [0, 0, height], [width, 0, height], [width, length, height], [0, length, height]  # Top
    ]
    # Define the edges
    edges = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # Front face
        [vertices[1], vertices[2], vertices[6], vertices[5]],  # Right face
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # Back face
        [vertices[3], vertices[0], vertices[4], vertices[7]],  # Left face
        [vertices[4], vertices[5], vertices[6], vertices[7]],  # Top face
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # Bottom face
    ]
    ax.add_collection3d(Poly3DCollection(edges, facecolors='cyan', linewidths=1, edgecolors='black', alpha=0.5))

    # Add labels for dimensions
    ax.text(width / 2, 0, -1, f"Width = {width} cm", color="red")
    ax.text(-1, length / 2, -1, f"Length = {length} cm", color="blue")
    ax.text(-1, -1, height / 2, f"Height = {height} cm", color="green")

# Function to plot a cylinder
def plot_cylinder(ax, radius, height, segments=50):
    x = radius * np.cos(np.linspace(0, 2 * np.pi, segments))
    y = radius * np.sin(np.linspace(0, 2 * np.pi, segments))
    z = np.zeros(segments)
    ax.plot_surface(np.c_[x, x], np.c_[y, y], np.array([[0, height]]), color='magenta', alpha=0.5)

    # Add labels for dimensions
    ax.text(0, 0, height + 0.1, f"Height = {height} cm", color="green")
    ax.text(radius + 0.1, 0, 0, f"Radius = {radius} cm", color="red")

# Function to plot a sphere
def plot_sphere(ax, radius):
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(x, y, z, color='yellow', alpha=0.5)

    # Add label for radius
    ax.text(radius + 0.1, 0, 0, f"Radius = {radius} cm", color="red")

# Plot setup
fig = plt.figure(figsize=(18, 6))

# Rectangular Prism
ax1 = fig.add_subplot(131, projection='3d')
plot_rectangular_prism(ax1, width=10.37, length=10.43, height=5.27)
ax1.set_title('Rectangular Prism')
ax1.set_xlim([0, 12])
ax1.set_ylim([0, 12])
ax1.set_zlim([0, 6])

# Cylinder
ax2 = fig.add_subplot(132, projection='3d')
plot_cylinder(ax2, radius=1.5, height=0.3)
ax2.set_title('Cylinder')
ax2.set_xlim([-2, 2])
ax2.set_ylim([-2, 2])
ax2.set_zlim([0, 1])

# Sphere
ax3 = fig.add_subplot(133, projection='3d')
plot_sphere(ax3, radius=0.95)
ax3.set_title('Sphere')
ax3.set_xlim([-1.5, 1.5])
ax3.set_ylim([-1.5, 1.5])
ax3.set_zlim([-1.5, 1.5])

plt.show()
