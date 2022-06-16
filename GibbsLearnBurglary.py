from GenerateLearningBurglaryNetwork import *
import pandas as pd
from tqdm import tqdm

def recordSamples(dataDict, network, unobservedIndices):
    '''
    # only sample from unobserved nodes
    # record the states of all the unobserved nodes
    '''

    for index in unobservedIndices:
        name = network[index].name
        state = network[index].state
        dataDict[name].append(state)
    return dataDict


for dataset in ["network_samples_burglary.csv"]:
    if dataset == "network_samples_burglary.csv":
        dsetMiniName = "unstable"
    else:
        dsetMiniName = "stable"

    for numHyperParameters in [0,2,5,10]:
        for numSamples in [10, 100, 1000]:
            outputFile = "network_samples_learned_burglary_" + str(numSamples) + "_" + str(numHyperParameters) + "_" + dsetMiniName + ".csv"

            print("initializing network")
            network, unobservedIndices = generateNetwork(numSamples=numSamples, numHyperParameters=numHyperParameters, dataset=dataset)
            print("network initialized")

            # generate dictionary to store data
            dataDict = {}
            for index in unobservedIndices:
                dataDict[network[index].name] = []

            # generate a gazillion samples
            numSamples = 100000
            saveInterval = 50000
            loop = tqdm(total=numSamples)
            for i in range(numSamples):
                for index in unobservedIndices:
                    node = network[index]
                    node.sample()
                dataDict = recordSamples(dataDict, network, unobservedIndices)

                if i % 100 == 0:
                    loop.update(100)

                if i % saveInterval == 0:
                    outDF = pd.DataFrame.from_dict(dataDict)
                    outDF.to_csv(outputFile, index=False)

            outDF = pd.DataFrame.from_dict(dataDict)
            outDF.to_csv(outputFile, index=False)
