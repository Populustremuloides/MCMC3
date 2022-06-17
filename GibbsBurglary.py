from GenerateBurglaryNetwork import *
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


outputFile = "network_samples_burglary_newProbs.csv"

print("initializing network")
network, unobservedIndices = generateNetwork()
print("network initialized")

# generate dictionary to store data
dataDict = {}
for index in unobservedIndices:
    dataDict[network[index].name] = []

# generate a gazillion samples
numSamples = 500000
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