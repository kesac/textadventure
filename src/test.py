
# PROTOTYPE

import mapgen
import mapvis
import textgen
import textwrap

room = mapgen.Location()
room.name = "Zamafradar Room"
room.description = textgen.describe(room)

header = "You are currently in [%s]" % room.name
print("-" * len(header))
print(textwrap.fill(header))
print("-" * len(header))
print(textwrap.fill(room.description))
print()

map = mapgen.create_dfs_map(10,10)
mapvis.visualize(map)