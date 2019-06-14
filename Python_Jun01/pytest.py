
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt




#print("pandas version: ",pd.__version__)   #pandas version:  0.24.2
#print("matplotlib version: ",matplotlib.__version__) #matplotlib version:  3.1.0

#df = pd.read_csv('Iris_data.csv')
#src = {str} 'Iris_data.csv'

#files = pd.read_html('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/')

df = pd.read_csv('/Users/diptiapple/Desktop/Data_science/iris_data_sets/iris.csv')

print(df)
#df = pd.DataFrame(csv)
print(df.head(n=5))

print(type(df))



