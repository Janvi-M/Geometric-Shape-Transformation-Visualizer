import numpy as np
import matplotlib.pyplot as plt

# Define a function to plot the shape
def plot_shapes(points_list, titles_list):
    plt.figure(figsize=(8, 6))
    for i, points in enumerate(points_list):
        plt.plot(points[:, 0], points[:, 1], label=titles_list[i])
    plt.xlabel('X-axis', fontsize=12)
    plt.ylabel('Y-axis', fontsize=12)
    plt.title(titles_list[0], fontsize=14)
    plt.grid(True, linestyle='-', linewidth=0.5)
    plt.gca().spines['bottom'].set_linewidth(2)  # Set x-axis linewidth
    plt.gca().spines['left'].set_linewidth(2)  # Set y-axis linewidth
    plt.legend(fontsize=10)
    plt.show()

# Define a function to rotate a shape
def rotate_shape(points, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                 [np.sin(theta), np.cos(theta)]])
    rotated_points = np.dot(points, rotation_matrix)
    return rotated_points

# Define a function to scale a shape
def scale_shape(points, scale_factor):
    scaling_matrix = np.array([[scale_factor, 0],
                                [0, scale_factor]])
    scaled_points = np.dot(points, scaling_matrix)
    return scaled_points

# Define a function to reflect a shape along the x-axis
def reflect_x_axis(points):
    reflection_matrix = np.array([[1, 0],
                                   [0, -1]])
    reflected_points = np.dot(points, reflection_matrix)
    return reflected_points

# Define a function to reflect a shape along the y-axis
def reflect_y_axis(points):
    reflection_matrix = np.array([[-1, 0],
                                   [0, 1]])
    reflected_points = np.dot(points, reflection_matrix)
    return reflected_points

# Original shape
original_points = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])

# List to hold points and titles for each transformation
points_list = [original_points]
titles_list = ["Original Shape"]

# Input rotation angle from user
rotation_angle = float(input("Enter rotation angle in degrees: "))

# Rotation
rotated_points = rotate_shape(original_points, rotation_angle)
points_list.append(rotated_points)
titles_list.append(f"Rotated Shape ({rotation_angle} degrees)")

# Input scale factor from user
scale_factor = float(input("Enter scale factor: "))

# Scaling
scaled_points = scale_shape(original_points, scale_factor)
points_list.append(scaled_points)
titles_list.append(f"Scaled Shape (Factor of {scale_factor})")

# Reflection along x-axis
reflected_x_points = reflect_x_axis(original_points)
points_list.append(reflected_x_points)
titles_list.append("Reflected Shape along x-axis")

# Reflection along y-axis
reflected_y_points = reflect_y_axis(original_points)
points_list.append(reflected_y_points)
titles_list.append("Reflected Shape along y-axis")

# Plot all shapes
plot_shapes(points_list, titles_list)
