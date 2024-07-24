import pytest
from project import FunctionPlotter 


def test_linear_function_plot():
    def linear_function(x):
        return 2 * x + 1

    plotter = FunctionPlotter(linear_function, x_range=(-10, 10))
    plotter.plot()

def test_quadratic_function_plot():
    def quadratic_function(x):
        return x**2 - 3*x + 2

    plotter = FunctionPlotter(quadratic_function, x_range=(-5, 5))
    plotter.plot()



if __name__ == '__main__':
    pytest.main()