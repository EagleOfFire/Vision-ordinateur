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

    point = (4, 3, 2)
    translate = translate_point(point, 0, 1, 1)
    plt.plot(point[0], point[1], point[2], marker='x', color='green')
    plt.plot(translate[0], translate[1], translate[2], marker='x', color='red')

    plt.plot([point[0], translate[0]], [point[1], translate[1]], [point[2], translate[2]], color='black',
             linestyle='dashed')
    plt.show()


def translate_point(point: tuple, alpha: int, beta: int, gamma: int):
    return point[0] + alpha, point[1] + beta, point[2] + gamma


if __name__ == "__main__":
    main()
