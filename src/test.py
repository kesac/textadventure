
import textwrap
import textgen

class Room:
    def __init__(self):
        self.name = None
        self.description = None
        self.n = None
        self.s = None
        self.e = None
        self.w = None
		



room = Room()
room.name = "Zamafradar Room"
room.description = textgen.get_basic_room_description(room)

header = "You are currently in [%s]" % room.name
print("-" * len(header))
print(textwrap.fill(header))
print("-" * len(header))
print(textwrap.fill(room.description))

