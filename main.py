from PlotBuilder import PlotBuilder
from Conductivity import Conductivity
import numpy
from constants.Ge import Ge
from constants.InSb import InSb

#   Constants
L = 1e-6
T = 300
r = 2

def main():
    #   Init the range of plots
    nf = numpy.arange(-5, 5, 0.1)
    GeConductivity = Conductivity(Ge, T, L, r)
    InSbConductivity = Conductivity(InSb, T, L, r)

    GeBallistic = GeConductivity.Ballistic(nf)
    GeDifussion = GeConductivity.Difussion(nf)
    
    InSbBallistic = InSbConductivity.Ballistic(nf)
    InSbDifussion = InSbConductivity.Difussion(nf)

    plotBuilder = PlotBuilder(Ge.id + ' conductivity', 'Muf', 'G, S')
    plotBuilder.AddPlot(nf, GeBallistic, "Ballistic")
    plotBuilder.AddPlot(nf, GeDifussion, "Difussion")
    plotBuilder.Build()

    plotBuilder = PlotBuilder(InSb.id + ' conductivity', 'Muf', 'G, S')
    plotBuilder.AddPlot(nf, InSbBallistic, "Ballistic")
    plotBuilder.AddPlot(nf, InSbDifussion, "Difussion")
    plotBuilder.Build()

main()