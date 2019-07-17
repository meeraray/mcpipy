# mcpipy
My projects made in McPiPy, the library that lets you run python scripts to change your Minecraft worlds

Followed [this tutorial](https://www.instructables.com/id/Python-coding-for-Minecraft/) to set up. The Minecraft version is 1.9. Make sure to choose this when downloading Forge and running Minecraft. Also, use the [latest release of the Raspberry Jam mod](https://github.com/arpruss/raspberryjammod/releases).

They said to put your files in the same directory as the Python library files. However, I wanted to put them in a separate folder. The work around is to add the folder with the McPiPy files to the system path.

You can do that by adding the path of your file in setup.py:

```
import sys
sys.path.insert(0, '<insert absolute path of folder here>')
```

and then putting

```
import setup
```

before you import project files

```
from mine import *
```
