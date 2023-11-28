# BatchProcessProgram
A useful plugin.

## Usage Step
1. Change to the working directory "BatchProcessProgram" (i.e., the current directory containing README.md). <br>
2. Install the required packages. <br>
```
pip install -r requirements.txt
```
3. Modify the hyperparameter in "hyperParam.csv". <br>
4. Create the instances. <br>
```
python instanceGenerator.py
```
5. Create the scripts and run the program. <br>
```
python makefileGenerator.py
make run
```
6. Aggregate the output results. All the results corresponding to the hyperparameter in "hyperParam.csv" will be output to the file "result.csv". <br>
```
python resultGenerator.py
```

## Input/Output Files
1. Directory "data", which contains the datasets.
2. Directory "src", which contains the source codes.
3. Directory "bpp_config", which contains the configuration files.
4. Input Files (Format of those files can be found in Appendix) <br>
   1. By default, we have file "hyperParam.csv" for the configuration of hyper-parameters. <br>
   2. "bpp_config/files_path.txt", which stores the names of the input/output files. In gereral, there is no need to modify the content in this file. <br>
   3. "bpp_config/annotations.txt", which contains the output files of the algorithm, and the corresponding metrics. <br>
5. Output Files (Format of those files can be found in Appendix) <br>
   1. "result.csv", which aggregates the result from each instance, based on the contents of "bpp_config/annotations.txt". <br>

  
## Appendix A. Format of "hyperParam.csv"
The first line corresponds to the names of hyper-parameters. Then, each following line corresponds to a set of hyper-parameters. <br>
The format of the line is <br>
>  , <para.1> <para.2> ... <--- names of hyper-parameters <br>
> 1, <value 1.1>, <value 1.2> ... <--- the hyper-parameters for the first instance <br>
> 2, <value 2.1>, <value 2.2> ... <--- the hyper-parameters for the second instance <br>


## Appendix B. Format of Configure File "bpp_config/files_path.txt"
Each line corresponds to a path of input/output files. <br>
> 1. The path of the file for the configuration of hyper-parameters (e.g., "hyperParam.csv")
> 2. The path of the executable program of the source code (e.g., "src/run.py").
> 3. The path of the config file for each instance in yaml style (e.g., "config.yaml").
> 4. The path of the aggregated result file (e.g., "result.csv").


## Appendix C. Format of Configure File "bpp_config/annotations.txt"
Each line corresponds to an output file in each instance. It means that it could be found in each instance directory. Please note that the name of file could contain \<space\>. Each element in each line is separated by \<tab\>. <br>
The format of the line is <br>
> <file 1> <metric 1.1> ... <--- The first output file and its corresponding metric <br>
> <file 2> <metric 2.1> <metric 2.2>... <--- The second output file and its corresponding metric <br>


## Appendix D. Format of "result.csv"
The first line corresponds to the names of hyper-parameters and the metrics. Then, each following line corresponds to a set of hyper-parameters and a set of results. <br>
The format of the line is <br>
>  , <para.1> <para.2> ... <metric.1> <metric.2> ... <--- names of hyper-parameters <br>
> 1, <value 1.1>, <value 1.2> ... <result 1.1> <result 1.2> ... <--- the hyper-parameters and results for the first instance <br>
> 2, <value 2.1>, <value 2.2> ... <result 2.1> <result 2.2> ... <--- the hyper-parameters and results for the second instance <br>




