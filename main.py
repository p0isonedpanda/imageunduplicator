import cv2
import numpy as np
import os
from copy import deepcopy

# only find pngs and throw them into a list
images = list(filter(lambda i: '.png' in i, os.listdir()))

while images:
    i = images.pop(0)
    orig = cv2.imread(i) # read in the file we want to compare against

    checkImages = deepcopy(images) # get copy of list for our comparisons
    removed = [] # used to track things we need to remove
    while checkImages:
        m = checkImages.pop(0)
        check = cv2.imread(m)

        # similarity checking
        if orig.shape == check.shape and not(np.bitwise_xor(orig, check).any()):
            print(i + ' and ' + m + ' are the same')
            removed.append(m)
            os.remove(m)

    for r in removed:
        images.remove(r)

print('done!')
