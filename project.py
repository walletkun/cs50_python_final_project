import numpy as np
import matplotlib.pyplot as plt
import math

class FunctionPlotter:
    #constructor
    def __init__(self,function, x_range = (-100,100), num_points = 1000):
        self.function = function
        self.x_range = x_range
        self.num_points = num_points


    
    def plot(self):
        if self.x_range[0] == float('-inf') or self.x_range[1] == float('inf'):
            #Very large negative and positive value
            x_min = -1e10
            x_max = 1e10
        else:
            x_min,x_max = self.x_range
        
        #Testing
        x = np.linspace(x_min,x_max,self.num_points)
        y = self.function(x)

        plt.figure(figsize=(8,6))
        plt.plot(x,y)
        plt.axhline(0, color = "black", linestyle = '-')
        plt.axvline(0, color = "black", linestyle= "-")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Function Plot")
        plt.grid(True)
        plt.show()



def parabola(x):
    return x ** 2


def sine_function(x):
    return np.sin(x)

def euclear_function(x):
    return np.exp(x)

def main():
    function_str = input("Enter a function of f(x): ")
    custom_function = lambda x: np.array([eval(function_str) for x in x])
    plotter = FunctionPlotter(custom_function)
    plotter.plot()

if __name__ == "__main__":
    main()