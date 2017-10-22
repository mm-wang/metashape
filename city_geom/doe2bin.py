import sys
import os
import cPickle
import pprint

import utilities
#from pandas import pandas



class RealBuild(object):
    def __init__(self):
        self.bin = None
        self.doe_type = None
        self.eui = None
        self.total_energy = None

class doe2bin(object):
    # File path parameter
    DIR_UP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    DIR_CURR_PATH = os.path.abspath(os.path.dirname(__file__))

    def __init__(self):
        self.refDOE = None
        self.refBEM = None
        self.refSchedule = None
        self.model_BIN = None

        self.csv_bld_num = 0
        self.realbuildlst = []


    def read_pickle_inputs(self):
        readDOE_file_path = os.path.join(self.DIR_UP_PATH,"resources","readDOE_4A.pkl")
        readDOE_file = open(readDOE_file_path, 'rb') # open pickle file in binary form
        refDOE = cPickle.load(readDOE_file)
        refBEM = cPickle.load(readDOE_file)
        refSchedule = cPickle.load(readDOE_file)
        readDOE_file.close()

        readMetaPath = os.path.join(self.DIR_UP_PATH,"resources","city_meta_shape.pkl")
        readMeta_file = open(readMetaPath, 'rb') # open pickle file in binary form
        refBIN = cPickle.load(readMeta_file)
        readMeta_file.close()

        self.refDOE = refDOE
        self.refBEM = refBEM
        self.refSchedule = refSchedule
        self.model_BIN = refBIN

    def read_csv_inputs(self):
        def helper_match_type(realtype):
            eui_not_match = True
            for j in xrange(len(self.refDOE)):
                refdoetype = self.refDOE[j].Type.upper().strip()
                #print realtype, refdoetype
                if realtype == refdoetype:
                    eui = self.refDOE[j].EUI
                    eui_not_match = False
                    break
            if not eui_not_match:
                return eui
            else:
                return 200.0

        # Make dir path to epw file
        realCityDataPath = os.path.join(self.DIR_UP_PATH,"resources","MN_Meta_Subset.csv")
        # Open epw file and feed csv data to climate_data
        real_city_rows = utilities.read_csv(realCityDataPath)[1:]
        # pprint.pprint(real_city_csv)
        # sample data set
        #[ '1089745', #binid
        #  '1000020003',
        #  '7',
        #  'Transportation & Utility',
        #  'Y7',
        #  'Selected Government Installations (Excluding Office Buildings, Training Schools, Academic, Garages, Warehouses, Piers, Air Fields, Vacant Land, Vacant Sites, And Land Under Water And Easements)',
        #  'Department of Ports and Terminals',
        #  'Unknown']


        self.csv_bld_num = len(real_city_rows) # from csv

        for i in xrange(self.csv_bld_num):
            real_bld_csv = real_city_rows[i]

            realbuild = RealBuild()
            realbuild.bin = real_bld_csv[0]
            realbuild.doe_type = real_bld_csv[-1]

            realtype_ = realbuild.doe_type.upper().strip()

            #TODO: change \ to better delimeter in csv
            #TODO: swap order of csv for fractional multiplication
            if ":" in realtype_:
                realtypeslst = realtype_.split(":")
                eui1 = helper_match_type(realtypeslst[0])
                eui2 = helper_match_type(realtypeslst[1])
                realbuild.eui = eui1 * 0.75 + eui2 * 0.25
            else:
                realbuild.eui = helper_match_type(realtype_)

            self.realbuildlst.append(realbuild)

        #print self.realbuildlst
        #print len(self.realbuildlst)

    def export_data(self):


        #realbuild_data = {
        #"BIN": map(lambda rb: rb.bin, realbuild),
        #"KWH/M2": map(lambda rb: rb.eui, realbuild),
        #"KWH": map(lambda rb: rb.total_energy, realbuild),
        #"TYPE": map(lambda rb: rb.doe_type, realbuild)
        #}
        #self.df = pd.DataFrame(realbuild_data, columns = ["BIN","KWH/M2","KWH","TYPE"])

        #self.df.to_csv(rb_csv_path)
        # print bin_id, real_doe_type


        rb_csv_path = os.path.join(self.DIR_UP_PATH,"csv","eui_bld.csv")
        cf = open(rb_csv_path,"w")
        cf.write("BIN,KWH/M2,TYPE\n")
        for i in xrange(len(self.realbuildlst)):
            rb = self.realbuildlst[i]
            cf.write("{a},{b},{d}\n".format(
                a = rb.bin,
                b = rb.eui,
                d = rb.doe_type))

        cf.close()

if __name__ == "__main__":
    d2b = doe2bin()
    d2b.read_pickle_inputs()
    d2b.read_csv_inputs()
    d2b.export_data()
