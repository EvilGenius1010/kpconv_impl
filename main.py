import numpy as np

def normalize(points):
    centroid = points.mean(axis=0)
    points -= centroid
    scale = np.max(np.linalg.norm(points, axis=1))
    return points / scale


# def conv(curr_point,neigbors,features_at_neigbor,weights):

# # Create kernel centres
# def farthest_point_sampling(points,num_samples) 
#     N,_ = points.shape


# test the code
def farthest_point_sampling(points, num_samples):
    N, _ = points.shape
    selected_pts = np.zeros((num_samples,), dtype=int)
    distances = np.ones((N,)) * 1e10

    # Pick the first point randomly
    selected_pts[0] = np.random.randint(N)
    cur_point = points[selected_pts[0]]

    for i in range(1, num_samples):
        dist = np.linalg.norm(points - cur_point, axis=1)
        distances = np.minimum(distances, dist)
        selected_pts[i] = np.argmax(distances)
        cur_point = points[selected_pts[i]]

    return points[selected_pts]