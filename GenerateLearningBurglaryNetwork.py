import pandas as pd
from Nodes import *



def getParentState(parents):
    return parents[0].state

def generateNetwork(numSamples, numHyperParameters, dataset):
    dfData = pd.read_csv(dataset)

    # prior nodes
    priorBurglaryAlpha = GammaNode(shape=1,scale=0.5,gType="log", name="PriorBurglaryAlpha")
    priorBurglaryBeta = GammaNode(shape=1,scale=0.5,gType="log", name="PriorBurglaryBeta")
    priorEarthquakeAlpha = GammaNode(shape=1,scale=0.5,gType="log", name="PriorEarthquakeAlpha")
    priorEarthquakeBeta = GammaNode(shape=1,scale=0.5,gType="log", name="PriorEarthquakeBeat")
    priorAlarmAlpha = GammaNode(shape=1,scale=0.5,gType="log", name="PriorAlarmAlpha")
    priorAlarmBeta = GammaNode(shape=1,scale=0.5,gType="log", name="PriorAlarmBeat")
    priorJohnAlpha = GammaNode(shape=1,scale=0.5,gType="log", name="PriorJohnAlpha")
    priorJohnBeta = GammaNode(shape=1,scale=0.5,gType="log", name="PriorJohnBeta")
    priorMaryAlpha = GammaNode(shape=1,scale=0.5,gType="log", name="PriorMaryAlpha")
    priorMaryBeta = GammaNode(shape=1,scale=0.5,gType="log", name="PriorMaryBeta")

    # POSTERIOR NODES

    # BURGLARY ****************************************************************
    if numHyperParameters > 0:
        burglaryAlphaLinker = LinkerNode([priorBurglaryAlpha], getParentState)
    else:
        burglaryAlphaLinker = 1
    if numHyperParameters > 1:
        burglaryBetaLinker = LinkerNode([priorBurglaryBeta], getParentState)
    else:
        burglaryBetaLinker = 1
    burglary = BetaNode(alpha=burglaryAlphaLinker,beta=burglaryBetaLinker, name="Burglary")

    # EARTHQUAKE ****************************************************************
    if numHyperParameters > 2:
        earthquakeAlphaLinker = LinkerNode([priorEarthquakeAlpha], getParentState)
    else:
        earthquakeAlphaLinker = 1
    if numHyperParameters > 3:
        earthquakeBetaLinker = LinkerNode([priorEarthquakeBeta], getParentState)
    else:
        earthquakeBetaLinker = 1
    earthquake = BetaNode(alpha=earthquakeAlphaLinker,beta=earthquakeBetaLinker, name="Earthquake")

    # ALARM ********************************************************************
    if numHyperParameters > 4:
        alarmAlphaLinker = LinkerNode([priorAlarmAlpha], getParentState)
    else:
        alarmAlphaLinker = 1
    if numHyperParameters > 5:
        alarmBetaLinker = LinkerNode([priorAlarmBeta], getParentState)
    else:
        alarmBetaLinker = 1
    alarm = BetaNode(alpha=alarmAlphaLinker,beta=alarmBetaLinker, name="Alarm")

    # John ********************************************************************
    if numHyperParameters > 6:
        johnAlphaLinker = LinkerNode([priorJohnAlpha], getParentState)
    else:
        johnAlphaLinker = 1
    if numHyperParameters > 7:
        johnBetaLinker = LinkerNode([priorJohnBeta], getParentState)
    else:
        johnBetaLinker = 1
    johnCalls = BetaNode(alpha=johnAlphaLinker,beta=johnBetaLinker, name="JohnCalls")

    # Mary ********************************************************************
    if numHyperParameters > 8:
        maryAlphaLinker = LinkerNode([priorMaryAlpha], getParentState)
    else:
        maryAlphaLinker = 1
    if numHyperParameters > 9:
        maryBetaLinker = LinkerNode([priorMaryBeta], getParentState)
    else:
        maryBetaLinker = 1
    maryCalls = BetaNode(alpha=maryAlphaLinker,beta=maryBetaLinker,name="MaryCalls")

    # initialize children of the priors
    priorBurglaryAlpha.initialize([burglary])
    priorBurglaryBeta.initialize([burglary])
    priorEarthquakeAlpha.initialize([earthquake])
    priorEarthquakeBeta.initialize([earthquake])
    priorAlarmAlpha.initialize([alarm])
    priorAlarmBeta.initialize([alarm])
    priorJohnAlpha.initialize([johnCalls])
    priorJohnBeta.initialize([johnCalls])
    priorMaryAlpha.initialize([maryCalls])
    priorMaryBeta.initialize([maryCalls])

    # store the prior nodes
    priors = [priorBurglaryAlpha, priorBurglaryBeta, priorEarthquakeAlpha,
              priorEarthquakeBeta, priorAlarmAlpha, priorAlarmBeta,
              priorJohnAlpha, priorJohnBeta, priorMaryAlpha, priorMaryBeta]
    priors = priors[:numHyperParameters] # not the most efficient way, but keeps us from adding hyperparameters we aren't using

    # OBSERVATION NODES

    # store the children observations in these lists
    burglaryChildren = []
    earthquakeChildren = []
    alarmChildren = []
    johnChildren = []
    maryChildren = []

    # initialize observation nodes
    for index, row in dfData.iterrows():
        # burglary observations
        name = "burglary_obs_" + str(index)
        bLinker = LinkerNode([burglary], getParentState)
        burglaryObservation = BernouliNode(p=bLinker, name=name)
        burglaryObservation.setObservation(row["Burglary"])
        burglaryChildren.append(burglaryObservation)

        # earthquake observations
        name = "earthquake_obs_" + str(index)
        eLinker = LinkerNode([earthquake], getParentState)
        earthquakeObservation = BernouliNode(p=eLinker, name=name)
        earthquakeObservation.setObservation(row["Earthquake"])
        earthquakeObservation.initialize([]) # no children
        earthquakeChildren.append(earthquakeObservation)

        # alarm observations
        name = "alarm_obs_" + str(index)
        aLinker = LinkerNode([alarm], getParentState)
        alarmObservation = BernouliNode(p=aLinker, name=name)
        alarmObservation.setObservation(row["Alarm"])
        alarmObservation.initialize([]) # no children
        alarmChildren.append(alarmObservation)

        # john observations
        name = "john_obs_" + str(index)
        jLinker = LinkerNode([johnCalls], getParentState)
        johnObservation = BernouliNode(p=jLinker,name=name)
        johnObservation.setObservation(row["JohnCalls"])
        johnObservation.initialize([]) # no children
        johnChildren.append(johnObservation)

        # mary observations
        name = "mary_obs_" + str(index)
        mLinker = LinkerNode([maryCalls], getParentState)
        maryObservation = BernouliNode(p=mLinker, name=name)
        maryObservation.setObservation(row["MaryCalls"])
        maryObservation.initialize([]) # no children
        maryChildren.append(maryObservation)

        if index > numSamples:
            break

    burglary.initialize(burglaryChildren)
    earthquake.initialize(earthquakeChildren)
    alarm.initialize(alarmChildren)
    johnCalls.initialize(johnChildren)
    maryCalls.initialize(maryChildren)

    estimatedValues = [burglary, earthquake, alarm, johnCalls, maryCalls]

    network = priors + estimatedValues + burglaryChildren + earthquakeChildren + alarmChildren + johnChildren + maryChildren
    unobservedIndices = np.arange(0, len(priors) + len(estimatedValues))

    return network, unobservedIndices