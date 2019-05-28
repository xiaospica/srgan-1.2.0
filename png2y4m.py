import glob
from os import path
import os
import subprocess

# setting
IF_PAIR = False
DATA_PATH = "D:\\CNNtest\\AliSR\\SRdata\\youku_00200_00249_l\\"
# DATA_PATH = "./data/round1/valid/"

def y4mtopng(if_pair,dir):
    """convert y4m video to frame image
    if_pair: without(test data) groud truth hr video, please set IF_PAIR to False
    dir: data directory
    """
    print("Working path: ",DATA_PATH)
    lr_y4m = glob.glob(DATA_PATH + "Youku_*_l.y4m")
    print("Found {} lr y4m video".format(len(lr_y4m)))
    for item in lr_y4m:

        # create folder
        dir = item.split('_')[1]
        dir_path = path.join(DATA_PATH,dir)
        if not path.exists(dir_path):
            os.mkdir(dir_path)

        # create lr folder for png file
        lr_dir_path = path.join(dir_path,'lr')
        if not path.exists(lr_dir_path):
            os.mkdir(lr_dir_path)

        # process lr video
        png_reg = lr_dir_path + "/%3d.png"
        print("Processing {} ...".format(item))
        cmd_str = "ffmpeg -i " + item + " -vsync 0 " + png_reg + " -y"
        p = subprocess.Popen(cmd_str, shell=True)
        p.wait()

        if if_pair:

            # create hr folder for png file
            hr_dir_path = path.join(dir_path,'hr')
            if not path.exists(hr_dir_path):
                os.mkdir(hr_dir_path)

            # process lr video
            tmp = item.split('_')
            tmp[2] = "h_GT.y4m"
            hr_item = ('_').join(tmp)
            png_reg = hr_dir_path + "/%3d.png"
            print("Processing {} ...".format(hr_item))
            cmd_str = "ffmpeg -i " + hr_item + " -vsync 0 " + png_reg + " -y"
            p = subprocess.Popen(cmd_str, shell=True)
            p.wait()


if __name__ == "__main__":
    y4mtopng(IF_PAIR,DATA_PATH)



