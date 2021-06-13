# pip3 install pillow
# pip3 install numpy

import os
import sys

from PIL import Image
import numpy as np

# K-means
def initialize_K_centroids(X, K):
    """ Choose K points from X at random """
    m = len(X)
    return X[np.random.choice(m, K, replace=False), :]


def find_closest_centroids(X, centroids):
    m = len(X)
    c = np.zeros(m)
    for i in range(m):
        # Find distancesfind_k_means
        distances = np.linalg.norm(X[i] - centroids, axis=1)

        # Assign closest cluster to c[i]
        c[i] = np.argmin(distances)

    return c

def compute_means(X, idx, K):
    _, n = X.shape
    centroids = np.zeros((K, n))
    for k in range(K):
        examples = X[np.where(idx == k)]
        mean = [np.mean(column) for column in examples.T]
        centroids[k] = mean
    return centroids


def find_k_means(X, K, max_iters=10):
    centroids = initialize_K_centroids(X, K)
    previous_centroids = centroids
    for _ in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_means(X, idx, K)
        if (centroids == previous_centroids).all():
            # The centroids aren't moving anymore.
            return centroids, 0
        else:
            previous_centroids = centroids

    return centroids, idx

# Get the image
try:
    image_path = sys.argv[1]
    assert os.path.isfile(image_path)
except (IndexError, AssertionError):
    print('Please specify an image')

def load_image(path):
    """ Load image from path. Return a numpy array """
    image = Image.open(path)
    return np.asarray(image) / 255


from os import listdir
from os.path import isfile, join

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-i", "--inputPath",default="/Users/rachelchen/Desktop/father's web/3rd/")
parser.add_argument("-o", "--outputPath", default="/Users/rachelchen/Desktop/father's web/compressed/")
# the desired number of colors in the compressed image
parser.add_argument("-k", "--kcluster",default=20)
parser.add_argument("-m", "--maxiters",default=20)

args = parser.parse_args()

inputPath =args.inputPath
outputPath = args.outputPath
K = args.kcluster
MAX_ITERS = args.maxiters

onlyfiles = [f for f in listdir(inputPath) if isfile(join(inputPath, f))]

for fileName in onlyfiles:
    image = load_image(inputPath+fileName)
    if(len(image.shape)==3):
        w, h, d = image.shape
        print('{} Image found with width: {}, height: {}, depth: {}'.format(fileName,w, h, d))
        X = image.reshape((w * h, d))
        colors, _ = find_k_means(X, K, max_iters=MAX_ITERS)
        idx = find_closest_centroids(X, colors)
        idx = np.array(idx, dtype=np.uint8)
        X_reconstructed = np.array(colors[idx, :] * 255, dtype=np.uint8).reshape((w, h, d))
    else:
        w, h = image.shape
        print('{} Image found with width: {}, height: {}'.format(fileName,w, h))
        X = image
        colors, _ = find_k_means(X, K, max_iters=MAX_ITERS)
        idx = find_closest_centroids(X, colors)
        idx = np.array(idx, dtype=np.uint8)
        X_reconstructed = np.array(colors[idx, :] * 255, dtype=np.uint8).reshape((w, h))

    compressed_image = Image.fromarray(X_reconstructed)
    compressed_image.save(outputPath+fileName)
