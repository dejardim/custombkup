import argparse 


# Create the parser
parser = argparse.ArgumentParser()

# Adds Custombkup arguments
parser.add_argument('-fp', '--frompath', type=str, required=False)
parser.add_argument('-tp', '--topath', type=str, required=False)
parser.add_argument('-lp', '--logpath', type=str, required=False)

# Parse the argument
args = parser.parse_args()
