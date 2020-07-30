# py-module-benchmark
This is a benchmarking utility tool to measure relative time and memory performance of python functions and programs in **3 easy steps**.

The goal of this tool is to provide an easy to use and general purpose program to determine the runtime and peak memory usage. The tool is built on the standard library to keep it lightweight and hassle free. So, researchers and developers can run the program **without install any additional libraries**.  

# How to use 
The program can be run in these 3 easy steps 

1. Load your code 
2. Choose function or modules to benchmark 
3. Run the benchmark 

### 1. Loading your code 
**Step-1:**  Clone the py-module-benchmarker repository into your local device. 

![cloning the repository](img/1-1.png)

**Step-2:**  Copy the you code under the lib folder. If you just have a function you can put it into the 'module.py' file.

![Copy your code](img/1-2.png)

**Step-3:**  If you have put your own file copied into the lib folder, import them into the run folder.

![Import code](img/1-3.png)

The code importing is very straight forward. The structure of the file import should be:  
```python
from lib.[file_name] import * 
```

or if it's under a folder
```python
from lib.[folder].[file_name] import *
```

### 2. Choosing function or modules 


### 3. Running the Benchmark 