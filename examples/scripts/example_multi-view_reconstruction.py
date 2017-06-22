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
import time

from alinea.phenomenal.display import (
    DisplayVoxelPointCloud)

from alinea.phenomenal.data_structure import (
    ImageView)

from alinea.phenomenal.multi_view_reconstruction import (
    reconstruction_3d)

from alinea.phenomenal.data_access.plant_1 import (
    plant_1_images_binarize,
    plant_1_calibration_camera_side,
    plant_1_calibration_camera_top)

# ==============================================================================


if __name__ == '__main__':

    images = plant_1_images_binarize()

    calibration_side = plant_1_calibration_camera_side()
    calibration_top = plant_1_calibration_camera_top()

    # Select images
    image_views = list()
    for angle in range(0, 360, 30):
        projection = calibration_side.get_arr_projection(angle)
        image_views.append(ImageView(images[angle],
                                     projection,
                                     inclusive=False))

    projection = calibration_top.get_arr_projection(0)
    image_views.append(ImageView(images[-1],
                                 projection,
                                 inclusive=True))

    t0 = time.time()
    voxels_size = 8
    error_tolerance = 1
    vpc = reconstruction_3d(image_views,
                            voxels_size=voxels_size,
                            error_tolerance=error_tolerance,
                            verbose=True)

    print("Number of voxel : {number_voxel}".format(
        number_voxel=len(vpc)))
    print(time.time() - t0)

    # Viewing
    dvpc = DisplayVoxelPointCloud()
    dvpc.show(vpc, color=(0.1, 0.9, 0.1))
