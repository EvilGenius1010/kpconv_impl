def normalize(points):
    centroid = points.mean(axis=0)
    points -= centroid
    scale = np.max(np.linalg.norm(points, axis=1))
    return points / scale
