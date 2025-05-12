DEBUG_MODE=True
import numpy as np
import pandas as pd
a=np.zeros((10,10,3))
print(a)
a=a.reshape(1,-1)
print(a)
b=pd.DataFrame(a)
print(b)