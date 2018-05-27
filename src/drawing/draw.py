import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


class Draw:
    fig = None
    ax = None

    def preparation(self, width, height, bg_colour):
        self.fig, self.ax = plt.subplots()
        plt.axis([0, width, 0, height])
        self.ax.set_facecolor(bg_colour)
        self.ax.set_yticklabels([])
        self.ax.set_xticklabels([])
        print("Preparation end succesfully.")

    def circle(self, x, y, radius, colour):
        self.ax.add_artist(plt.Circle((x, y,), radius, color=colour))
        print("Circle created succesfully.")

    def square(self, x, y, size, colour):
        size = size / 2
        self.ax.fill([x - size, x + size, x + size, x - size],
                     [y + size, y + size, y - size, y - size],
                     color=colour)
        print("Square created succesfully.")

    def rectangle(self, x, y, width, height, colour):
        width = width / 2
        height = height / 2
        self.ax.fill([x - width, x + width, x + width, x - width],
                     [y + height, y + height, y - height, y - height],
                     colour)
        print("Rectangle created succesfully.")

    def points(self, x_list, y_list, colour):
        plt.plot(x_list, y_list, 'ro', color=colour)
        print("Points created succesfully.")

    def polygon(self, points_list, colour):
        self.ax.add_artist(Polygon(points_list, color=colour))
        print("Polygon created succesfully.")

    def end(self):
        plt.show()
