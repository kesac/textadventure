
# PROTOTYPE

import mapgen
import mapvis
import shell


map = mapgen.create_dfs_map(10,10)

shell.start(map)
mapvis.visualize(map)