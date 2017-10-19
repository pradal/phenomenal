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
import numpy

from openalea.phenomenal.data_structure import (
    VoxelSegment)

import openalea.phenomenal.segmentation_3D.plane_interception
# ==============================================================================


class VoxelOrgan(object):

    def __init__(self, label):
        self.voxel_segments = list()
        self.label = label
        self.info = dict()

    def add_voxel_segment(self, voxels_position, polyline):
        self.voxel_segments.append(VoxelSegment(voxels_position, polyline))

    def voxels_position(self):

        voxels_position = set()
        for voxel_segment in self.voxel_segments:
            voxels_position = voxels_position.union(
                voxel_segment.voxels_position)

        return voxels_position

    def longest_polyline(self):
        long_polyline = list()

        for vs in self.voxel_segments:
            if len(vs.polyline) > len(long_polyline):
                long_polyline = vs.polyline

        return long_polyline

    def get_highest_polyline(self):

        highest_polyline = list()
        z_max = float("-inf")
        for vs in self.voxel_segments:
            z = numpy.max(numpy.array(vs.polyline)[:, 2])

            if z > z_max:
                z_max = z
                highest_polyline = vs

        return highest_polyline

    def real_longest_polyline(self):

        voxels_position = set(self.voxels_position())

        long_polyline = list()

        for vs in self.voxel_segments:
            if len(vs.polyline) > len(long_polyline):
                long_polyline = vs.polyline

        index_position_tip = -1
        index_position_base = len(long_polyline) - 1
        for i in range(len(long_polyline) - 1, -1, -1):
            if long_polyline[i] not in voxels_position:
                index_position_base = i
                break

        real_polyline = long_polyline[index_position_base:index_position_tip]

        return real_polyline

    def get_closest_nodes(self):

        voxels_position = numpy.array(map(tuple, list(self.voxels_position())))

        closest_nodes, planes_equation = (
            openalea.phenomenal.segmentation_3D.
            plane_interception.compute_closest_nodes_with_planes(
                voxels_position,
                self.longest_polyline(),
                dist=4,
                without_connexity=True))

        return closest_nodes


