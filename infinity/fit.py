from scipy.optimize import curve_fit
import numpy as np

def check_monotonic_np(arr):
    arr = np.asarray(arr)
    diffs = np.diff(arr)

    if np.all(diffs == 0):
        return True, "constant"
    elif np.all(diffs >= 0):
        return True, "increasing"
    elif np.all(diffs <= 0):
        return True, "decreasing"
    else:
        return False, None

def hyperbola_with_translation_x_y(x, a, c, d):
    return a / (x - c) + d

def fit_shifted_inverse_with_offset(x_values, y_values):
    """
    Fits y = a / (n - c) + d using nonlinear least squares.

    Args:
        n_values (list of float): Input values (x).
        y_values (list of float): Observed outputs (y).
        initial_guess (tuple): Starting values for (a, c, d).

    Returns:
        tuple: (a, c, d)
    """

    projections_range = max(x_values) - min(x_values)
    # not using scaling of y values now, it made the fit algorithm to fail.
    #dts_range = max(y_values) - min(y_values)
    #y_values = [x *(projections_range / dts_range) for x in y_values]
    
    if not x_values or not y_values or len(x_values) != len(y_values):
        raise ValueError("Input lists must be non-empty and of the same length.")



    # Fit the curve using curve_fit from scipy.optimize
        # bounds definition
        # defined for a, c and d
        # two lists with lower and upper bounds
        # [min a, min c, min d],
        # [max a, max c, max d]
    monotonic, direction = check_monotonic_np(x_values)
    if monotonic and direction =='increasing':
        initial_guess = (-1, max(x_values) + 0.1 * projections_range, 0)
        popt, _ = curve_fit(hyperbola_with_translation_x_y, x_values, y_values, p0=initial_guess,
                        bounds=([-float('inf'),max(x_values),-1],
                                 [0, float('inf'),1]))
    if monotonic and direction =='decreasing':
        initial_guess = (1, min(x_values) - 0.1 * projections_range, 0)
        popt, _ = curve_fit(hyperbola_with_translation_x_y, x_values, y_values, p0=initial_guess,
                        bounds=([0,-float('inf'),-1],
                                 [float('inf'), min(x_values),1]))

    
    
    return tuple(popt)