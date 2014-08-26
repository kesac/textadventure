
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
print()

map = mapgen.create_dfs_map(20,20)


solid     = "  "
visitable = "[]"

print(solid * (len(map) + 2))

for i in map:
    print(solid, end="")
    for j in i:
        if j.name == None:
            print(solid, end="")
        else:
            print(visitable, end="")
    print(solid)
    
print(solid * (len(map) + 2))
    