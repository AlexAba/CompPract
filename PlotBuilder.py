from matplotlib import pyplot as plt

class PlotBuilder:
    def __init__(self, name = 'Plot', labelX = 'x', labelY = 'y'):
        self.name = name
        self.labelX = labelX
        self.labelY = labelY
        self.plots = []

    def AddPlot(self, x, y, label):
        self.plots.append((x, y, label))

    def Build(self):
        for plot in self.plots:
            x, y, label = plot
            plt.plot(x, y, label=label)

        plt.title(self.name)
        plt.xlabel(self.labelX)
        plt.ylabel(self.labelY)
        plt.legend()
        plt.show()