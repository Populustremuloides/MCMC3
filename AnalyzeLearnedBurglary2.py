import pandas as pd
import matplotlib.pyplot as plt

def getName(numSamples, numHyperParams, observationDropProp):
    obsString = str(observationDropProb)
    obsString = obsString.split(".")[1][:2]
    outputFile = "network_samples_learned_burglary_" + str(numHyperParams) + "_" + str(obsString) + "_" + str(numSamples) + ".csv"
    return outputFile

def plotData(dfs, column, title, legendTitle, names):
    i = 0
    for df in dfs:
        data = df[column]
        plt.plot(data, label=str(names[i]))
        i = i + 1
    plt.legend(title=legendTitle)
    plt.title(title)
    plt.xlabel("iteration")
    plt.ylabel("parameter estimate")
    plt.show()

#
# sampleLengths = [10,50,100,200]
# dfs = []
# for numSamples in sampleLengths:
#     numHyperParams = 0
#     observationDropProb = 0.0
#     name = getName(numSamples, numHyperParams, observationDropProb)
#     df = pd.read_csv(name)
#     dfs.append(df)
#
# # plot mary
# plotData(dfs=dfs, column="PROB_maryGivenA", title="Probability of Mary given Alarm", legendTitle="# samples per node", names=sampleLengths)
# plotData(dfs=dfs, column="PROB_maryGivenNotA", title="Probability of Mary given no Alarm", legendTitle="# samples per node", names=sampleLengths)
# plotData(dfs=dfs, column="PROB_burglary", title="Probability of Burglary", legendTitle="# samples per node", names=sampleLengths)
# plotData(dfs=dfs, column="PROB_earthquake", title="Probability of Earthquake", legendTitle="# samples per node", names=sampleLengths)
#
# # Number of samples *******************************************************************************8
#
# hyperParameters = [0,5,10]
# dfs = []
# for numHyperParams in hyperParameters:
#     numSamples = 50
#     observationDropProb = 0.0
#     name = getName(numSamples, numHyperParams, observationDropProb)
#     df = pd.read_csv(name)
#     dfs.append(df)
#
# plotData(dfs=dfs, column="PROB_maryGivenA", title="Probability of Mary given Alarm", legendTitle="# hyperparameters", names=hyperParameters)
# plotData(dfs=dfs, column="PROB_maryGivenNotA", title="Probability of Mary given no Alarm", legendTitle="# hyperparameters", names=hyperParameters)
# plotData(dfs=dfs, column="PROB_burglary", title="Probability of Burglary", legendTitle="# hyperparameters", names=hyperParameters)
# plotData(dfs=dfs, column="PROB_earthquake", title="Probability of Earthquake", legendTitle="# hyperparameters", names=hyperParameters)


observationDropProbs = [0.25, 0.1, 0.0]
dfs = []
for observationDropProb in observationDropProbs:
    numSamples = 100
    numHyperParams = 0
    name = getName(numSamples, numHyperParams, observationDropProb)
    df = pd.read_csv(name)
    dfs.append(df)

plotData(dfs=dfs, column="PROB_maryGivenA", title="Probability of Mary given Alarm", legendTitle="% observation dropped", names=observationDropProbs)
plotData(dfs=dfs, column="PROB_maryGivenNotA", title="Probability of Mary given no Alarm", legendTitle="% observation dropped", names=observationDropProbs)
plotData(dfs=dfs, column="PROB_burglary", title="Probability of Burglary", legendTitle="% observation dropped", names=observationDropProbs)
plotData(dfs=dfs, column="PROB_earthquake", title="Probability of Earthquake", legendTitle="% observation dropped", names=observationDropProbs)
