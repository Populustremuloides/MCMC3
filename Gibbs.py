from GenerateFacultyNetwork import *
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

for i in range(5):

    outputFile = "network_samples_faculty_" + str(i) + ".csv"

    print("initializing network")
    if i == 0:
        network,unobservedIndices = generateNetwork0()
    elif i == 1:
        network, unobservedIndices = generateNetwork1()
    elif i == 2:
        network, unobservedIndices = generateNetwork2()
    elif i == 3:
        network, unobservedIndices = generateNetwork3()
    elif i == 4:
        network, unobservedIndices = generateNetwork4()
    print("network initialized")

    # generate dictionary to store data
    dataDict = {}
    for index in unobservedIndices:
        dataDict[network[index].name] = []

    # generate a gazillion samples
    numSamples = 50000
    saveInterval = 10000
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