import collections
import matplotlib.pyplot as plt
import numpy as np
stepSize = 0.01
def read_data() :
    data = open("vehicle_sale_data.txt" , "r")
    gdp_sale = collections.OrderedDict()
    for line in data.readlines()[1:] :
        record = line.split(",")
        gdp_sale[float(record[1])] = float(record[2].replace('\n', ""))
    
    return gdp_sale
def sale_for_data(constant, slope, data):
    return constant + slope * data   # y = c + ax format
def step_cost_function_for(gdp_sale, constant, slope) :
    global stepSize
    diff_sum_constant = 0 # diff of sum for constant 'c' in "c + ax" equation
    diff_sum_slope = 0  # diff of sum for 'a' in "c + ax" equation
    cost = 0
    gdp_for_years = list(gdp_sale.keys())
    for year_gdp in gdp_for_years: # for each year's gdp in the sample data
        # get the sale for given 'c' and 'a'by giving the GDP for this sample record
        trg_data_sale = sale_for_data(constant, slope, year_gdp) # calculated sale for current 'c' and 'a'
        a_year_sale = gdp_sale.get(year_gdp) # real sale for this record
        diff_sum_slope = diff_sum_slope + ((trg_data_sale - a_year_sale) * year_gdp) # slope's (h(y) - y) * x
        diff_sum_constant = diff_sum_constant + (trg_data_sale - a_year_sale) # consant's (h(y) - y)
        cost += (trg_data_sale - a_year_sale) ** 2
    cost = cost / len(gdp_sale) / 2
    step_for_constant = (stepSize / len(gdp_sale)) * diff_sum_constant # distance to be moved by c
    step_for_slope = (stepSize / len(gdp_sale)) * diff_sum_slope # distance to be moved by a
    new_constant = constant - step_for_constant # new c
    new_slope = slope - step_for_slope # new a
    print("partial diff of c and s are : ", step_for_constant, step_for_slope)    
    print("cost : ", cost)
    return new_constant, new_slope
def get_weights(gdp_sale) :
    constant = 1
    slope = 1
    accepted_diff = 0.01
    while 1 == 1:  # continue till we reach local minimum
        new_constant, new_slope = step_cost_function_for(gdp_sale, constant, slope)
        # if the diff is too less then lets break
        if (abs(constant - new_constant) <= accepted_diff) and (abs(slope - new_slope) <= accepted_diff):
            print( "done. Diff is less than " + str(accepted_diff))
            return new_constant, new_slope
        else:
            constant = new_constant
            slope = new_slope
            print ("new values for constant and slope are " + str(new_constant) + ", " + str(new_slope))
def main() :
    data = read_data()
    contant, slope = get_weights(data)
    print ("constant :", contant, ", slope:", slope)
    f, ax = plt.subplots(figsize=(7, 7))
    c1, c2 = "#3366AA", "#AA3333"
    # print(data)
    W = [[1, 7], [2, 2], [3, 1], [4, 3]]
    # for point in data.keys():
    #     # print(point, data[point])
    #     W.append([point, data[point]])
    W = np.array(W)
    ax.scatter(*W.T, c=c1,s = 10, label = "Datapoints")
    ax.legend()
    # ax.scatter(*w2.T, c=c2, marker="D", label = "w2")
    # ax.legend()
    x_vec = np.linspace(0.9, 4.1, 20)
    y_vec = 15.25 - 10.05*x_vec + 1.75*x_vec*x_vec 
    # y_vec = -y_vec   
    print(y_vec)
    plt.plot(x_vec, y_vec, 'r')
    plt.show()
if __name__ == '__main__':
    main()