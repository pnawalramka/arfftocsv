import os
import pathlib

import pandas as pd
from scipy.io.arff import loadarff


filename = 'updateme.arff'
dirname = pathlib.Path(__file__).resolve().parent

def main():
	filepath = pathlib.Path.joinpath(dirname, filename)
	dataset = loadarff(filepath)
	df = pd.DataFrame(dataset[0])
	# convert byte columns to str
	cols = [col for col in df.columns if df[col].dtype=='object']
	df[cols] = df[cols].apply(lambda x: x.str.decode('utf8'))

	out = os.path.splitext(filepath)[0] + '.csv'
	df.to_csv(out, index=False)


if __name__ == '__main__':
	main()
