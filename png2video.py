import cv2
import os
import tqdm

path = 'D:\\CNNtest\\AliSR\\srgan-1.2.0\\samples\\evaluate\\'
filelist = os.listdir(path)
out = cv2.VideoWriter('Youku_00239_l.avi', cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'), 24, (1920,1080))
for item in filelist:
    if item.endswith('.png'):
        # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        item = path + item
        img = cv2.imread(item)
        out.write(img)

out.release()
cv2.destroyAllWindows()

