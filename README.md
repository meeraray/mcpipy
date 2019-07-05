# mcpipy
My projects made in McPiPy, the library that lets you run python scripts to change your Minecraft worlds

Followed [this tutorial](https://www.instructables.com/id/Python-coding-for-Minecraft/) to set up. The Minecraft version is 1.8.

They said to put your files in the same directory as the Python library files. However, I wanted to put them in a separate folder. The work around is to add the folder with the McPiPy files to the system path.

You can do that by adding this to the top of every program:

```
import sys
sys.path.insert(0, 'C:/Users/ronuk/AppData/Roaming/.minecraft/mcpipy')
```

before you import project files

```
from mine import *
```
