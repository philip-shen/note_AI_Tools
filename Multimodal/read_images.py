'''
Claude3 API使ってみる 2024/03/14
https://zenn.dev/iwatagumi/articles/fa441b7a36e6c0
'''
import base64
import anthropic
import os,sys,time
import pathlib
import glob
import pandas as pd
import argparse
import json
from datetime import datetime
from sys import platform

strabspath=os.path.abspath(sys.argv[0])
strdirname=os.path.dirname(strabspath)
str_split=os.path.split(strdirname)
prevdirname=str_split[0]
dirnamelog=os.path.join(strdirname,"logs")
sys.path.append('./_libs')

from logger_setup import *
import lib_misc

def est_timer(start_time):
    time_consumption, h, m, s= lib_misc.format_time(time.time() - start_time)         
    msg = 'Time Consumption: {}.'.format( time_consumption)#msg = 'Time duration: {:.2f} seconds.'
    logger.info(msg)

def get_png_files(folder_path):
    return glob.glob(f"{folder_path}/*.png")
    
def get_jpg_files(folder_path):
    logger.info(f"Search {folder_path}/*.jpg")
    return glob.glob(f"{folder_path}/*.jpg")


def load_or_create_dataframe(filename):
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    else:
        df = pd.DataFrame(columns=['image_file', 'description'])
    return df


# 画像をbase64にエンコードする
def get_base64_encoded_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()
        base_64_encoded_data = base64.b64encode(binary_data)
        base64_string = base_64_encoded_data.decode('utf-8')
        return base64_string

# processing the images
def process_image(image_path, 
                  prompt= "用300個字描述在圖中的布林通道的趨勢",
                  model = "claude-3-sonnet-20240229",
                  mediatype= "image/jpeg"):
    logger.info(f"\n\n Processing {image_path}\n")

    full_response = ''
    message = client.messages.create(
        model = model,
        max_tokens=1024,
        messages = [
            #{"role": 'system',
            # "content": [{"type": "text", "text": "You are an AI assistant that analyzes images based on the given prompt."}]
            # },

            {"role": 'user',
            "content": [
                {"type": "image", 
                "source": {"type": "base64", 
                            #"media_type": "image/jpeg", 
                            "media_type": mediatype, 
                            "data": get_base64_encoded_image(image_path)}},

                {"type": "text", "text": "用300個字描述在圖中的布林通道的趨勢"}
            ]}    
        ]
    )

    # Print the response to the console and add it to the full response
    logger.info(message.content[0].text)    
    #logger.info(message.content[0].text, end='', flush=True)
    full_response += message.content[0].text

    # Add a new row to the DataFrame
    df.loc[len(df)] = [image_path, full_response]

def process_image_stream(image_path, model,
                  query_text= "用100個字描述在圖中的布林通道的趨勢",
                  mediatype= "image/jpeg"):
    print(f"\n\n Processing {image_path}\n")

    with client.messages.stream(
        model=model,  # モデル指定
        max_tokens=1024,  # 最大トークン数
        messages=[
            {
                "role": "user",
                "content": [
                    *map(lambda x: {"type": "image", 
                                    "source": {
                                        "type": "base64", 
                                        "media_type": "image/jpeg", 
                                        "data": x}}, base64_frames),
                    {
                        "type": "text",
                        "text": prompt
                    }
                ],
            }
        ],
    ) as stream:
        for text in stream.text_stream: 
            print(text, end="", flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test WebDAV for fsspec module')
    parser.add_argument('--conf', type=str, default='config.json', help='Config json')
    args = parser.parse_args()
    
    logger_set(strdirname)
    
    # Get present time
    t0 = time.time()
    local_time = time.localtime(t0)
    msg = 'Start Time is {}/{}/{} {}:{}:{}'
    logger.info(msg.format( local_time.tm_year,local_time.tm_mon,local_time.tm_mday,\
                            local_time.tm_hour,local_time.tm_min,local_time.tm_sec))
    
    json_file= args.conf
    json_path_file = pathlib.Path(strdirname)/json_file
    
    if (not os.path.isfile(json_file))  :
        msg = 'Please check json file:{}  if exist!!! '
        logger.info(msg.format(json_file) )    
        est_timer()
        sys.exit()

    json_data = json.load(json_path_file.open())

    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key=json_data["api_key"],
    )

    
    if platform == "linux" or platform == "linux2":
        home = os.path.expanduser("~")
        images_path= pathlib.Path(f'{home}/{json_data["images_folder"]}')
    elif platform == "darwin":
        pass
    elif platform == "win32":
        images_path= pathlib.Path(f'{json_data["images_folder"]}')
    
    df = load_or_create_dataframe('image_descriptions.csv')

    if json_data["mediatype"] == "image/png":
        image_files = get_png_files(images_path)        
    elif json_data["mediatype"] == "image/jpeg":
        image_files = get_jpg_files(images_path)
    
    mediatype= json_data["mediatype"]

    # image_files.sort()
    image_files.sort(key=lambda k: k[-7:-4])

    logger.info(f"image_files: {image_files}")
    print(df.head())
    
    model = json_data["model"]
    
    for image_file in image_files:
        if image_file not in df['image_file'].values:
            time_process = time.time()
            process_image(image_file, model, mediatype=mediatype)
            est_timer(time_process)
    
    # Save the DataFrame to a CSV file
    csv_filename = 'image_descriptions_{0:%Y%m%d_%H%M%S}.csv'.format(datetime.now())
    df.to_csv(csv_filename, index=False)
    
    est_timer(t0)