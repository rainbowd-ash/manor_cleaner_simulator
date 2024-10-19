# Manor Cleaner Simulator
Or, Vacuum World: an exploration of rationality

## Homework for my AI class
What is *rational* at any given moment depends upon four things: the ability to tell between right and wrong (a *performance metric*), everything you can remember, a way to perceive linear time (some events happen before other events), and intimate knowledge of the action-set available in the coming moments.

## How to Run
`python3 manor_cleaner_simulator.py`

## Backstory
In a remote country, you are the last heiress of a doomed house, awaiting salvation. The last remaining manservant has taken the horses and carriage to the capital. He told you that he hopes to appeal to the daughter of a man your father once called friend. Both of your fathers have been dead for years. It's possible she has never heard of your lowly family.

While you wait alone in the dusty manor, cobwebbed in memories, you decide to impersonate the chef and the manservant while cleaning.

## The Goal
The object of the assignment is to create 2 robots and compare their performance. One robot is a "reflex agent" which has a table of percept sequences and along with the action to take based on it. The second robot is random.

The world the robots inhabit is a 3x3 grid of rooms. A room can be dirty or clean. The robots move between the rooms and suck up dirt, converting a dirty room to a clean room.

The robots can see the room they are in, and one room in each cardinal direction. The robots can clean the room they are in. The robots can move to a room in a cardinal direction. The robots do not have a memory.

The robots will be run over a series of trials and scored. After tracking 100 runs for each bot, CHAOS WORLD begins. In CHAOS WORLD a suck action on a clean floor will deposit dirt 25% of the time. Additionally, the robots will misidentify a clean room as dirty (or vice versa) 10% of the time.
