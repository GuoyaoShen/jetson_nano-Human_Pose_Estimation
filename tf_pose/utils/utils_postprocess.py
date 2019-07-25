'''
(c) GuoyaoShen
'''

import cv2
import numpy as np

idx_face_max = 0

def get_gesture_hello(list_centers):
    '''
    :param list_centers: a list of human joints coords, each ele is a dict
    :return:
    '''
    # check human points
    for idx, centers in enumerate(list_centers):
        print('CENTERS', centers)
        if ((4 in centers) and (1 in centers)):
            if (centers[4][1] < centers[1][1]):
                print(
                    '==============================================HELLO RIGHT==================================================')
        if ((7 in centers) and (1 in centers)):
            if (centers[7][1] < centers[1][1]):
                print(
                    '==============================================HELLO LEFT===================================================')

def show_face_imgs(img_orig, list_faceboxes, tuple_facesz=(128,128), scalar_face=1):
    '''
    :param img_orig: orig image, np array
    :param list_faceboxes: list, each ele is a dict
    :param tuple_facesz: tuple of the size of target face window
    :param scalar_face: a scalar used to adjust the face window
    :return:
    '''
    # show face img
    global idx_face_max
    print('LIST MAX', idx_face_max)
    H = img_orig.shape[0]
    W = img_orig.shape[1]
    if list_faceboxes != []:  # face list not empty
        print('NOT NONE LIST')

        len_idx = len(list_faceboxes)
        if len_idx > idx_face_max:
            idx_face_max = len_idx

        for idx_face, face_box in enumerate(list_faceboxes):
            name_face = 'face img ' + str(idx_face)
            if face_box != None:
                H_face_low = int(max(face_box['y'] - face_box['h'] * scalar_face, 0))
                H_face_high = int(min(face_box['y'] + face_box['h'] * scalar_face, H))
                W_face_low = int(max(face_box['x'] - face_box['w'] * scalar_face, 0))
                W_face_high = int(min(face_box['x'] + face_box['w'] * scalar_face, W))

                image_face = img_orig[H_face_low:H_face_high, W_face_low:W_face_high]
                image_face = cv2.resize(image_face, tuple_facesz)
                print('FACE SHOWING..........')
                cv2.imshow(name_face, image_face)
            else:
                cv2.imshow(name_face, np.zeros(tuple_facesz))

        for idx in range(len_idx, idx_face_max):
            name_face = 'face img ' + str(idx)
            cv2.imshow(name_face, np.zeros(tuple_facesz))

    else:
        print('EMPTY FACE LIST')
        for idx in range(idx_face_max):
            name_face = 'face img ' + str(idx)
            cv2.imshow(name_face, np.zeros(tuple_facesz))

    return idx_face_max
