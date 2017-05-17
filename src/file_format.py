#!/usr/bin/env python
#
# Copyright (c) 2016-2017 Fraunhofer Institute for Manufacturing Engineering and Automation (IPA)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from operator import itemgetter
from sets import Set
import re
import sys
import os.path
import os
import subprocess
import rospkg
import fnmatch
import yaml
import readline
import glob
from autocomplete import AutoComplete


# Function for user input completion of the current path
def complete_path(text, state):
    return (glob.glob(text + '*') + [None])[state]


# Important global variables
rospack = rospkg.RosPack()

try:
    this_pkg_path = rospack.get_path('ipa_code_refactoring')
except Exception as e:
    print "Unable to find ROS Package with name 'ipa_code_refactoring'."
    sys.exit()

# set autocompletion to ros packages
try:
    autocomplete = AutoComplete(rospack.list())
except Exception, e:
    print "Unable to get ROS Package List."
    sys.exit()

readline.set_completer_delims(' \t\n;')
readline.set_completer(complete_path)
readline.parse_and_bind('tab: complete')

print
print "Supply the executable for your clang formater:"

user_input = raw_input("[clang-format-3.8]:  ")
clang = user_input if user_input != "" else "clang-format-3.8"
exec_policy = {'cpp': ' -name "*.h" -or -name "*.hpp" -or -name "*.cpp" | xargs ' + clang + ' -i -style=file',  # CPP
               'py': ' -name "*.py" | xargs autopep8 --global-config ' + this_pkg_path + '/cfg/pep8.cfg'}       # Python

if len(sys.argv) < 2:
    print 'You need to provide a file type. Program shutting down now.'
    sys.exit()
elif len(sys.argv) > 2:
    os.system('cp ' + this_pkg_path + '/cfg/.clang-format ' + sys.argv[2])

file_type = sys.argv[1]


print
print "1)  Do you want to \n\t[a] Format all files within the 'src' Folder \n\t[b] Format all files in certain ROS packages \n\t[c] Format all files within a repository"

user_input = raw_input("Choice:  ")

if user_input in ['a', 'A']:
    print "\n2)  Please enter the full path to your 'src' folder:"
    input_src_path = raw_input("Path:  ")
    os.system('find ' + input_src_path + exec_policy.get(file_type))
    print "Formatted all files in:  '" + input_src_path + "'\n"

elif user_input in ['b', 'B']:
    readline.set_completer(autocomplete.complete)
    print "\n2)  Specify the ROS packages you want to format (quit by entering [q/Q]):"
    input_ros_pkg = raw_input("ROS Package:  ")

    while input_ros_pkg not in ['q', 'Q']:
        # try to find ros package by name
        try:
            ros_pkg_path = rospack.get_path(input_ros_pkg)
        except Exception, e:
            print "Can't find ROS Package with name '" + input_ros_pkg + "', please try another one."
            continue

        # format all files according to the selected file type
        os.system('find ' + ros_pkg_path + exec_policy.get(file_type))
        print "Formatted all files in:  '" + ros_pkg_path + "'\n"

        # read in new ros package
        input_ros_pkg = raw_input("ROS Package:  ")

elif user_input in ['c', 'C']:
    print "\n2)  Please enter the full path to your 'src' folder:"
    input_src_path = raw_input("Path:  ")
    if not os.path.isdir(input_src_path):
        print "Path does not exist. Program will shut down now."
        sys.exit()

    autocomplete.set_options(next(os.walk(input_src_path))[1])
    readline.set_completer(autocomplete.complete)
    print "3)  Specify the repositories you want to format (quit by entering [q/Q]):"
    input_repo_name = raw_input("Repository:  ")

    while input_repo_name not in ['q', 'Q']:
        if not os.path.isdir(input_src_path + '/' + input_repo_name):
            print "Path does not exist, please try again."
        else:
            # format all files according to the selected file type
            repo_path = (input_src_path + '/' + input_repo_name).replace('//', '/')
            os.system('find ' + repo_path + exec_policy.get(file_type))
            print "Formatted all files in:  '" + repo_path + "'\n"

        # read new repo
        input_repo_name = raw_input("Repository:  ")

else:
    print "Error! Wrong character, program is shutting down now."

print "\nProgram is shutting down now."
