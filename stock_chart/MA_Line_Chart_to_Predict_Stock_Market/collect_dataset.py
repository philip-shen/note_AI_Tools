
import os, sys, time
import argparse
import json, re, pickle
import pathlib

from _libs.lib_misc import *
from _libs.logger_setup import *

strabspath=os.path.abspath(sys.argv[0])
strdirname=os.path.dirname(strabspath)
str_split=os.path.split(strdirname)
prevdirname=str_split[0]
dirnamelog=os.path.join(strdirname,"logs")

def est_timer(start_time):
    time_consumption, h, m, s= format_time(time.time() - start_time)         
    msg = 'Time Consumption: {}.'.format( time_consumption)#msg = 'Time duration: {:.3f} seconds.'
    logger.info(msg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='stock indicator')
    parser.add_argument('--conf_json', type=str, default='config.json', help='Config json')
    parser.add_argument('--gspred_json', type=str, default='xxxx.json', help='Google Sheet Certi json')
    
    args = parser.parse_args()
    
    logger_set(strdirname)
    
    # Get present time
    t0 = time.time()
    local_time = time.localtime(t0)
    msg = 'Start Time is {}/{}/{} {}:{}:{}'
    logger.info(msg.format( local_time.tm_year,local_time.tm_mon,local_time.tm_mday,\
                            local_time.tm_hour,local_time.tm_min,local_time.tm_sec))
    
    json_file= args.conf_json
    
    json_path_file = pathlib.Path(strdirname)/json_file
    
    if (not os.path.isfile(json_file))  :
        msg = 'Please check json file:{}  if exist!!! '
        logger.info(msg.format(json_file) )    
        est_timer(t0)
        sys.exit()

    with open(json_file, encoding="utf-8") as f:
        json_data = json.load(f)  
        
    opt_verbose= 'OFF'
    
    path_raw_dataset_ref = json_data["path_raw_dataset"][0]
    path_raw_dataset_from = json_data["path_raw_dataset"][-1]
    
    raw_dataset_file_type = '*.txt'
        
    '''
    Z:/xxxx/MA\2022-08-19_TWS_MA.txt
    Z:/xxxx/ML\2022-08-19_ML_TWS_MA.txt
    '''
    for idx, _ in enumerate(json_data["reg_date_string_output_fname"]):
        reg_date_string = json_data["reg_date_string_output_fname"][idx][0]
        output_fname =  json_data["reg_date_string_output_fname"][idx][-1]
        path_total_dataset_MA_fname = pathlib.Path(path_raw_dataset_from)/output_fname
        
        local_query_all_files= Query_all_files_in_dir(path_raw_dataset_ref, raw_dataset_file_type, opt_verbose='off')
        list_folder_txt_files= local_query_all_files.walk_in_dir()
        
        for folder_txt_file in sorted(list_folder_txt_files):        
            #logger.info(f"folder_wav_file: {folder_txt_file}")
            #folder, fileName, _ = splitFullFileName(folder_txt_file)
            #logger.info(f'folder: {folder}, fileName: {fileName}')            
            local_query_all_files.get_path_ML_filename(folder_txt_file, reg_date_string)
        
        local_query_all_files.collect_ML_dataset()
        local_query_all_files.list_out_file(path_total_dataset_MA_fname, \
                                            local_query_all_files.output_all_raw_ML_dataset)
        local_query_all_files.read_MA_dataset(path_total_dataset_MA_fname)
        
        logger.info(f'path_total_dataset_MA_fname: {path_total_dataset_MA_fname}')
        logger.info(f'cnt_path_raw_ML_dataset: {local_query_all_files.cnt_path_raw_ML_dataset}')        
        logger.info(f'lengh of all_path_raw_ML_dataset:{local_query_all_files.all_path_raw_ML_dataset.__len__()}')    
        logger.info(f'dataframe of MA dataset:\n{local_query_all_files.df_MA_dataset}')
        
    est_timer(t0)