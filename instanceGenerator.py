# Generate a series of instances based on the hyperParam.csv file.
# This .py file should be put in the working directory.
# This program is suggested being running on the Linux platform.
# In the hyperParam.csv file, the we use "." to spilt the tree-based sturcture.

import pandas as pd
import yaml
import os
from src.defaults import get_cfg_defaults

# make a folder on the given path.
def mkdir(path):
    folder = os.path.exists(path)

    # if there is not folder on the given path, the program will create a new one.
    if not folder:
        os.makedirs(path)
        print(f"The sub-folder: {path} is created successful!")


# create the tree-based yaml file based on the csv file (split by ".")
def csv2yaml(row, config_path, csv_path):
    # load the data of the corresponding row 
    table = pd.read_csv(csv_path, index_col=0)              # read the whole csv table
    header = table.columns.values                           # read the name of each column
    data = table.loc[row, :]                                # read the data of the corresponding row 

    # construct a tree-based structural dict
    config = {}
    for col_name in header:                                 # read the header of the table
        value = data[col_name]                              # read the corresponding value
        col_name_split = col_name.split(".")                # split the col_name into several sub-string (i.e., DATA.BATCH_SIZE -> DATA BATCH_SIZE)
        current = config                                    # cite the dict (not copy)
        for idx in range(len(col_name_split)-1):            # create the tree-based dict, and reach the target dict which store the value
            key = col_name_split[idx]
            if key not in current:
                current[key] = {}
            current = current[key]
        key = col_name_split[-1]                            # the last one
        if type(value) == str:
                current[key] = value
        elif type(value.item()) == int:
            current[key] = value.item()
        elif float.is_integer(value.item()):                # is integer
            current[key] = int(value.item())
        else:
            current[key] = value.item()
    
    # save the dict as a .yaml file
    with open(config_path,"w") as f:                  
        yaml.safe_dump(data=config,stream=f)


def instanceGenerator(csv_path="./hyperParam.csv", run_path="src/run.py", config_path="./config.yaml"):
    table = pd.read_csv(csv_path, index_col=0)              # read the whole csv table
    # change to the correct dir
    working_dir_path = os.path.abspath(os.path.dirname(__file__))   # get the absolute path of the directory containing instanceGenerator.py
    os.chdir(working_dir_path)                              # change to the dir containing instanceGenerator.py (i.e., /autoParam)
    
    # create the instances
    for row_num in table.index:
        cfg = get_cfg_defaults()                                # all the experiment parameters
        # create subfolder for each row
        subfolder_path = str(row_num)
        mkdir(subfolder_path)
        os.chdir(subfolder_path)                            # enter the sub-folder
        
        # copy the executable file run.py
        os.system(f'cp {os.path.join(working_dir_path, run_path)} .')

        # generate the config.yaml file
        csv2yaml(row_num, config_path, csv_path=os.path.join(working_dir_path, csv_path))

        # update the experimental parameters based on the row data
        cfg.merge_from_file(config_path)
        
        # save the whole parameters (default+hyperparameters)
        with open(config_path, "w") as f:
            f.write(cfg.dump())   # save config to file

        os.chdir(working_dir_path)                          # return the main working directory


if __name__ == "__main__":
    instanceGenerator()

