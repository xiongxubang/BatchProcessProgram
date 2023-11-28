import pandas as pd
import os

def script_generator(params_path, file_name = "script.sh"):  
    with open(file_name, "w") as f:
        table = pd.read_csv(params_path, index_col=0)   # read the hyperParam.csv file using pandas

        # Note that there is something wrong with command 'cd'. Please refer to the link: https://blog.csdn.net/robertaqi/article/details/6578449
        for row_num in table.index:
            f.write(f"cd ./{row_num}\n")
            f.write("python ./run.py;\n")
            f.write("cd ..\n")
        
    os.system(f"chmod +x {file_name}")

    

if __name__ == "__main__":
    # change the work dir path
    working_dir_path = os.path.abspath(os.path.dirname(__file__))
    os.chdir(working_dir_path)      # change to the dir containing instanceGenerator.py
    
    with open("./bpp_config/files_path.txt", "r") as f:
        lines = f.read().splitlines()   # read all lines
        params_path = lines[0]          # input table   
        file_name = lines[4]
        
    script_generator(params_path, file_name)


