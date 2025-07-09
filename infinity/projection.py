import math

def project_to_1d_along_line(xs, ys):
    """
    Projects 2D points onto the best-fit line and returns 1D scalar distances
    along the line from the base point (centroid projection onto line).

    Args:
        xs (list of float): x-coordinates
        ys (list of float): y-coordinates

    Returns:
        list of float: Scalar values representing each point's position along the line
    """
    if len(xs) != len(ys):
        raise ValueError("Input lists must be non-empty and of the same length.")

    # Fit the best-fit line
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    denominator = sum((x - mean_x) ** 2 for x in xs)

    if denominator == 0:
        raise ValueError("Cannot fit a line if all x values are the same.")

    m = numerator / denominator
    b = mean_y - m * mean_x

    # Direction vector of the line
    dx, dy = 1, m
    mag = math.sqrt(dx ** 2 + dy ** 2)
    dir_x, dir_y = dx / mag, dy / mag  # Unit direction vector

    # Base point on the line (use mean point on line)
    base_x = mean_x
    base_y = m * mean_x + b

    # Compute scalar projection for each point
    scalars = []
    for x, y in zip(xs, ys):
        vec_x = x - base_x
        vec_y = y - base_y
        scalar = vec_x * dir_x + vec_y * dir_y  # Dot product
        scalars.append(scalar)
    
    return scalars, m, base_x, base_y
