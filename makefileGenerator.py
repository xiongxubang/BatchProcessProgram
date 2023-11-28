import pandas as pd
import os

def makefile_generator(params_path):
    with open("makefile", "w") as f:
        f.write("run:\n")
        table = pd.read_csv(params_path, index_col=0)   # read the hyperParam.csv file using pandas
        for row_num in table.index:
            f.write(f"\tpython ./{row_num}/run.py;\n")
    

if __name__ == "__main__":
    # change the work dir path
    working_dir_path = os.path.abspath(os.path.dirname(__file__))
    os.chdir(working_dir_path)      # change to the dir containing instanceGenerator.py
    
    params_path = "./hyperParam.csv"    # input table
    makefile_generator(params_path)


