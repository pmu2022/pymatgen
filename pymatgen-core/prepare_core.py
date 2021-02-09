import shutil
import os

shutil.copytree("../pymatgen/core", "pymatgen/core")
shutil.copytree("../pymatgen/util", "pymatgen/util")

# remove __init__.py to make packages implicit namespace packages
os.remove("pymatgen/core/__init__.py")
os.remove("pymatgen/util/__init__.py")
