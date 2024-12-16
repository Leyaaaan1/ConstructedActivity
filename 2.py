import matplotlib.pyplot as plt
import numpy as np

# Function to convert polar to Cartesian coordinates
def polar_to_cartesian(magnitude, angle_deg):
    angle_rad = np.radians(angle_deg)
    x = magnitude * np.cos(angle_rad)
    y = magnitude * np.sin(angle_rad)
    return x, y

# Data for vectors
vectors = [
    {"name": "A", "magnitude": 5.13, "angle": 45},  # Vector A
    {"name": "B", "magnitude": 6.33, "angle": 180},  # Vector B (West = 180°)
    {"name": "C", "magnitude": 3.94, "angle": 180 - 75},  # Vector C (75° North of West = 105°)
    {"name": "D", "magnitude": 3.3, "angle": -15},  # Vector D (15° South of East = -15°)
]

# Calculate Cartesian coordinates for each vector
positions = [(0, 0)]  # Start at the origin
for vector in vectors:
    x, y = polar_to_cartesian(vector["magnitude"], vector["angle"])
    prev_x, prev_y = positions[-1]
    positions.append((prev_x + x, prev_y + y))

# Separate x and y coordinates for plotting
x_coords, y_coords = zip(*positions)

# Plot the vectors
plt.figure(figsize=(10, 8))
plt.plot(x_coords, y_coords, marker="o", color="blue", label="Vectors")

# Annotate vectors with labels
for i, vector in enumerate(vectors):
    start_x, start_y = positions[i]
    end_x, end_y = positions[i + 1]
    plt.arrow(start_x, start_y, end_x - start_x, end_y - start_y,
              head_width=0.2, head_length=0.3, fc='blue', ec='blue', length_includes_head=True)
    label = f"Vector {vector['name']}: {vector['magnitude']} m at {vector['angle']}°"
    plt.text((start_x + end_x) / 2, (start_y + end_y) / 2, label, fontsize=10, color="red")

# Add label for the resultant vector
start_x, start_y = positions[0]
end_x, end_y = positions[-1]
plt.arrow(start_x, start_y, end_x - start_x, end_y - start_y,
          head_width=0.2, head_length=0.3, fc='green', ec='green', linestyle="dashed", length_includes_head=True)
plt.text((start_x + end_x) / 2, (start_y + end_y) / 2,
         f"Resultant R: {np.sqrt((end_x - start_x)**2 + (end_y - start_y)**2):.2f} m",
         fontsize=10, color="green")

# Add labels and grid
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(color="gray", linestyle="--", linewidth=0.5)
plt.title("Polygon Method: Vector Reconstruction")
plt.xlabel("X-Coordinate")
plt.ylabel("Y-Coordinate")
plt.legend(["Vectors", "Resultant"], loc="upper left")
plt.axis("equal")  # Ensure equal scaling for both axes
plt.show()
