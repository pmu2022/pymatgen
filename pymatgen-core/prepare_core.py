import shutil
import os

# Copy pymatgen core folders from parent
# (This is probably unnecessary, just for prototyping)
shutil.copytree("../pymatgen/core", "pymatgen/core")
shutil.copytree("../pymatgen/util", "pymatgen/util")
os.remove("pymatgen/core/__init__.py")
os.remove("pymatgen/util/__init__.py")