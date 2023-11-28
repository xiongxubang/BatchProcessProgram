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
1. Input Files (Format of those files can be found in Appendix) <br>
   1. By default, we have file "hyperParam.csv" for the configuration of hyper-parameters. <br>
   2. "bpp_config/files_path.txt", which stores the names of the input/output files. In gereral, there is no need to modify the content in this file. <br>
   3. "bpp_config/annotations.txt", which contains the output files of the algorithm, and the corresponding metrics. <br>
2. Output Files (Format of those files can be found in Appendix) <br>
   1. "result.csv", which aggregates the result from each instance, based on the contents of "bpp_config/annotations.txt". <br>
  
## Appendix A. Format of "hyperParam.csv"
The first line corresponds to the names of hyper-parameters. Then, each following line corresponds to a set of hyper-parameters. <br>
The format of the line is <br>
>  , <para.1> <para.2> ... <--- names of hyper-parameters <br>
> 1, <value 1.1>, <value 1.2> ... <--- the hyper-parameters for the first instance <br>
> 2, <value 2.1>, <value 2.2> ... <--- the hyper-parameters for the second instance <br>




