import sys
import string
import operator
from optparse import OptionParser

from .lib import load_data, get_evidence, get_opinion, get_theta, test_flow, write_to_file, extract_evidence, matrixgeoconvtest
from .lib import otimes, oplus, odot, scalartimes, boxtimes, matrixtimes, matrixplus, matrixsquare, matrixpow, matrixgeo, matrixgeonew, func_belief, func_belief_sqrt
import json



# python -B test.py -d data.txt -c 2 -m 1 -o output.txt
# parser.set_defaults(outputfile = "output.txt", data = "exampleSet.txt", constant=2, mode=0, threshold=1.0)

# Constants
uncertainty_constant = 2
threshold=1.0


def get_multiplication_mode(mode, data):
    if mode == 'otimes':
        return otimes
    elif mode == 'boxtimes':
        f = func_belief
        return lambda x, y: boxtimes(x, y, f)
    elif mode == 'boxtimes2':
        f = func_belief_sqrt
        return lambda x, y: boxtimes(x, y, f)
    elif mode == 'odot':
        theta = get_theta(data)
        print("theta", theta)
        # print("theta = " + str(theta))
        return lambda x, y: odot(x, y, theta, uncertainty_constant)	



# This runs the evidence-based subjective logic algorithm to calculate our "worldview" of other nodes
# It takes an array of global interactions between nodes
# in the form of (from: node, to: node, evidence: number)
# (evidence can be positive or negative)
# 
# It then derives the worldview matrix
# Which is the relative opinion and absolute reputation of every node
# From the perspective of every other node
# Returned as (opinions, evidence)
import numpy as np

def converge_worldview(interactions):
    # interactions = np.asarray(interactions)
    # Modes
    # Set plus, times operations with respect to EBSL mode
    plus = oplus
    times = get_multiplication_mode('odot', interactions)

    # Convert interaction data into opinion matrix
    P = get_opinion(interactions, uncertainty_constant)

    # initfile = open(options.outputfile.split(".")[0]+"-init."+options.outputfile.split(".")[1], "w")
    # # Opinions initially
    # write_to_file(P, initfile)

    # initfile.write("#Evidences initially\n")
    # write_to_file(extract_evidence(P, uncertainty_constant), initfile)
    # initfile.close()

    # print("ready to test for convergence")
    # print("theshold is set to: " + str(options.threshold))
    
    # Converge
    P2, count, t = matrixgeoconvtest(P, threshold, plus, times)

    # print("Convergence reached at iteration " + str(count))
    # print("write to file: " + options.outputfile)
    # outputfile.write("#Convergence after iteration: "+ str(count)+"\n")
    # outputfile.write("#Actual distance to next iteration: "+ str(t)+"\n")

    # outputfile.write("#Opinions: \n")
    # write_to_file(P2, outputfile)

    # with open('opinions.json', 'w') as outfile:
    #     json.dump(P2, outfile)

    # print("done...")

    # outputfile.write("#Underlying derived Evidence: \n")
    # print("convert to Evidence matrix")
    E2 = extract_evidence(P2, uncertainty_constant)

    # with open('evidence.json', 'w') as outfile:
    #     json.dump(E2, outfile)

    # print("done...")

    # print("write_to file")
    # write_to_file(E2, outputfile)

    opinions, evidence = P2, E2
    return (opinions, evidence)