import sys

if sys.platform.startswith("win"):
    from .win_utils import *
else:
    from .nx_utils import *