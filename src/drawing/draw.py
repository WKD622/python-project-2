import matplotlib.pyplot as plt
import src.common as cm
from matplotlib import pylab
from matplotlib.patches import Polygon


class Draw:
    fig = None
    ax = None

    def preparation(self, width, height, bg_colour):
        """
        Prepares axes and background for drawing.
        :param width:
        :param height:
        :param bg_colour:
        :return:
        """
        self.fig, self.ax = plt.subplots()
        plt.axis([0, width, 0, height])
        self.ax.set_facecolor(bg_colour)
        self.ax.set_yticklabels([])
        self.ax.set_xticklabels([])
        print("Preparation ends successfully.")

    def circle(self, x, y, radius, colour):
        """
        Adds circle to queue of elements to draw.
        :param x:
        :param y:
        :param radius:
        :param colour:
        :return:
        """
        self.ax.add_artist(plt.Circle((x, y,), radius, color=colour))
        print("Circle created successfully.")

    def square(self, x, y, size, colour):
        """
        Adds square to queue of elements to draw.
        :param x:
        :param y:
        :param size:
        :param colour:
        :return:
        """
        size = size / 2
        self.ax.fill([x - size, x + size, x + size, x - size],
                     [y + size, y + size, y - size, y - size],
                     color=colour)
        print("Square created successfully.")

    def rectangle(self, x, y, width, height, colour):
        """
        Adds rectangle to queue of elements to draw.
        :param x:
        :param y:
        :param width:
        :param height:
        :param colour:
        :return:
        """
        width = width / 2
        height = height / 2
        self.ax.fill([x - width, x + width, x + width, x - width],
                     [y + height, y + height, y - height, y - height],
                     colour)
        print("Rectangle created successfully.")

    def point(self, x_list, y_list, colour):
        """
        Adds point to queue of elements to draw.
        :param x_list:
        :param y_list:
        :param colour:
        :return:
        """
        plt.plot(x_list, y_list, 'ro', color=colour)
        print("Point created successfully.")

    def polygon(self, points_list, colour):
        """
        Adds polygon to queue of elements to draw.
        :param points_list:
        :param colour:
        :return:
        """
        self.ax.add_artist(Polygon(points_list, color=colour))
        print("Polygon created successfully.")

    def end(self):
        """
        Draws all figures from queue.
        :return:
        """
        print(cm.FILE_NAME)
        if cm.FILE_NAME is not None:
            plt.savefig('../out/{}.png'.format(cm.FILE_NAME))
        plt.show()
