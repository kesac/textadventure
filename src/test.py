
# PROTOTYPE

import mapgen
import mapvis
import shell


map = mapgen.create_dfs_map(6,6)

shell.start(map)
mapvis.visualize(map)