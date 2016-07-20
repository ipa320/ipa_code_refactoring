===================================================================================================

                                       ipa_code_refactoring

===================================================================================================

This package contains several scripts as well as binaries for code refactoring according to 
ros-cpp/ros-py guidelines 
(http://wiki.ros.org/CppStyleGuide). The scripts and their corresponding functionality are listed
below.





##########################################
###########     cpp-format     ###########
##########################################

Functionality
-------------------------------
Auto-formatting all cpp-files found in either the src-directory, a ros package or a whole 
repository.



How to use it
-------------------------------
1)  Call 'roslaunch ipa_code_refactoring clang_format.launch' to launch the script without using
    any parameters.

2)  Follow the given instructions to either 
      (1) format the whole src folder
      (2) format all files within the chosen ROS packages
      (3) format all files within the chosen repositories (inside 'src' folder)




How to configure it
-------------------------------
The formatting properties are specified within the '.clang-format' file in the YAML language.
The specification of the Clang-Format Style Options can be found under the following link:
  
    http://clang.llvm.org/docs/ClangFormatStyleOptions.html

IMPORTANT:
You further you need to specify the paths to your ros workspaces at the beginning of the 
'file-format' file.




##########################################
############     py-format     ###########
##########################################

Functionality
-------------------------------
Auto-formatting all python-files found in either the src-directory, a ros package or a whole 
repository. Further it installs/upgrades the versions of 'pycodestyle' (python code checker) and
'autopep8' (python auto code formatter). These two are needed to auto-format the code.



How to use it
-------------------------------
1)  Call 'roslaunch ipa_code_refactoring py_format.launch' to launch the script without using
    any parameters.

2)  Follow the given instructions to either 
      (1) format the whole src folder
      (2) format all files within the chosen ROS packages
      (3) format all files within the chosen repositories (inside 'src' folder)



How to configure it
-------------------------------
The python functionality is not yet implemented but the specification of the autopep Options can 
be found under the following link:
  
    https://pypi.python.org/pypi/autopep8





##########################################
###########     file-format     ##########
##########################################

Functionality
-------------------------------
Offers a possibilty to execute a formatting function on all finds found for a certain file 
extension.



How to use it
-------------------------------
This is just the script that is executed by 'cpp-format' as well as 'py-format' scripts.
It gets a parameter specifying which files are supposed to be formatted. It distingueshes 
between 'cpp' and 'py'.





##########################################
##########     param-update     ##########
##########################################

Functionality
-------------------------------
This script is able to compare all parameter initializations in the _common.cpp, _ros.cpp, .cfg 
and .yaml file of a package regarding a consistent naming (snake_case) and identical values, if 
existing. It updates all parameter names according to the occurrences found in _common.cpp file.
Further the values used in _ros.cpp are updated by the ones found in .cfg if they are different.
Values in .yaml files are not touched. 
The script allows also to manually modify all found parameters and their regarding values. 
In the end it is possible to choose whether the parameters missing in some files are printed out
on screen or saved to a file. 



How to use it
-------------------------------
1)  Call 'roslaunch ipa_code_refactoring param-update.launch' with up to two parameters.
      1. The package name
      2. The name of the node within the package (optional)

2)  Follow the given instructions to
      (1) update parameter names and values
      (2) print or save missing parameters to file
      (3) open all edited files in sublime



How to configure it
-------------------------------
The configuration is already implemented for the ipa_navigation_localization and expects the 
following package structure as well as namings:

- package 'x'
  - cfg
    - 'n'.cfg
  - common
    - 'n'_common.cpp
  - ros
    - 'n'_ros.cpp

With 'x' being the package name (first parameter) and 'n' being the filename (optional second 
parameter).
The default path and naming for yaml files is set to:
  
  ./ipa_navigation/ipa_navigation_config/config/components/'n'.yaml

Where 'n' is the filename, specified during the call of the script.



