# -*- python -*-
#
#       Copyright 2015 INRIA - CIRAD - INRA
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
# ==============================================================================
import cv2
import glob
import os

import openalea.deploy.shared_data
import alinea.phenomenal

from alinea.phenomenal.calibration.chessboard import (
    Chessboard)

from alinea.phenomenal.calibration.calibration import (
    CalibrationCameraSideWith2Target,
    CalibrationCameraTop)

from alinea.phenomenal.multi_view_reconstruction.formats import (
    read_xyz)
# ==============================================================================

__all__ = ["plant_1_images",
           "plant_1_images_binarize",
           "plant_1_chessboards",
           "plant_1_calibration_camera_side",
           "plant_1_calibration_camera_top",
           "plant_1_voxel_centers"]

# ==============================================================================


def plant_1_images():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    data_directory = shared_directory + '/plant_1/images/'
    files_path = glob.glob(data_directory + '*.png')
    files_name = [os.path.basename(path) for path in files_path]

    angles = map(lambda x: int((x.split('.png')[0])), files_name)

    images = dict()
    for i in range(len(files_path)):
        images[angles[i]] = cv2.imread(files_path[i], cv2.IMREAD_UNCHANGED)

    return images


def plant_1_images_chessboard():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    data_directory = shared_directory + '/plant_1/images_chessboard/'
    files_path = glob.glob(data_directory + '*.png')
    files_name = [os.path.basename(path) for path in files_path]

    angles = map(lambda x: int((x.split('.png')[0])), files_name)

    images_chessboard = dict()
    for i in range(len(files_path)):
        images_chessboard[angles[i]] = cv2.imread(
            files_path[i], cv2.IMREAD_UNCHANGED)

    return images_chessboard


def plant_1_images_binarize():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    data_directory = shared_directory + '/plant_1/images_binarize/'
    files_path = glob.glob(data_directory + '*.png')
    files_name = [os.path.basename(path) for path in files_path]

    angles = map(lambda x: int((x.split('.png')[0])), files_name)

    images = dict()
    for i in range(len(files_path)):
        images[angles[i]] = cv2.imread(files_path[i], cv2.IMREAD_GRAYSCALE)

    return images


def plant_1_mask_mean_shift():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    file_path = shared_directory + '/plant_1/mask/mask_mean_shift.png'

    mask_mean_shift = cv2.imread(file_path, flags=cv2.IMREAD_UNCHANGED)

    return mask_mean_shift


def plant_1_mask_hsv():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    file_path = shared_directory + '/plant_1/mask/mask_hsv.png'

    mask_hsv = cv2.imread(file_path, flags=cv2.IMREAD_UNCHANGED)

    return mask_hsv


def plant_1_mask_clean_noise():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    file_path = shared_directory + '/plant_1/mask/mask_clean_noise.png'

    mask_clean_noise = cv2.imread(file_path, flags=cv2.IMREAD_UNCHANGED)

    return mask_clean_noise


def plant_1_mask_adaptive_threshold():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    file_path = shared_directory + '/plant_1/mask/mask_adaptive_threshold.png'

    mask_adaptive_threshold = cv2.imread(file_path, flags=cv2.IMREAD_UNCHANGED)

    return mask_adaptive_threshold


def plant_1_mask_elcom_mean_shift():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    file_path = shared_directory + '/plant_1/mask/mask_elcom_mean_shift.png'

    mask_elcom_mean_shift = cv2.imread(file_path, flags=cv2.IMREAD_UNCHANGED)

    return mask_elcom_mean_shift


def plant_1_mask_elcom_hsv():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    file_path = shared_directory + '/plant_1/mask/mask_elcom_hsv.png'

    mask_elcom_hsv = cv2.imread(file_path, flags=cv2.IMREAD_UNCHANGED)

    return mask_elcom_hsv


def plant_1_mask_hsv_roi_main():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    file_path = shared_directory + '/plant_1/mask/mask_hsv_roi_main.png'

    mask_hsv_roi_main = cv2.imread(file_path, flags=cv2.IMREAD_GRAYSCALE)

    return mask_hsv_roi_main


def plant_1_mask_hsv_roi_band():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    file_path = shared_directory + '/plant_1/mask/mask_hsv_roi_band.png'

    mask_hsv_roi_band = cv2.imread(file_path, flags=cv2.IMREAD_GRAYSCALE)

    return mask_hsv_roi_band


def plant_1_mask_hsv_roi_pot():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    file_path = shared_directory + '/plant_1/mask/mask_hsv_roi_pot.png'

    mask_hsv_roi_pot = cv2.imread(file_path, flags=cv2.IMREAD_GRAYSCALE)

    return mask_hsv_roi_pot


def plant_1_background_hsv():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    file_path = shared_directory + '/plant_1/mask/background_hsv.png'

    background_hsv = cv2.imread(file_path, flags=cv2.IMREAD_COLOR)

    return background_hsv


def plant_1_chessboards():

    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    data_directory = shared_directory + '/plant_1/'

    chess_1 = Chessboard.load(
        data_directory + 'chessboard_2013-07-11_15-49-42_vis_wide_chess_1')

    chess_2 = Chessboard.load(
        data_directory + 'chessboard_2013-07-11_15-49-42_vis_wide_chess_2')

    return chess_1, chess_2


def plant_1_calibration_camera_side():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    data_directory = shared_directory + '/plant_1/'
    file_path = data_directory + 'calibration_camera_side'

    return CalibrationCameraSideWith2Target.load(file_path)


def plant_1_calibration_camera_top():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    data_directory = shared_directory + '/plant_1/'
    file_path = data_directory + 'calibration_camera_top'

    return CalibrationCameraTop.load(file_path)


def plant_1_params_camera_opencv_path():
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    data_directory = shared_directory + '/plant_1/'

    params_camera_opencv_path = data_directory + 'params_camera_opencv'

    return params_camera_opencv_path


def plant_1_voxel_centers(voxel_size=10):
    shared_directory = openalea.deploy.shared_data.shared_data(
        alinea.phenomenal)

    data_directory = shared_directory + '/plant_1/'

    if 3 <= int(voxel_size) <= 20:
        path = data_directory + 'voxel_centers_size_' + str(int(voxel_size))
        return read_xyz(path)

    return None

