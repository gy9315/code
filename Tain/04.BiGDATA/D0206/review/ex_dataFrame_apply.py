import pandas as pd
import random as rd
import numpy as np
np.random.seed(100)
a=np.random.randint(0,10,9)
b=np.random.randint(0,10,9)
DF=pd.DataFrame([a,b])
print(DF)
print(DF.apply(lambda x:x+1))