import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get90Percent(array):
    array = np.asarray(array)
    mean = np.mean(array)
    array = np.sort(array)
    numToKeep = int(0.9 * array.shape[0])
    startIndex = int(0.05 * array.shape[0])
    lowerBound = array[startIndex]
    upperBound = array[startIndex + numToKeep]

    return mean, lowerBound, upperBound

dataDict = {"dataset":[],"numHyperParameters":[], "numSamples":[],"estimatedParameter":[],"mean":[],"lowerBound90":[],"upperBound90":[]}

outputFileName = "learned_parameters_burglary.csv"
for dataset in ["network_samples_burglary.csv"]:
    if dataset == "network_samples_burglary.csv":
        dsetMiniName = "unstable"
    else:
        dsetMiniName = "stable"

    for numHyperParameters in [0, 2, 5, 10]:
        for numSamples in [10, 100, 1000]:
            inputFileName = "network_samples_learned_burglary_" + str(numSamples) + "_" + str(
                numHyperParameters) + "_" + dsetMiniName + ".csv"

            df = pd.read_csv(inputFileName)

            # separate priors from posteriors
            priorCols = []
            posteriorCalls = []
            for col in df.columns:
                if col.startswith("Prior"):
                    priorCols.append(col)
                else:
                    posteriorCalls.append(col)

            # plot the mixing on the priors
            for col in priorCols:
                plt.plot(df[col], label=col)
            plt.legend()
            plt.title("number of observations per rv: " + str(numSamples))
            plt.show()

            # take the means and get 90% confidence intervals for the posteriors
            for col in posteriorCalls:
                mean, lowerBound, upperBound = get90Percent(df[col])
                dataDict["numSamples"].append(numSamples)
                dataDict["estimatedParameter"].append(col)
                dataDict["mean"].append(mean)
                dataDict["lowerBound90"].append(lowerBound)
                dataDict["upperBound90"].append(upperBound)

outDf = pd.DataFrame.from_dict(dataDict)
outDf.to_csv(outputFileName)