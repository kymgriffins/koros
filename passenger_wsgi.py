import os
import sys

# Add the project directory to Python path for cPanel
sys.path.insert(0, os.path.dirname(__file__))

from bns.wsgi import application
