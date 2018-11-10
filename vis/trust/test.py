import sys
import string
import operator
from optparse import OptionParser

from lib import load_data, get_evidence, get_opinion, get_theta, test_flow, write_to_file, extract_evidence, matrixgeoconvtest
from lib import otimes, oplus, odot, scalartimes, boxtimes, matrixtimes, matrixplus, matrixsquare, matrixpow, matrixgeo, matrixgeonew, func_belief, func_belief_sqrt
import json


	
parser = OptionParser()
parser.add_option("-o", "--outputfile",
    help="Filename for output data.")
parser.add_option("-d", "--data",
    help="Filename for data set.")
parser.add_option("-c", "--constant", type="int", 
    help="Constant used in Uncertainty Calculation.")
parser.add_option("-m", "--mode", type="int", 
    help="Mode used for mul. mode = 0 --> boxtimes, mode=1--> odot.")
parser.add_option("-t", "--threshold", type="float", 
    help="Convergence threshold")
parser.set_defaults(outputfile = "output.txt", data = "exampleSet.txt", constant=2, mode=0, threshold=1.0)
options, args = parser.parse_args()


outputfile = open(options.outputfile.split(".")[0]+"-conv."+options.outputfile.split(".")[1], "w")
outputfile.write("#Convergence Threshold = "+ str(options.threshold)+".\n")

# order of invention
# boxtimes
# odot

print("Dataset: " + options.data)
print("Constant: " +  str(options.constant))
if options.mode == 0:
	print("boxtimes is set as multiplication, g(x) = x_b")
	outputfile.write("#boxtimes is set as multiplication, g(x) = x_b\n")
else:
	if options.mode == 1:
		print("odot is set as multiplication")
		outputfile.write("#odot is set as multiplication.\n")
	else:
		if options.mode == 2:
			print("boxtimes is set as multiplication, g(x) = sqrt(x_b)")
			outputfile.write("#boxtimes is set as multiplication, g(x) = sqrt(x_b)\n")
		else:
			if options.mode == 4:
				print("otimes is set as multiplication")
				outputfile.write("#otimes is set as multiplication.\n")
			else:
				print("No valid mode selected; mode can be either 0,1, or 2.")

print("-----------------------------------------------------------------------------")
print("Use -d FILENAME in command line to set dataset to FILENAME")
print("Use -c CONSTANT in command line to set uncertianty constant to value CONSTANT")
print("Use -m MODE in command line to set multiplication mode to value MODE")
print("Use -o FILENAME in command line to set the output filenames to FILENAME")
print("use -t FLOAT in command line to set the convergence threshold")
print("-----------------------------------------------------------------------------")

data = load_data(options.data)
print("dataset loaded...")

# Convert data into opinion matrix
print("Convert dataset to Opinion Matrix...")
P = get_opinion(data, options.constant)

# print(P)
# Set plus, times operations with respect to EBSL mode
plus = oplus


if (options.mode & 4) == 4:
	print("otimes")
	times = otimes
else:
	if (options.mode & 1) == 0:
		if (options.mode & 2) == 0:
			print("boxtimes, x_b")
			f = func_belief
		else:
			print("boxtimes, sqrt(x_b)")
			f = func_belief_sqrt
		times = lambda x, y: boxtimes(x, y, f)
	else:
		print("odot")
		theta = get_theta(data)
		print("theta = " + str(theta))
		outputfile.write("#theta = "+str(theta)+ ".\n")
		times = lambda x, y: odot(x, y, theta, options.constant)		
print("-----------------------------------------------------------------------------")
initfile = open(options.outputfile.split(".")[0]+"-init."+options.outputfile.split(".")[1], "w")


print("write initial state to file: " + options.outputfile)

initfile.write("#Opinions initially\n")
write_to_file(P, initfile)

initfile.write("#Evidences initially\n")
write_to_file(extract_evidence(P, options.constant), initfile)
initfile.close()


print("ready to test for convergence")
print("theshold is set to: " + str(options.threshold))


P2, count, t = matrixgeoconvtest(P, options.threshold, plus, times)
print("Convergence reached at iteration " + str(count))
print("write to file: " + options.outputfile)
outputfile.write("#Convergence after iteration: "+ str(count)+"\n")
outputfile.write("#Actual distance to next iteration: "+ str(t)+"\n")

outputfile.write("#Opinions: \n")
write_to_file(P2, outputfile)
with open('opinions.json', 'w') as outfile:
    json.dump(P2, outfile)

print("done...")

outputfile.write("#Underlying derived Evidence: \n")
print("convert to Evidence matrix")
E2 = extract_evidence(P2, options.constant)
with open('evidence.json', 'w') as outfile:
    json.dump(E2, outfile)
print("done...")

print("write_to file")
write_to_file(E2, outputfile)


outputfile.close()

# R = A + fixedpoint(R * A)
# F = T + fixedpoint(R * T)

# R = 






print("exit")




# extracts direct referral trust matrix A
# A = direct referral trust
# T = direct functional trust
# R = final referral trust
# F = final functional trust

# final referral   = direct referral   + fixedpoint(direct referral * direct functional)
# final functional = direct functional + fixedpoint(final referral * direct functional)

# R = A + fixedpoint(R * A)
# F = T + fixedpoint(R * T)

# the final functional trust matrix F is 
# F = matrixgeoconvtest()