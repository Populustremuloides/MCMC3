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

def generateData(numHyperParams, observationDropProb, numSamples, data, dataSource=""):
    obsString = str(observationDropProb)
    obsString = obsString.split(".")[1][:2]
    outputFile = "network_samples_learned_burglary_" + str(numHyperParams) + "_" + str(obsString) + "_" + str(numSamples) + "_" + dataSource + ".csv"

    print("initializing network")
    network, unobservedIndices = generateNetwork(numHyperParams=numHyperParams,
                                                 observationDropProb=observationDropProb, numSamples=numSamples,
                                                 data=data)
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
            if node.name == "uninitialized node":
                print("stop here")
            node.sample()
        dataDict = recordSamples(dataDict, network, unobservedIndices)

        if i % 100 == 0:
            loop.update(100)

        if i % saveInterval == 0:
            outDF = pd.DataFrame.from_dict(dataDict)
            outDF.to_csv(outputFile, index=False)

    outDF = pd.DataFrame.from_dict(dataDict)
    outDF.to_csv(outputFile, index=False)

# various tests for different scenarios

# # number of samples
# print()
# print("testing number of samples ***************8")
# print()
# for numSamples in [10,50,100,200]:
#     numHyperParams = 0
#     observationDropProb = 0.0
#     data = "network_samples_burglary_newProbs.csv"
#     generateData(numHyperParams, observationDropProb, numSamples, data)

# number of hyper parameters
# print()
# print("testing number of hyper parameters ***************8")
# print()
# for numHyperParams in [0]:#, 5, 10]:
#     numSamples = 50
#     observationDropProb = 0.0
#     data = "network_samples_burglary_newProbs.csv"
#     generateData(numHyperParams, observationDropProb, numSamples, data)

# print()
# print("testing number of obsevations to drop ***************8")
# print()
# for observationDropProb in [0., 0.1,0.25]:
#     numHyperParams = 0
#     numSamples = 100
#     data = "network_samples_burglary_newProbs.csv"
#     generateData(numHyperParams, observationDropProb, numSamples, data)

print()
print("testing datasets ***************8")
print()
i = 0
for data in ["network_samples_burglary_newProbs.csv", "network_samples_burglary_oldProbs.csv"]:
    numHyperParams = 0
    observationDropProb = 0.0
    numSamples = 100
    if i == 0:
        generateData(numHyperParams, observationDropProb, numSamples, data, dataSource="updated")
    else:
        generateData(numHyperParams, observationDropProb, numSamples, data, dataSource="old_sparse")