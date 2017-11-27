import inspect
import os
import sys

# Add the parent directory to the path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
print(parentdir)
sys.path.insert(0, parentdir)

# Import from the parent directory
import api
