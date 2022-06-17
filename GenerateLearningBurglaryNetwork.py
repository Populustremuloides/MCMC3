from Nodes import *
import pandas as pd

def multiConditional(parents):
    burglary = parents[0]
    earthquake = parents[1]

    if burglary == 1 and earthquake == 1:
        p = parents[2].state #0.95
    elif burglary == 1 and earthquake == 0:
        p = parents[3].state #0.94
    elif burglary == 0 and earthquake == 1:
        p = parents[4].state #0.29
    elif burglary == 0 and earthquake == 0:
        p = parents[5].state #0.2
    return p

def conditionalJohn(parents):
    alarm = parents[0]
    if alarm == 1:
        p = parents[1].state #0.9
    else:
        p = parents[2].state #0.2
    return p

def conditionalMary(parents):
    alarm = parents[0]
    if alarm == 1:
        p = parents[1].state #0.7
    else:
        p = parents[2].state #0.3
    return p

def getParents(parents):
    return parents[0].state

def generateNetwork(numHyperParams=0, observationDropProb=0, numSamples=100, data=None):

    # hyperparameters for "observed" probabilities (to be used if probabilityNodes are not observed)
    # I am not being excessive here with them. Just one per beta distribution variable
    hyperAlarmGivenBandE = GammaNode(shape=10, scale=2, gType="log", name="hyperAlarmGivenBandE")
    hyperAlarmGivenBandNotE = GammaNode(shape=10, scale=2, gType="log", name="hyperAlarmGivenBandNotE")
    hyperAlarmGivenNotBandE = GammaNode(shape=10, scale=2, gType="log", name="hyperAlarmGivenNotBandE")
    hyperAlarmGivenNotBandNotE = GammaNode(shape=10, scale=2, gType="log", name="hyperAlarmGivenNotBandNotE")

    hyperJohnGivenA = GammaNode(shape=10, scale=2, gType="log", name="hyperJohnGivenA")
    hyperJohnGivenNotA = GammaNode(shape=10, scale=2, gType="log", name="hyperJohnGivenNotA")

    hyperMaryGivenA  = GammaNode(shape=10, scale=2, gType="log", name="hyperMaryGivenA")
    hyperMaryGivenNotA  = GammaNode(shape=10, scale=2, gType="log", name="hyperMaryGivenNotA")

    hyperBurglary = GammaNode(shape=10, scale=2, gType="log", name="hyperBurglary")
    hyperEarthquake = GammaNode(shape=10, scale=2, gType="log", name="hyperEarthquake")

    # probability Nodes **************************************************************

    keptHyperNodes = []

    # multi-conditional parents of Alarm
    if numHyperParams > 0:
        linker = LinkerNode([hyperAlarmGivenBandE], getParents)
        alarmGivenBandE = BetaNode(alpha=linker,beta=1, name="PROB_alarmGivenBandE")
        hyperAlarmGivenBandE.initialize([alarmGivenBandE])
        keptHyperNodes.append(hyperAlarmGivenBandE)
    else:
        alarmGivenBandE = BetaNode(alpha=1, beta=1, name="PROB_alarmGivenBandE")
    if numHyperParams > 1:
        linker = LinkerNode([hyperAlarmGivenBandNotE], getParents)
        alarmGivenBandNotE = BetaNode(alpha=linker,beta=1, name="PROB_alarmGivenBandNotE")
        hyperAlarmGivenBandNotE.initialize([alarmGivenBandNotE])
        keptHyperNodes.append(hyperAlarmGivenBandNotE)
    else:
        alarmGivenBandNotE = BetaNode(alpha=1, beta=1, name="PROB_alarmGivenBandNotE")
    if numHyperParams > 2:
        linker = LinkerNode([hyperAlarmGivenNotBandE], getParents)
        alarmGivenNotBandE = BetaNode(alpha=linker,beta=1, name="PROB_alarmGivenNotBandE")
        hyperAlarmGivenNotBandE.initialize([alarmGivenNotBandE])
        keptHyperNodes.append(hyperAlarmGivenNotBandE)
    else:
        alarmGivenNotBandE = BetaNode(alpha=1,beta=1, name="PROB_alarmGivenNotBandE")
    if numHyperParams > 3:
        linker = LinkerNode([hyperAlarmGivenNotBandNotE], getParents)
        alarmGivenNotBandNotE = BetaNode(alpha=linker,beta=1, name="PROB_alarmGivenNotBandNotE")
        hyperAlarmGivenNotBandNotE.initialize([alarmGivenNotBandNotE])
        keptHyperNodes.append(hyperAlarmGivenNotBandNotE)
    else:
        alarmGivenNotBandNotE = BetaNode(alpha=1, beta=1, name="PROB_alarmGivenNotBandNotE")

    # conditional parents of JohnCalls
    if numHyperParams > 4:
        linker = LinkerNode([hyperJohnGivenA], getParents)
        johnGivenA = BetaNode(alpha=linker,beta=1, name="PROB_johnGivenA")
        hyperJohnGivenA.initialize([johnGivenA])
        keptHyperNodes.append(hyperJohnGivenA)
    else:
        johnGivenA = BetaNode(alpha=1, beta=1, name="PROB_johnGivenA")
    if numHyperParams > 5:
        linker = LinkerNode([hyperJohnGivenNotA], getParents)
        johnGivenNotA = BetaNode(alpha=linker,beta=1, name="PROB_johnGivenNotA")
        hyperJohnGivenNotA.initialize([johnGivenNotA])
        keptHyperNodes.append(hyperJohnGivenNotA)
    else:
        johnGivenNotA = BetaNode(alpha=1, beta=1, name="PROB_johnGivenNotA")

    # conditional parents of MaryCalls
    if numHyperParams > 6:
        linker = LinkerNode([hyperMaryGivenA], getParents)
        maryGivenA = BetaNode(alpha=linker,beta=1, name="PROB_maryGivenA")
        hyperMaryGivenA.initialize([maryGivenA])
        keptHyperNodes.append(hyperMaryGivenA)
    else:
        maryGivenA = BetaNode(alpha=1, beta=1, name="PROB_maryGivenA")
    if numHyperParams > 7:
        linker = LinkerNode([hyperMaryGivenNotA], getParents)
        maryGivenNotA = BetaNode(alpha=linker,beta=1, name="PROB_maryGivenNotA")
        hyperMaryGivenNotA.initialize([maryGivenNotA])
        keptHyperNodes.append(hyperMaryGivenNotA)
    else:
        maryGivenNotA = BetaNode(alpha=1, beta=1, name="PROB_maryGivenNotA")

    # probabilities of burglary
    if numHyperParams > 8:
        linker = LinkerNode([hyperBurglary], getParents)
        pBurglary = BetaNode(alpha=linker,beta=1, name="PROB_burglary")
        hyperBurglary.initialize([pBurglary])
        keptHyperNodes.append(hyperBurglary)
    else:
        pBurglary = BetaNode(alpha=1, beta=1, name="PROB_burglary")
    if numHyperParams > 9:
        linker = LinkerNode([hyperEarthquake], getParents)
        pEarthquake = BetaNode(alpha=linker,beta=1, name="PROB_earthquake")
        hyperEarthquake.initialize([pEarthquake])
        keptHyperNodes.append(hyperEarthquake)
    else:
        pEarthquake = BetaNode(alpha=1,beta=1, name="PROB_earthquake")

    probabilityNodes = [pBurglary, pEarthquake, alarmGivenBandE,
                        alarmGivenBandNotE, alarmGivenNotBandE,
                        alarmGivenNotBandNotE, johnGivenA, johnGivenNotA,
                        maryGivenA, maryGivenNotA]

    # initialize (even though potentially all of them may not be used)







    # observation nodes *******************************************************************************************

    pBurglaryChildren = []
    pEarthquakeChildren = []
    pAlarmChildren = []
    pJohnChildren = []
    pMaryChildren = []

    df = pd.read_csv(data)

    for index, row in df.iterrows():
        randomNums = np.random.uniform(0,1, 5) # decide whether to keep all the data

        # Burglary
        if randomNums[0] > observationDropProb: # don't add the node if it is "dropped"
            pBurglaryLinker = LinkerNode([pBurglary], getParents)
            B = BernouliNode(p=pBurglaryLinker, name="Burglary")
            B.setObservation(row["Burglary"])
            pBurglaryChildren.append(B)

        # Earthquake
        if randomNums[1] > observationDropProb:
            pEarthquakeLinker = LinkerNode([pEarthquake], getParents)
            E = BernouliNode(p=pEarthquakeLinker, name="Earthquake")
            E.setObservation(row["Earthquake"])
            pEarthquakeChildren.append(E)

        # Alarms
        if randomNums[2] > observationDropProb:
            alarmPs = LinkerNode([row["Burglary"], row["Earthquake"], alarmGivenBandE, alarmGivenBandNotE,
                                  alarmGivenNotBandE, alarmGivenNotBandNotE],multiConditional)
            A = BernouliNode(p=alarmPs, name="Alarm")
            A.setObservation(row["Alarm"])
            pAlarmChildren.append(A)

        # JohnCalls
        if randomNums[3] > observationDropProb:
            jPs = LinkerNode([row["Alarm"], johnGivenA, johnGivenNotA],conditionalJohn)
            J = BernouliNode(p=jPs, name="JohnCalls")
            J.setObservation(row["JohnCalls"])
            pJohnChildren.append(J)

        # MaryCalls
        if randomNums[4] > observationDropProb:
            mPs = LinkerNode([row["Alarm"], maryGivenA, maryGivenNotA],conditionalMary)
            M = BernouliNode(p=mPs, name="MaryCalls")
            M.setObservation(row["MaryCalls"])
            pMaryChildren.append(M)
        if index > numSamples:
            break

    # initialize the probability nodes
    alarmGivenBandE.initialize(pAlarmChildren)
    alarmGivenBandNotE.initialize(pAlarmChildren)
    alarmGivenNotBandE.initialize(pAlarmChildren)
    alarmGivenNotBandNotE.initialize(pAlarmChildren)
    johnGivenA.initialize(pJohnChildren)
    johnGivenNotA.initialize(pJohnChildren)
    maryGivenA.initialize(pMaryChildren)
    maryGivenNotA.initialize(pMaryChildren)
    pBurglary.initialize(pBurglaryChildren)
    pEarthquake.initialize(pEarthquakeChildren)

    # combine together in 1 network
    network = keptHyperNodes + probabilityNodes + \
              pBurglaryChildren + pEarthquakeChildren + \
              pAlarmChildren + pJohnChildren + pMaryChildren

    unobservedIndices = np.arange(0, len(keptHyperNodes + probabilityNodes))

    return network, unobservedIndices