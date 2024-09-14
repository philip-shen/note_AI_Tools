from _libs.logger_setup import *
import os,glob
import re
import csv
import pandas as pd

__all__ = [
#
    'format_time',
    'Query_all_files_in_dir',
    'splitFullFileName',
    'getFileNameOnly',
    'Diff_List',

]

def format_time(timesec):
    m, s = divmod(timesec, 60)
    h, m = divmod(m, 60)
    str_format_time= ''
    if h == 0:
        if m == 0:
            str_format_time= "%02ds" % (s)
            #return "%02ds" % (s)
        else:
            str_format_time= "%02dm%02ds" % (m, s)
            #return "%02dm%02ds" % (m, s)
    else:
        str_format_time= "%dh%02dm%02ds" % (h, m, s)
        #return "%dh%02dm%02ds" % (h, m, s)

    return str_format_time, h, m, s

def walk_in_dir(dir_path,file_type,opt_verbose='OFF'):
    ret_listOfFileNames = []
    
    for filename in glob.glob(os.path.join(dir_path, file_type)):
        listOfFileNames = []

        listOfFileNames = filename
        ret_listOfFileNames.append(listOfFileNames)

        
        if opt_verbose.lower() == "on":
            msg = "fileName:{} in directory:{}"
            logger.info(msg.format(filename, dir_path))
             
            msg = "listOfFileNames:{} in walk_in_dir"
            logger.info(msg.format(listOfFileNames))        

    for dirname in (d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d)) ):
        walk_in_dir(os.path.join(dir_path, dirname),file_type)
        
    if opt_verbose.lower() == "on":
        msg = "number of listOfFileNames:{} in walk_in_dir"
        logger.info(msg.format( len(ret_listOfFileNames) ))
        msg = "ret_listOfFileNames:{} in walk_in_dir"
        logger.info(msg.format(ret_listOfFileNames))        

    return ret_listOfFileNames
class Query_all_files_in_dir:

    def __init__(self,dir_path, file_type, opt_verbose='OFF'):
        self.dir_path= dir_path
        self.file_type= file_type
        self.opt_verbose= opt_verbose
        self.ret_listOfFileNames= []
        self.cnt_path_raw_ML_dataset = 0
        self.all_path_raw_ML_dataset= []
        
    def walk_in_dir(self):

        for filename in glob.glob(os.path.join(self.dir_path, self.file_type)):
            listOfFileNames = []

            listOfFileNames = filename
            self.ret_listOfFileNames.append(listOfFileNames)

            if self.opt_verbose.lower() == "on":
                msg = "fileName:{} in directory:{}"
                logger.info(msg.format(filename, self.dir_path))
             
                msg = "listOfFileNames:{} in walk_in_dir"
                logger.info(msg.format(listOfFileNames))      

        for dirname in (d for d in os.listdir(self.dir_path) if os.path.isdir(os.path.join(self.dir_path, d)) ):
            walk_in_dir(os.path.join(self.dir_path, dirname), self.file_type, self.opt_verbose)

        '''
        number of self.ret_listOfFileNames:8 in walk_in_dir
        '''        
        '''
        self.ret_listOfFileNames:['/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-13_144554.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-13_164632.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-13_184703.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-13_193507.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-13_200110.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-13_220142.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-14_000214.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-14_020246.log'] in walk_in_dir
        '''
        if self.opt_verbose.lower() == "on":
            msg = "number of self.ret_listOfFileNames:{} in walk_in_dir"
            logger.info(msg.format( len(self.ret_listOfFileNames) ))
            msg = "self.ret_listOfFileNames:{} in walk_in_dir"
            logger.info(msg.format(self.ret_listOfFileNames))        

        return self.ret_listOfFileNames    
    
    '''
    Z:/xxxx/MA\2022-08-19_TWS_MA.txt
    Z:/xxxx/ML\2022-08-19_ML_TWS_MA.txt
    '''
    def get_ML_filename(self, fileName):
        temp1 = fileName[0:11]
        temp2 = fileName[11::]
    
        if self.opt_verbose.lower() == 'on':
            logger.info(f'temp1: {temp1}; temp2: {temp2}')
    
        self.raw_ML_dataset = temp1+'ML_'+temp2    

    def get_path_ML_filename(self, path_txt_file, reg_date_str):
        path = os.path.dirname(path_txt_file) 
        fileName = os.path.basename(path_txt_file)
        path_ML = os.path.dirname(path)+'/'+'ML'
        
        if bool(re.match(reg_date_str, fileName)):
            self.get_ML_filename(fileName)
            #logger.info(f'path_raw_ML_dataset: {path_ML+"/"+raw_ML_dataset}')
            if os.path.isfile(path_ML+'/'+ self.raw_ML_dataset):
                if self.opt_verbose.lower() == 'on':
                    logger.info(f"path_raw_ML_dataset: {path_ML+'/'+self.raw_ML_dataset}")
                    
                self.cnt_path_raw_ML_dataset += 1
                self.all_path_raw_ML_dataset.append(f"{path_ML+'/'+self.raw_ML_dataset}")
    
    def collect_ML_dataset(self):
        self.output_all_raw_ML_dataset = []
        
        for path_raw_ML_dataset in self.all_path_raw_ML_dataset:            
            '''
            exclude below case:
            1072,144,2,9,24,0,0,0,0,147,248,0,0,0,0,0,0,
            '''
            with open(path_raw_ML_dataset, "r") as f:
                reader = f.readlines()
                if reader[0].split(',').__len__() > 20:
                    self.output_all_raw_ML_dataset.append(reader[0])

        #logger.info(f'output: {output}')
        
    def list_out_file(self, path_filename: str, content: list):
        if self.opt_verbose.lower() == 'on':
            logger.info(f'output file name: {path_filename}')
    
        with open(path_filename, 'w') as f:
            for line in content:
                f.write(f"{line}\n")
    '''
                 0     1    2    3    4    5   6   7   8   9    10   11  12  13  14  15  16  17            18            19            20            21         22  23
    0    2022-04-01  1049    0  244   18   40   0   0   0   0    0  235   0   0   0   0   0   0  17657.759766  17657.759766  17465.609375  17625.589844  3396600.0 NaN
    1    2022-04-06  1049    0  263   11   54   0   0   0   0    0  274   0   0   0   0   0   0  17484.189453  17528.990234  17381.070312  17522.500000  4241200.0 NaN
    2    2022-04-07  1049    0  113    5   14   0   0   0   0    0  477   0   0   0   0   0   0  17430.130859  17438.599609  17178.630859  17178.630859  4863100.0 NaN
    3    2022-04-08  1049  167   56   16   52   0   0   0   0  322   61   0   0   0   0   0   0  17210.400391  17316.689453  17210.400391  17284.539062  3538700.0 NaN
    4    2022-04-11  1049  115   24   12   33   0   0   0   0  450   74   0   0   0   0   0   0  17273.050781  17316.349609  17046.669922  17048.369141  4584600.0 NaN
    ..          ...   ...  ...  ...  ...  ...  ..  ..  ..  ..  ...  ...  ..  ..  ..  ..  ..  ..           ...           ...           ...           ...        ...  ..
    182  2022-12-26  1063  152    7   56  231   0   0   0   0  129  134   0   0   0   0   0   0  14271.200195  14301.110352  14253.200195  14285.129883  1574600.0 NaN
    183  2022-12-27  1063  175    9  101  220   0   0   0   0  101   97   0   0   0   0   0   0  14310.190430  14410.240234  14310.190430  14328.429688  1821100.0 NaN
    184  2022-12-28  1063  107    4   41   39   0   0   0   0  257  213   0   0   0   0   0   0  14249.830078  14249.830078  14119.299805  14173.099609  1958900.0 NaN
    185  2022-12-29  1063  104    4   37   33   0   0   0   0  268  212   0   0   0   0   0   0  14097.509766  14120.570312  13981.629883  14085.019531  1839200.0 NaN
    186  2022-12-30  1063  144    8   97   52   0   0   0   0  210  153   0   0   0   0   0   0  14183.519531  14248.900391  14137.690430  14137.690430  1748100.0 NaN

    [187 rows x 24 columns]
    '''                
    def read_MA_dataset(self, dataset_MA_fname):
        
        self.df_MA_dataset = pd.read_csv(dataset_MA_fname, header=None)
        self.df_MA_dataset.reset_index(inplace=False)
        
def splitFullFileName(fileName):
	"""
	split a full file name into path, fileName and suffix
	@param fileName
	@return a list containing the path (with a trailing slash added), the 
		file name (without the suffix) and the file suffix (without the 
		preceding dot)
	"""
	tmp = fileName.split('/')
	path = '/'.join(tmp[:-1]) + '/'
	fullFileName = tmp[-1]
	tmp2 = fullFileName.split('.')
	fileName = '.'.join(tmp2[:-1])
	suffix = tmp2[-1]
	return path, fileName, suffix

def getFileNameOnly(fileName):
	"""
	return the file name minus the trailing suffix
	"""
	#return '.'.join(fileName.split('/')[-1].split('.')[:-1])
	
	re_fileName= re.split('; |, |\\|\n',fileName)
	return '.'.join(re_fileName[-1].split('.')[:-1])

def Diff_List(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif


        
    