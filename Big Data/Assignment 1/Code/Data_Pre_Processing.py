import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pre_processing():

    # Importing the data as a dataframe and storing into a variable called data
    data = pd.read_csv(r'F:\Docs\Big data\Data_Sets\airlines.csv')

    # Giving name to the columns present in the dataset
    data.columns = ['Airline ID', 'Name', 'Alias', 'IATA', 'ICAO', 'Callsign', 'Country', 'Active']
    
    #The first 5 entries of the dataset
    print(data.head())

    #The shape of the data
    print(data.shape)

    #Changing \N value to null which is easily recognised by inbuilt functions
    data['Alias'] = data['Alias'].replace(r'\N', np.NaN)
    data['Callsign'] = data['Callsign'].replace(r'\N', np.NaN)
    data['ICAO'].replace(r'\N', np.NaN, inplace = True)
    data['Active'].replace(r'n', 'N', inplace = True)
    
    #Counting the number of missing values in each attributes of the dataset
    print(data.isnull().sum()) 

    #Dropping these as their missing values are greater than 50%
    data.drop(columns = ['IATA', 'Alias'], axis = 1 ,inplace = True)

    #Filling the missing value of countires with its mode
    data['Country'].fillna(data['Country'].mode()[0], inplace = True)
    
    #These two attributes are supposed to have unique values, so dropping all the rows that hve the value of these attributes missing
    data.dropna(subset=['Callsign', 'ICAO'], inplace=True)    
    
    #Counting the number of missing values in each attributes of the dataset
    print(data.isnull().sum()) 
    
    #Final shape of the clean dataset
    print(data.shape)

    #Saving it into a csv
    data.to_csv('cleaned_data.csv', index = False)
    
    #Visualising the distribution of categorical variable, and their unique values 
    for column in data.columns:
        if(column in ['Airline ID', 'Name']):
            pass
        elif(column in ['ICAO', 'Callsign']):
            print(column)
            print("The unique values of this column is : ")
            print(data[column].unique())
        else:
            print(column)
            print("The unique values of this column is : ")
            print(data[column].unique())
            if(column == 'Active'):
                data[column].value_counts().plot(kind = 'pie')
            else:
                data[column].value_counts().plot(kind = 'bar')
            plt.show()
        print("\n\n")

if(__name__ == "__main__"):
    pre_processing()