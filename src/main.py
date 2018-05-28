import sys
import src.drawing.json_to_figures as js
import src.common as cm

if len(sys.argv) == 4:
    if sys.argv[2] == "-o":
        cm.FILE_NAME = sys.argv[3]
    else:
        cm.handle_error("Incorrect arguments.")
elif len(sys.argv) != 2:
    cm.handle_error("Incorrect number of arguments.")

if sys.argv[1] == "None":
    js.json_to_figures(None)
else:
    js.json_to_figures(sys.argv[1])

# import sys
#
# sys.path.insert(0, "/home/kuba/Workspace/Python/project-2/src/drawing/colours.py")
# sys.path.insert(1, "/home/kuba/Workspace/Python/project-2/src/drawing/draw.py")
# sys.path.insert(2, "/home/kuba/Workspace/Python/project-2/src/drawing/json_to_figures.py")
# sys.path.insert(3, "/home/kuba/Workspace/Python/project-2/src/json/is_correct.py")
# sys.path.insert(4, "/home/kuba/Workspace/Python/project-2/src/json/operations.py")
#
# import os.path
#
# from drawing import json_to_figures
