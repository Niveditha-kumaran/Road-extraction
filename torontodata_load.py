import scipy.misc
from glob import glob
import numpy as np
import matplotlib.pyplot as plt

class DataLoader():
    def __init__(self, dataset_name, img_res=(128, 128)):
        self.dataset_name = dataset_name
        self.img_res = img_res
    
    def genlistsfortarget(self,batchA,dtype):
        halfname= ('./datasets/torontomap/%s/target\\'%(dtype))
        listgen=[]
        for i in batchA:
            var= str(i)
            var1= var.split('\\')
            newname= halfname + var1[1]
            listgen.append(newname)
        return listgen

    
    def load_data(self, batch_size=1, is_testing=False):
        data_type = "train" if not is_testing else "test"
        #path = glob('./datasets/%s/%s/*' % (self.dataset_name, data_type))
        path1 = glob('./datasets/%s/%s/input/*' % (self.dataset_name, data_type))
        path2 = glob('./datasets/%s/%s/target/*' % (self.dataset_name, data_type))

        batch_images1 = np.random.choice(path1, size=batch_size)
        batch_images2 = self.genlistsfortarget(batch_images1, data_type)
        imgs_A = []
        imgs_B = []
       
        for img_path1 in batch_images1:
            img1 = self.imread(img_path1)
            img_A= img1
            img_A = scipy.misc.imresize(img_A, self.img_res)
            imgs_A.append(img_A)
           
        
        for img_path2 in batch_images2:
            img2 = self.imread(img_path2)
            img_B= img2
            img_B = scipy.misc.imresize(img_B, self.img_res)
            imgs_B.append(img_B)
           

        imgs_A = np.array(imgs_A)/127.5 - 1.
        imgs_B = np.array(imgs_B)/127.5 - 1.

        return imgs_B, imgs_A


    def imread(self, path):
        return scipy.misc.imread(path, mode='RGB').astype(np.float)