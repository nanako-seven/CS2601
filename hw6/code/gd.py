import numpy as np


def gd_const_ss(fp, x0, stepsize, tol=1e-5, maxiter=100000):
    """
    fp: function that takes an input x and returns the derivative of f at x
    x0: initial point in gradient descent
    stepsize: constant step size used in gradient descent
    tol: toleracne parameter in the stopping crieterion. Gradient descent stops 
         when the 2-norm of the gradient is smaller than tol
    maxiter: maximum number of iterations in gradient descent.

    This function should return a list of the sequence of approximate solutions
    x_k produced by each iteration
    """
    x_traces = [np.array(x0)]
    x = np.array(x0)
    g = fp(x)
    while np.linalg.norm(g) >= tol and len(x_traces) <= maxiter:
        x -= stepsize * g
        x_traces.append(x.copy())
        g = fp(x)
    return x_traces
