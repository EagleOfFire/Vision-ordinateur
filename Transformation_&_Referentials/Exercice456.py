import math

import matplotlib.pyplot as plt


def main():
    # Initialize a new Plotting window
    plt.figure(figsize=(10, 10))
    # Initializing 3D capabilities
    axes = plt.axes(projection="3d", proj_type='ortho')
    # Setting axis properties
    axes.set_xlim(-10, 10)  # X Axis graduation
    axes.set_ylim(-10, 10)  # Y Axis graduation
    axes.set_zlim(-10, 10)  # Z Axis graduation
    axes.set_xlabel('X')  # X Axis label
    axes.set_ylabel('Y')  # Y Axis label
    axes.set_zlabel('Z')  # Z Axis label
    axes.xaxis.label.set_color('red')  # X Axis color
    axes.yaxis.label.set_color('green')  # Y Axis color
    axes.zaxis.label.set_color('blue')  # Z Axis color
    axes.tick_params(axis='x', colors='red')  # X Axis graduation color
    axes.tick_params(axis='y', colors='green')  # Y Axis graduation color
    axes.tick_params(axis='z', colors='blue')  # Z Axis graduation color
    # Display the 3D plotting window
    plt.plot([0, 10], [0, 0], [0, 0], color='red', linestyle='solid')
    plt.plot([0, -10], [0, 0], [0, 0], color='red', linestyle='dashed')
    plt.plot([0, 0], [0, 10], [0, 0], color='green', linestyle='solid')
    plt.plot([0, 0], [0, -10], [0, 0], color='green', linestyle='dashed')
    plt.plot([0, 0], [0, 0], [0, 10], color='blue', linestyle='solid')
    plt.plot([0, 0], [0, 0], [0, -10], color='blue', linestyle='dashed')
    plt.plot(4, 4, 4, marker='o', color='black')
    rotationX = rot_x_point((4, 4, 4), math.pi / 4)
    rotationY = rot_y_point((4, 4, 4), math.pi / 4)
    rotationZ = rot_z_point((4, 4, 4), math.pi / 4)
    plt.plot(rotationX[0], rotationX[1], rotationX[2], marker='o', color='red')
    plt.plot(rotationY[0], rotationY[1], rotationY[2], marker='o', color='green')
    plt.plot(rotationZ[0], rotationZ[1], rotationZ[2], marker='o', color='blue')
    plt.show()


def rot_x_point(point: tuple, omega: float):
    x = point[0]
    y = (point[1] * math.cos(omega)) - (point[2] * math.sin(omega))
    z = (point[1] * math.sin(omega)) + (point[2] * math.cos(omega))
    return x, y, z


def rot_y_point(point: tuple, omega: float):
    x = (point[0] * math.cos(omega)) + (point[2] * math.sin(omega))
    y = point[1]
    z = (point[2] * math.cos(omega)) - (point[0] * math.sin(omega))
    return x, y, z


def rot_z_point(point: tuple, omega: float):
    x = (point[0] * math.cos(omega)) - (point[1] * math.sin(omega))
    y = (point[0] * math.sin(omega)) + (point[1] * math.cos(omega))
    z = point[2]
    return x, y, z


def rot_point(point: tuple, omega: float, phi, kappa):
    return


if __name__ == "__main__":
    main()
