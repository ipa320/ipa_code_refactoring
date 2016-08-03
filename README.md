# IPA Code Refactoring

This repository contains several scripts as well as binaries for code refactoring according to ros 
coding guidelines. The scripts and their corresponding functionalities are listed below:

1. **[cpp_format](#1-cpp_format)**: Format h/hpp/cpp files according to ros-cpp coding guidelines (http://wiki.ros.org/CppStyleGuide)  
2. **[py_format](#2-py_format)**: Format h/hpp/cpp files according to ros-cpp coding guidelines (http://wiki.ros.org/PyStyleGuide)  
3. **[file_format.py](#3-file_formatpy)**: The script called by cpp_format and py_format  
4. **[clang_format](#4-clang_format)**: The binary called by file_format.py for cpp-files  
5. **[param_update.py](#5-param_updatepy)**: Updates ros-parameter names and values automatically as well as manually  

#### Important:
Please use an extra pull request for any changes made to a repository using these scripts. There will 
be a lot of automatically driven changes which can be erroneous sometimes. As a conclusion, pull requests 
containing changes made by these scripts should be reviewed carefully.


## 1. cpp_format
---
### Functionality

Auto-formatting all cpp-files found in either the src-directory, a ros package or a whole 
repository. This includes e.g. indents, braces, comments, maximum line length, etc.

### How to use it

1. Call 'rosrun ipa_code_refactoring cpp_format' to run the script without using any parameters.  
2. Follow the given instructions to either  
  1. format the whole src folder  
  2. format all files within the chosen ROS packages  
  3. format all files within the chosen repositories (inside 'src' folder)

### How to configure it

The formatting properties are specified within the '.clang-format' file in the YAML language. At the
beginning of each call, this fill will be copied to the current users home directory. The script than 
expects all *src*-folders to be below this home folder. Otherwise the configurations specified in the 
'.clang-format' file won't be applied.
The specification of the Clang-Format Style Options can be found under the following link:
  
http://clang.llvm.org/docs/ClangFormatStyleOptions.html

#### Important:
You further you need to specify the paths to your ros workspaces at the beginning of the 
'file-format' file.


## 2. py_format
---
### Functionality

Auto-formatting all python-files found in either the src-directory, a ros package or a whole 
repository. Further it installs/upgrades the versions of 'pycodestyle' (python code checker) and
'autopep8' (python auto code formatter). These two are needed to auto-format the code.

### How to use it

1. Call 'rosrun ipa_code_refactoring py_format' to run the script without using any parameters.  
2. Follow the given instructions to either  
  1. format the whole src folder  
  2. format all files within the chosen ROS packages  
  3. format all files within the chosen repositories (inside 'src' folder)

### How to configure it

The python functionality is not yet implemented but the specification of the autopep Options can 
be found under the following link:
  
https://pypi.python.org/pypi/autopep8


## 3. file_format.py
---
### Functionality
Offers the possibilty to execute a code formatting script/binary on all finds found for a certain file 
extension.

### How to use it

This is just the script that is executed by 'cpp-format' as well as 'py-format' scripts.
It gets a parameter specifying which files are supposed to be formatted. It distingueshes 
between 'cpp' and 'py'. Further refactoring scripts could be included in the same way.


## 4. param_update.py
---
### Functionality

This binary is called by the file_format.py for formatting cpp-files. You can also call it directly to 
format a single file.


### How to use it

1. Call 'rosrun ipa_code_refactoring clang_format -i -style=file' followed by a file path to format a single file



## 5. param_update.py
---
### Functionality

This script is able to compare all parameter initializations in the _common.cpp, _ros.cpp, .cfg 
and .yaml file of a package regarding a consistent naming (snake_case) and identical values, if 
existing. It updates all parameter names according to the occurrences found in the _common.cpp file.
Further the values used in _ros.cpp are updated by the ones found in .cfg if they are different.
Values in .yaml files are not changed. 
The script allows to also manually modify all found parameters and their regarding values. 
In the end it is possible to choose whether the parameters missing in some files are printed out
on screen or saved to a file. 

### How to use it

1. Call 'rosrun ipa_code_refactoring param_update' without any parameters
2. Follow the given instructions to  
  1. specify the ros pkg name and optionally a different file name
  2. update parameter names and values  
  3. print or save missing parameters to file  
  4. open all edited files in sublime

### How to configure it

The configuration is loaded from the file 'cfg/param_update.yaml' and is currently only suitable for the bride 
structure as given in the *ipa_navigation_localization* package. The script expects the following naming conventions 
for the different files:

- in package 'x'
  - common-file: 'n'_common.cpp / 'n'.cpp
  - ros-file: 'n'_ros.cpp
  - cfg-file: 'n'.cfg

With 'x' being the package name (first parameter) and 'n' being the filename (optional second 
parameter).
The default path and naming for yaml files is set to:
  
    ../ipa_navigation_config/config/components/'n'.yaml

Where 'n' is the filename, specified during the call of the script.