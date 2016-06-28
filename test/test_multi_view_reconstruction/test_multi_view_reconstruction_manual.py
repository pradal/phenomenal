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
from alinea.phenomenal.calibration.calibration_manual import (
    EnvironmentCamera,
    CalibrationCameraManual)

from alinea.phenomenal.data_plants.data_creation import (
    build_object_1,
    build_images_1)

from alinea.phenomenal.multi_view_reconstruction.multi_view_reconstruction\
    import (project_voxel_centers_on_image,
            reconstruction_3d,
            error_reconstruction)
# ==============================================================================


def test_multi_view_reconstruction_manual_1():
    # ==========================================================================
    size = 10
    voxel_size = 10
    world_coordinate = (0, 0, 0)

    voxel_centers, _ = build_object_1(size, voxel_size, world_coordinate)

    # ==========================================================================
    env_feat = EnvironmentCamera()
    calibration = CalibrationCameraManual(env_feat)

    images_projections = list()
    shape_image = (2454, 2056)
    for angle in range(0, 360, 30):

        projection = calibration.get_projection(angle)

        img = project_voxel_centers_on_image(voxel_centers,
                                             voxel_size,
                                             shape_image,
                                             projection)

        images_projections.append((img, projection))

    # ==========================================================================
    voxel_size = 20
    voxel_centers = reconstruction_3d(images_projections,
                                      voxel_size=voxel_size,
                                      verbose=True)

    print len(voxel_centers)
    assert len(voxel_centers) == 216
    volume = len(voxel_centers) * voxel_size**3
    assert volume == 1728000


def test_multi_view_reconstruction_manual_2():

    voxel_size = 1

    env_feat = EnvironmentCamera()
    calibration = CalibrationCameraManual(env_feat)

    images = build_images_1()

    images_projections = list()
    for angle in range(0, 360, 30):
        projection = calibration.get_projection(angle)
        img = images[angle]
        images_projections.append((img, projection))

    voxel_centers = reconstruction_3d(
        images_projections, voxel_size=voxel_size, verbose=True)

    print len(voxel_centers)

    for image, projection in images_projections:
        err = error_reconstruction(
            image, projection, voxel_centers, voxel_size)

        print 'err : ', err
        assert err < 6000

# ==============================================================================

if __name__ == "__main__":
    test_multi_view_reconstruction_manual_1()
    test_multi_view_reconstruction_manual_2()
