#%%

import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px
def main():
    data = {'Product Development steps' : ['Requirement Elicitation', 'Requirement Analysis', 'Software Development', 'Debugging & Testing', 'Others'], 'Time spent (in hours)' : [50, 110, 250, 180, 70]}
    fig = px.funnel(data, y = 'Product Development steps', x = 'Time spent (in hours)')
    fig.show()
if(__name__ == '__main__'):
    main()

# %%
