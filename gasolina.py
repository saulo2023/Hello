import pandas as pd
import matplotlib.pyplot as plt

# input data
gasdf = pd.read_csv('./gasolina.csv')

gasdf.plot(x='dia', y='venda')
plt.show()

plt.savefig('gasolina.png')
