import os



def run(cfg):
    # create the file
    abs_path = os.path.join(os.path.dirname(__file__), f"../data/{cfg.Data_Name}")
    abs_path = os.path.abspath(abs_path)
    os.system(f"ln -s {abs_path} ./{cfg.Data_Name}")

    with open("config.txt", "w") as f:
        f.write(str(cfg.Data_Name)+'\n')
        f.write(str(cfg.Data_Size)+'\n')
        f.write(str(cfg.Para2)+'\n')
        f.write(str(cfg.Para3)+'\n')
        f.write(str(cfg.Para4)+'\n')

    os.system("chmod +x ../src/sort")
    os.system("../src/sort")

    # after
    ans = []
    with open('time.txt',"r") as f:
        lines = f.read().splitlines()
        for line in lines:
            line = line.split(sep=" ")
            temp = float(line[0])+float(line[1])
            ans.append(str(temp))
    with open('time.txt',"w") as f:
        for line in ans:
            f.write(line+'\n')


    