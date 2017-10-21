import rhinoscriptsyntax as rs
import Rhino as rc
import scriptcontext as sc


""" Calculate View Factor

"""
class ViewFactor(object):
    def __init__(self):
        self.sphere_nested = []
        self.cpt = []
        self.bound_nested = []
        self.bld_num = None
        self.ray_num = None
        # Outputs
        self.raycast_distance = None
        self.raycast_pt_x = None
        self.raycast_pt_y = None
        self.raycast_pt_z = None

    def process_raw_inputs(self,sphere_tree_in,bound_srf_lst_in,cpt_lst_in):
        self.cpt = map(lambda c: rs.coerce3dpoint(c), cpt_lst_in)
        # convert tree to nested list of sphere pts
        for i in range(sphere_tree_in.BranchCount):
            branchList = sphere_tree_in.Branch(i)
            self.sphere_nested.append(branchList)

        # convert tree to nested list of bound srfs
        for i in range(bound_srf_lst_in.BranchCount):
            branchList = bound_srf_lst_in.Branch(i)
            branchList = map(lambda s: rs.coercebrep(s), branchList)
            self.bound_nested.append(branchList)

        # convert guids to rc points
        for i in xrange(len(self.sphere_nested)):
            sphere_per_bld = list(self.sphere_nested[i])
            for j in xrange(len(sphere_per_bld)):
                sphere_per_bld[j] = rs.coerce3dpoint(sphere_per_bld[j])
            self.sphere_nested[i] = sphere_per_bld

        self.bld_num = len(self.sphere_nested)
        self.ray_num = len(self.sphere_nested[0])

    def ray_cast(self):
        """
        base_vector
        direction_vector
        srf2int
        """
        self.ray_int_nested = []
        self.ray_dist_nested = []

        for i in xrange(self.bld_num):
            raypts = []
            raydist = []
            for j in xrange(self.ray_num):
                srf2int_lst = self.bound_nested[i]
                r0 = self.cpt[i] #base_vector
                r1 = self.sphere_nested[i][j] #direction_vector
                #convert pts to vectors
                r1 = rc.Geometry.Vector3d(r1) - rc.Geometry.Vector3d(r0)

                ray = rc.Geometry.Ray3d(r0,r1)
                point_intersect_lst = rc.Geometry.Intersect.Intersection.RayShoot(ray,srf2int_lst,1)
                if point_intersect_lst:
                    point_intersect_lst = list(point_intersect_lst)
                    rpt = point_intersect_lst[0]
                    raypts.append(rpt)
                    raydist.append(rs.Distance(rpt,r0))
                    #rc.Geometry.Vector3d.Multiply(
            self.ray_dist_nested.append(raydist)
            self.ray_int_nested.append(raypts)
        #print len(self.ray_int_nested)
    def generate_viewfactor_matrix(self):
        # flip the matrix
        self.raycast_distance = map(lambda r: [None] * self.ray_num, [None] * self.bld_num)

        self.raycast_x = map(lambda r: [None] * self.ray_num, [None] * self.bld_num)
        self.raycast_y = map(lambda r: [None] * self.ray_num, [None] * self.bld_num)
        self.raycast_z = map(lambda r: [None] * self.ray_num, [None] * self.bld_num)
        #self.header_lst = []
        self.ray_mtx = []
        for i in xrange(self.bld_num):
            self.bld_lst = []
            for j in xrange(self.ray_num):
                d = self.ray_dist_nested[i][j]
                x = self.ray_int_nested[i][j][0]
                y = self.ray_int_nested[i][j][1]
                z = self.ray_int_nested[i][j][2]
                #self.header = "BLD_{a}_RAY_{b}".format(a=i,b=j)

                self.bld_lst.extend([d,x,y,z])

                #self.ray_dist_nested[i][j]
                #self.raycast_distance[i][j]
            self.ray_mtx.append(self.bld_lst)

vf = ViewFactor()
vf.process_raw_inputs(sphere_tree_in, bound_srf_lst_in, cpt_lst_in)
vf.ray_cast()
vf.generate_viewfactor_matrix()
print len(vf.ray_mtx)
print len(vf.bld_lst)

#sphere_out = vf.sphere_nested
#cpt_out = vf.cpt


ray_mtx = vf.ray_mtx

ray_out = reduce(lambda x,y: x+y, vf.ray_int_nested)
