import pandas as pd
import os
import json
from tqdm import tqdm



def importData():
    PATH = "Migros_case/products/products_en/en/"
    file_list = os.listdir(PATH)

    data = pd.DataFrame()

    for file in tqdm(file_list[:3]):            #Takes 20 mins. Don't run often!
        data_open = open(PATH + file, encoding="utf8").read()
        temp = pd.json_normalize(json.loads(data_open))
        data  = data._append(temp, ignore_index = True)
