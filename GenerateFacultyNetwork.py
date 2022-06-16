from Nodes import *

priorNormalMean = 5
priorNormalVar = 1
priorGammaShape = 5
priorGammaScale = 2
sampleVariance = 0.3

def getParentState(parentNode): # by default, parentNode must be a list (in this case of length 1)
    return parentNode[0].state


def generateNetwork0():

    # set up prior nodes and posterior nodes for mean
    posteriorMu = NormalNode(mu=priorNormalMean, sigma=priorNormalVar, name="posteriorMu", sampleVariance=sampleVariance)

    # set up prior nodes and posterior nodes for variance
    posteriorSigma = GammaNode(shape=priorGammaShape, scale=priorGammaScale, gType="logInverse", name="posteriorSigma", sampleVariance=sampleVariance)

    # save to the network
    network = [posteriorMu, posteriorSigma]
    unobservedIndices = np.arange(0, len(network))

    # add the observations
    obs = []
    with open("faculty_dat.csv", "r+") as data:
        i = 1
        children = []
        for line in data:
            line = line.replace("\n","")
            observation = float(line)
            obs.append(observation)
            posteriorMuLinker = LinkerNode([posteriorMu], getParentState)
            posteriorSigmaLinker = LinkerNode([posteriorSigma], getParentState)
            obsNode = NormalNode(mu=posteriorMuLinker, sigma=posteriorSigmaLinker, name=str(i))
            obsNode.setObservation(observation)
            obsNode.initialize([])
            children.append(obsNode)
            i = i + 1

    print("mean observation: ", np.mean(obs))
    print("var observation: ", np.var(obs))
    #
    # add children
    network[0].initialize(children)
    network[1].initialize(children)

    network = network + children

    return network, unobservedIndices


def generateNetwork1():

    # set up prior nodes and posterior nodes for mean
    priorMuMu = NormalNode(mu=priorNormalMean, sigma=priorNormalVar, name="priorMeanMu", sampleVariance=sampleVariance)
    priorMuMuLinker = LinkerNode([priorMuMu], getParentState)
    posteriorMu = NormalNode(mu=priorMuMuLinker, sigma=priorNormalVar, name="posteriorMu", sampleVariance=sampleVariance)
    # priorMuMu.state = 5
    # posteriorMu.state = 5

    # attach children
    priorMuMu.initialize([posteriorMu])

    # set up prior nodes and posterior nodes for variance
    posteriorSigma = GammaNode(shape=priorGammaShape, scale=priorGammaScale, gType="logInverse", name="posteriorSigma", sampleVariance=sampleVariance)

    # save to the network
    network = [priorMuMu, posteriorMu, posteriorSigma]
    unobservedIndices = np.arange(0, len(network))

    # add the observations
    obs = []
    with open("faculty_dat.csv", "r+") as data:
        i = 1
        children = []
        for line in data:
            line = line.replace("\n","")
            observation = float(line)
            obs.append(observation)
            posteriorMuLinker = LinkerNode([posteriorMu], getParentState)
            posteriorSigmaLinker = LinkerNode([posteriorSigma], getParentState)
            obsNode = NormalNode(mu=posteriorMuLinker, sigma=posteriorSigmaLinker, name=str(i))
            obsNode.setObservation(observation)
            obsNode.initialize([])
            children.append(obsNode)
            i = i + 1

    print("mean observation: ", np.mean(obs))
    print("var observation: ", np.var(obs))

    # add children
    network[1].initialize(children)
    network[2].initialize(children)

    network = network + children

    return network, unobservedIndices

def generateNetwork2():

    # set up prior nodes and posterior nodes for mean
    priorMuMu = NormalNode(mu=priorNormalMean, sigma=priorNormalVar, name="priorMeanMu", sampleVariance=sampleVariance)
    priorMuSigma = GammaNode(shape=priorGammaShape,scale=priorGammaScale, gType="logInverse", name="priorMeanSigma", sampleVariance=sampleVariance)
    priorMuMuLinker = LinkerNode([priorMuMu], getParentState)
    priorMuSigmaLinker = LinkerNode([priorMuSigma], getParentState)
    posteriorMu = NormalNode(mu=priorMuMuLinker, sigma=priorMuSigmaLinker, name="posteriorMu", sampleVariance=sampleVariance)
    # priorMuMu.state = 5
    # posteriorMu.state = 5

    # attach children
    priorMuMu.initialize([posteriorMu])
    priorMuSigma.initialize([posteriorMu])

    # set up prior nodes and posterior nodes for variance
    posteriorSigma = GammaNode(shape=priorGammaShape, scale=priorGammaScale, gType="logInverse", name="posteriorSigma", sampleVariance=sampleVariance)

    # save to the network
    network = [priorMuMu, priorMuSigma, posteriorMu, posteriorSigma]
    unobservedIndices = np.arange(0, len(network))

    # add the observations
    obs = []
    with open("faculty_dat.csv", "r+") as data:
        i = 1
        children = []
        for line in data:
            line = line.replace("\n","")
            observation = float(line)
            obs.append(observation)
            posteriorMuLinker = LinkerNode([posteriorMu], getParentState)
            posteriorSigmaLinker = LinkerNode([posteriorSigma], getParentState)
            obsNode = NormalNode(mu=posteriorMuLinker, sigma=posteriorSigmaLinker, name=str(i))
            obsNode.setObservation(observation)
            obsNode.initialize([])
            children.append(obsNode)
            i = i + 1

    print("mean observation: ", np.mean(obs))
    print("var observation: ", np.var(obs))

    # add children
    network[-1].initialize(children)
    network[-2].initialize(children)

    network = network + children

    return network, unobservedIndices

def generateNetwork3():

    # set up prior nodes and posterior nodes for mean
    priorMuMu = NormalNode(mu=priorNormalMean, sigma=priorNormalVar, name="priorMeanMu", sampleVariance=sampleVariance)
    priorMuSigma = GammaNode(shape=priorGammaShape,scale=priorGammaScale, gType="logInverse", name="priorMeanSigma", sampleVariance=sampleVariance)
    priorMuMuLinker = LinkerNode([priorMuMu], getParentState)
    priorMuSigmaLinker = LinkerNode([priorMuSigma], getParentState)
    posteriorMu = NormalNode(mu=priorMuMuLinker, sigma=priorMuSigmaLinker, name="posteriorMu", sampleVariance=sampleVariance)
    # attach children
    priorMuMu.initialize([posteriorMu])
    priorMuSigma.initialize([posteriorMu])

    # set up prior nodes and posterior nodes for variance
    priorSigmaShape = GammaNode(shape=priorGammaShape, scale=priorGammaScale, gType="logInverse", name="priorSigmaShape", sampleVariance=sampleVariance)
    priorSigmaShapeLinker = LinkerNode([priorSigmaShape], getParentState)
    posteriorSigma = GammaNode(shape=priorSigmaShapeLinker, scale=priorGammaScale, gType="logInverse", name="posteriorSigma", sampleVariance=sampleVariance)
    # attach children
    priorSigmaShape.initialize([posteriorSigma])

    # save to the network
    network = [priorMuMu, priorMuSigma,posteriorMu, priorSigmaShape, posteriorSigma]
    unobservedIndices = np.arange(0, len(network))

    # add the observations
    obs = []
    with open("faculty_dat.csv", "r+") as data:
        i = 1
        children = []
        for line in data:
            line = line.replace("\n","")
            observation = float(line)
            obs.append(observation)
            posteriorMuLinker = LinkerNode([posteriorMu], getParentState)
            posteriorSigmaLinker = LinkerNode([posteriorSigma], getParentState)
            obsNode = NormalNode(mu=posteriorMuLinker, sigma=posteriorSigmaLinker, name=str(i))
            obsNode.setObservation(observation)
            obsNode.initialize([])
            children.append(obsNode)
            i = i + 1

    print("mean observation: ", np.mean(obs))
    print("var observation: ", np.var(obs))

    # add children
    network[2].initialize(children)
    network[2].initialize(children)

    network = network + children

    return network, unobservedIndices




# full version:

def generateNetwork4():

    # set up prior nodes and posterior nodes for mean
    priorMuMu = NormalNode(mu=priorNormalMean, sigma=priorNormalVar, name="priorMeanMu", sampleVariance=sampleVariance)
    priorMuSigma = GammaNode(shape=priorGammaShape,scale=priorGammaScale, gType="logInverse", name="priorMeanSigma", sampleVariance=sampleVariance)
    priorMuMuLinker = LinkerNode([priorMuMu], getParentState)
    priorMuSigmaLinker = LinkerNode([priorMuSigma], getParentState)
    posteriorMu = NormalNode(mu=priorMuMuLinker, sigma=priorMuSigmaLinker, name="posteriorMu", sampleVariance=sampleVariance)
    # attach children
    priorMuMu.initialize([posteriorMu])
    priorMuSigma.initialize([posteriorMu])

    # set up prior nodes and posterior nodes for variance
    priorSigmaShape = GammaNode(shape=priorGammaShape, scale=priorGammaScale, gType="logInverse", name="priorSigmaShape", sampleVariance=sampleVariance)
    priorSigmaScale = GammaNode(shape=priorGammaShape, scale=priorGammaScale, gType="logInverse", name="priorSigmaScale", sampleVariance=sampleVariance)
    priorSigmaShapeLinker = LinkerNode([priorSigmaShape], getParentState)
    priorSigmaScaleLinker = LinkerNode([priorSigmaScale], getParentState)
    posteriorSigma = GammaNode(shape=priorSigmaShapeLinker, scale=priorSigmaScaleLinker, gType="logInverse", name="posteriorSigma", sampleVariance=sampleVariance)
    # attach children
    priorSigmaShape.initialize([posteriorSigma])
    priorSigmaScale.initialize([posteriorSigma])

    # save to the network
    network = [priorMuMu, priorMuSigma,posteriorMu, priorSigmaShape, priorSigmaScale,  posteriorSigma]
    unobservedIndices = np.arange(0, len(network))

    # add the observations
    obs = []
    with open("faculty_dat.csv", "r+") as data:
        i = 1
        children = []
        for line in data:
            line = line.replace("\n","")
            observation = float(line)
            obs.append(observation)
            posteriorMuLinker = LinkerNode([posteriorMu], getParentState)
            posteriorSigmaLinker = LinkerNode([posteriorSigma], getParentState)
            obsNode = NormalNode(mu=posteriorMuLinker, sigma=posteriorSigmaLinker, name=str(i))
            obsNode.setObservation(observation)
            obsNode.initialize([])
            children.append(obsNode)
            i = i + 1

    print("mean observation: ", np.mean(obs))
    print("var observation: ", np.var(obs))

    # add children
    network[2].initialize(children)
    network[5].initialize(children)

    network = network + children

    return network, unobservedIndices

