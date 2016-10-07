import os
import subprocess
import sys


def create_project():
    base_python_project_dir = "/home/rbs/www/python/"
    project_name = input("Enter python project name: ")
    full_path = base_python_project_dir + project_name

    try:
        if not os.path.exists(full_path):

            # create project directory
            os.makedirs(full_path)
            print("Creating project folder...OK")

            # initialize git repository
            
            pr = subprocess.Popen("/usr/bin/git init", cwd=full_path,
                                  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("Creating git repository...OK")
            (out, error) = pr.communicate()
            out = str(out.decode("utf-8"))
            error = str(error.decode("utf-8"))

            if error != "":
                print(error)

            print(out)
            

    except OSError:
        sys.exit('Fatal: output directory "' + full_path +
                 '" does not exist and cannot be created')
