
import mapgen
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

map = mapgen.create_dfs_map(10,10)

for i in map:
    for j in i:
        if j.name == None:
            print("* ", end="")
        else:
            print("  ", end="")
    print("")