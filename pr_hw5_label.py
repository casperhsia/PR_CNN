from keras.preprocessing import image
import numpy as np
import glob
import os
import ntpath

def load_data():
    for folderPath in glob.glob('./pr_dataset_HW5/*'):
        filePath = glob.glob(folderPath+'/*')
        for item in filePath[:int(len(filePath) * 0.8)]:
            folder = "./data/train/"+ntpath.basename(ntpath.dirname(item))
            if not os.path.exists(folder):
                os.makedirs(folder)
            target = folder+"/"+ntpath.basename(item)
            os.rename(item, target)
        for item in filePath[int(len(filePath) * 0.8):]:
            folder = "./data/validation/"+ntpath.basename(ntpath.dirname(item))
            if not os.path.exists(folder):
                os.makedirs(folder)
            target = "./data/validation/"+ntpath.basename(ntpath.dirname(item))+"/"+ntpath.basename(item)
            os.rename(item, target)

if __name__ == '__main__':
    load_data()
