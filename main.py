from random import randint
from itertools import combinations
import sys


def generate_random_instances(n):
    existent = list()
    while len(existent) != n:
        num = randint(1, 1000)
        if num not in existent:
            existent.append(num)
    existent.sort()
    return existent


def J(clusters, centroids):
    dist_sum = 0
    i = 0
    for cluster in clusters:
        for instance in cluster:
            dist = (instance - centroids[i])**2
            dist_sum += dist
        i += 1
    return dist_sum


def find_best_centroids(k, instances):
    centroids_candidates = list(combinations(instances, k))
    min_j_value = sys.maxsize

    best_centroids = list()
    best_clusters = list()

    for candidate in centroids_candidates:
        # find separators between centroids
        separators = list()
        separators.append(instances[0])
        for i in range(len(candidate) - 1):
            separators.append(abs(candidate[i] - candidate[i+1]))
        separators.append(instances[len(instances) - 1])

        # initialize each cluster with its centroid
        candidate_clusters = list()
        for _ in candidate:
            candidate_clusters.append([])
        
        # add instances to their closest cluster
        for instance in instances:
            for i in range(len(separators) - 1):
                if separators[i] <= instance < separators[i + 1] + 1:
                    candidate_clusters[i].append(instance)

        # find J value for this case
        j_value = J(candidate_clusters, candidate)
        if j_value < min_j_value:
            min_j_value = j_value
            best_centroids = candidate
            best_clusters = candidate_clusters

    return best_centroids, best_clusters


if __name__ == '__main__':
    instances = generate_random_instances(4)
    print('Instances:', instances)
    
    cents, clusts = find_best_centroids(2, instances)
    print('Centroids:', cents)
    print('Clusters:', clusts)