from os import path
import os
import subprocess
import numpy as np

DATA_PATH = "D:\\YoukuVideoTest\\"
test_dirs = []

def png2y4m():

    print("Working path: ", DATA_PATH)
    lr_y4m = os.walk(DATA_PATH)

    # find test video directory
    for root,dirs,filename in lr_y4m:
        print('root:',root)
        if dirs:
            test_dirs = dirs
            print("Found {} video directories".format(np.array(dirs).shape[0]))
            print('dirs:',dirs)
            break

    # creat folder for video
    dir_path = path.join(DATA_PATH,'submit_videos')
    if not path.exists(dir_path):
        os.mkdir(dir_path)

    # convert png to y4m
    for item in test_dirs:

        # process SR video
        SR_video_path = path.join(dir_path, 'Youku_'+ item +'_l' )
        SR_pic_path = path.join(DATA_PATH,item)

        video_path = SR_video_path + '.y4m'
        SR_pic = SR_pic_path + "/%3d.png"
        print('SR_pic:', SR_pic)
        print("Processing {} ...".format(item))
        cmd_str = 'ffmpeg -i ' + SR_pic + ' -pix_fmt yuv420p -vsync 0 ' + video_path + ' -y'
        p = subprocess.Popen(cmd_str, shell=True)
        p.wait()
#
if __name__ == "__main__":
    png2y4m()
