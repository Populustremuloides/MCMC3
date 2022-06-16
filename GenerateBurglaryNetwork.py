from Nodes import *

def multiConditional(parents):
    burglary = parents[0].state
    earthquake = parents[1].state
    if burglary == 1 and earthquake == 1:
        p = 0.95
    elif burglary == 1 and earthquake == 0:
        p = 0.94
    elif burglary == 0 and earthquake == 1:
        p = 0.29
    elif burglary == 0 and earthquake == 0:
        p = 0.2
    return p

def conditionalJohn(parents):
    alarm = parents[0].state
    if alarm:
        p = 0.9
    else:
        p = 0.2
    return p

def conditionalMary(parents):
    alarm = parents[0].state
    if alarm:
        p = 0.7
    else:
        p = 0.3
    return p

def generateNetwork():
    # A
    B = BernouliNode(p=0.2, name="Burglary")
    E = BernouliNode(p=0.3, name="Earthquake")
    alarmPs = LinkerNode([B, E],multiConditional)
    A = BernouliNode(p=alarmPs, name="Alarm")
    jPs = LinkerNode([A],conditionalJohn)
    J = BernouliNode(p=jPs, name="JohnCalls")
    mPs = LinkerNode([A],conditionalMary)
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

    return network, unobservedIndices