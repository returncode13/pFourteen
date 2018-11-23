import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.tools as tls
x=np.random.rand(200,100)
fig,ax=plt.subplots()

plt.imshow(x)
plt.show()
tls.mpl_to_plotly(fig)