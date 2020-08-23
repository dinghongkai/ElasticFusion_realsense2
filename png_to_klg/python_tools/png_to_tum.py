import os
import sys
ros_cv2_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'
if ros_cv2_path in sys.path: sys.path.remove(ros_cv2_path)
import cv2



def main():

    data_path = "/raw_image"
    
    num = len(os.listdir(os.path.join(data_path, 'rgb')))

    for i in range(num):
        print('Processing %d ...' % i)
        rgb_img = cv2.imread(os.path.join(data_path, 'rgb/color_%d.png' % i))
        rgb_path = os.path.join(data_path, 'tum/rgb')
        if not os.path.exists(rgb_path):
            os.makedirs(rgb_path)
        cv2.imwrite(os.path.join(rgb_path, '%d.000000.png' % i), rgb_img)

        depth_img = cv2.imread(os.path.join(data_path, 'depth/depth_%d.png' % i), cv2.IMREAD_ANYDEPTH)
        depth_path = os.path.join(data_path, 'tum/depth')
        if not os.path.exists(depth_path):
            os.makedirs(depth_path)
        cv2.imwrite(os.path.join(depth_path, '%d.000000.png' % i), depth_img)

    print('Create txt file ...')
    with open(os.path.join(data_path, 'tum/rgb.txt'), 'w') as f:
        for i in range(num):
            f.write('%d.000000 rgb/%d.000000.png\n' % (i, i))

    with open(os.path.join(data_path, 'tum/depth.txt'), 'w') as f:
        for i in range(num):
            f.write('%d.000000 depth/%d.000000.png\n' % (i, i))

    print('Done!')


if __name__ == '__main__':

    main()