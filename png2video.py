import cv2
import os
from tqdm import tqdm
import numpy as np

path = 'C:\\Users\\richard.xiao\\PycharmProjects\\AliSR\\srgan-1.2.0\\srgan-1.2.0\\samples\\evaluate\\'
filelist = os.listdir(path)

#filehead is 'valid_gen'
filehead = filelist[1].split('_')[0]+'_'+filelist[1].split('_')[1]
file_num = np.array(filelist).shape[0]

out = cv2.VideoWriter('Youku_00239_l.avi', cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'), 24, (1920,1080))

for item in tqdm(range(file_num)):

    # print(item)
    item_path = path + filehead + '_' + str(item) + '.png'
    img = cv2.imread(item_path)
    out.write(img)
    print(item_path)

out.release()
cv2.destroyAllWindows()
