from Nodes import *

def multiConditional(parents):
    burglary = parents[0].state
    earthquake = parents[1].state

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
    alarm = parents[0].state
    if alarm == 1:
        p = parents[1].state #0.9
    else:
        p = parents[2].state #0.2
    return p

def conditionalMary(parents):
    alarm = parents[0].state
    if alarm == 1:
        p = parents[1].state #0.7
    else:
        p = parents[2].state #0.3
    return p

def getParents(parents):
    return parents[0].state

def generateNetwork():

    # "observed" (or not) probabilities **************************************************************

    # multi-conditional parents of Alarm
    alarmGivenBandE = BetaNode(alpha=1, beta=1, name="PROB_alarmGivenBandE")
    alarmGivenBandNotE = BetaNode(alpha=1, beta=1, name="PROB_alarmGivenBandNotE")
    alarmGivenNotBandE = BetaNode(alpha=1,beta=1, name="PROB_alarmGivenNotBandE")
    alarmGivenNotBandNotE = BetaNode(alpha=1, beta=1, name="PROB_alarmGivenNotBandNotE")

    johnGivenA = BetaNode(alpha=1, beta=1, name="PROB_johnGivenA")
    johnGivenNotA = BetaNode(alpha=1, beta=1, name="PROB_johnGivenNotA")

    maryGivenA = BetaNode(alpha=1, beta=1, name="PROB_maryGivenA")
    maryGivenNotA = BetaNode(alpha=1, beta=1, name="PROB_maryGivenNotA")

    pBurglary = BetaNode(alpha=1, beta=1, name="PROB_burglary")
    pEarthquake = BetaNode(alpha=1,beta=1, name="PROB_earthquake")

    # actual nodes *******************************************************************************************

    # Burglary
    pBurglaryLinker = LinkerNode([pBurglary], getParents)
    B = BernouliNode(p=pBurglaryLinker, name="Burglary")

    # Earthquake
    pEarthquakeLinker = LinkerNode([pEarthquake], getParents)
    E = BernouliNode(p=pEarthquakeLinker, name="Earthquake")

    # Alarms
    alarmPs = LinkerNode([B, E, alarmGivenBandE, alarmGivenBandNotE,
                          alarmGivenNotBandE, alarmGivenNotBandNotE],multiConditional)
    A = BernouliNode(p=alarmPs, name="Alarm")

    # JohnCalls
    jPs = LinkerNode([A, johnGivenA, johnGivenNotA],conditionalJohn)
    J = BernouliNode(p=jPs, name="JohnCalls")

    # MaryCalls
    mPs = LinkerNode([A, maryGivenA, maryGivenNotA],conditionalMary)
    M = BernouliNode(p=mPs, name="MaryCalls")


    # combine together in 1 network
    network = [B,E,A,J,M]
    unobservedIndices = np.arange(0, len(network))

    # add children nodes to parents
    bChildren = [A]
    eChildren = [A]
    aChildren = [J,M]
    jChildren = []
    mChildren = []

    B.initialize(bChildren)
    E.initialize(eChildren)
    A.initialize(aChildren)
    J.initialize(jChildren)
    M.initialize(mChildren)

    alarmGivenBandEChildren = [A]
    alarmGivenBandNotEChildren = [A]
    alarmGivenNotBandEChildren = [A]
    alarmGivenNotBandNotEChildren = [A]
    johnGivenAChildren = [J]
    johnGivenNotAChildren = [J]
    maryGivenAChildren = [M]
    maryGivenNotAChildren = [M]
    pBurglaryChildren = [B]
    pEarthquakeChildren = [E]

    alarmGivenBandE.initialize(alarmGivenBandEChildren)
    alarmGivenBandNotE.initialize(alarmGivenBandNotEChildren)
    alarmGivenNotBandE.initialize(alarmGivenNotBandEChildren)
    alarmGivenNotBandNotE.initialize(alarmGivenNotBandNotEChildren)
    johnGivenA.initialize(johnGivenAChildren)
    johnGivenNotA.initialize(johnGivenNotAChildren)
    maryGivenA.initialize(maryGivenAChildren)
    maryGivenNotA.initialize(maryGivenNotAChildren)
    pBurglary.initialize(pBurglaryChildren)
    pEarthquake.initialize(pEarthquakeChildren)

    # SET OBSERVATIONS

    alarmGivenBandE.setObservation(0.95)
    alarmGivenBandNotE.setObservation(0.94)
    alarmGivenNotBandE.setObservation(0.29)
    alarmGivenNotBandNotE.setObservation(0.2)
    johnGivenA.setObservation(0.90)
    johnGivenNotA.setObservation(0.2)
    maryGivenA.setObservation(0.7)
    maryGivenNotA.setObservation(0.3)
    pBurglary.setObservation(0.2)
    pEarthquake.setObservation(0.3)

    return network, unobservedIndices