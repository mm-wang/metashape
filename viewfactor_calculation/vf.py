import rhinoscriptsyntax as rs
import Rhino as rc
import pprint
import scriptcontext as sc


""" Calculate View Factor

"""
class ViewFactor(object):
    def __init__(self):
        self.sphere_nested = []
        self.cpt = []
    def process_raw_inputs(self,sphere_tree_in,cpt_lst_in):
        self.cpt = cpt_lst_in
        # convert tree to nested list
        for i in range(sphere_tree_in.BranchCount):
            branchList = sphere_tree_in.Branch(i)
            self.sphere_nested.append(branchList)

        # convert guids to brep
        for i in xrange(len(self.sphere_nested)):
            sphere_per_bld = list(self.sphere_nested[i])
            for j in xrange(len(sphere_per_bld)):
                sphere_per_bld[j] = rs.coerce3dpoint(sphere_per_bld[j])
            self.sphere_nested[i] = sphere_per_bld

    def ray_cast(self,srf2int):
        """
        base_vector
        direction_vector
        srf2int
        """
        for i in xrange(self.sphere_nested):
            sphere_pt = self.sphere_nested[i]
            r0 = self.cpt#base_vector
            r1 = self.sphere#direction_vector

            ray = rc.Geometry.Ray3d(r0,r1)
            point_intersect_lst = rc.Geometry.Intersect.Intersection.RayShoot(ray,[srf2int],1)
            if point_intersect_lst:
                point_intersect_lst = list(point_intersect_lst)
                #debug.extend(point_intersect_lst)
                #debug.append(self.cpt)
        return point_intersect_lst

vf = ViewFactor()
vf.process_raw_inputs(sphere_tree_in, cpt_lst_in)
vf.ray_cast(srf2int_int)

sphere_out = vf.sphere_nested
cpt_out = vf.cpt
