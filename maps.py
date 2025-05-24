# These are maps of the game.
import random

LEVEL1_MAPS = [
    [
        list("################"),
        list("#P#  #####     #"),
        list("# #  #      o  #"),
        list("# ####   ### ###"),
        list("#           E  #"),
        list("#   ############"),
        list("#              #"),
        list("################"),
    ],

    [
        list("################"),
        list("#P             #"),
        list("#############  #"),
        list("##             #"),
        list("##    o ########"),
        list("###  ###########"),
        list("###           E#"),
        list("################"),
    ],

    [
        list("################"),
        list("#              #"),
        list("####o#######   #"),
        list("#              #"),
        list("###    ####  E #"),
        list("#      #  #    #"),
        list("########  #   P#"),
        list("################"),
    ]
]
LEVEL2_MAPS = [
    [
        list("################"),
        list("#P             #"),
        list("#              #"),
        list("#              #"),
        list("#            E #"),
        list("## ###         #"),
        list("# ?  #         #"),
        list("################"),
    ],

    [
        list("################"),
        list("#P####? #  #   #"),
        list("# #     #  #   #"),
        list("# #  #  #  #   #"),
        list("# #  #  #    E #"),
        list("# #  #     #   #"),
        list("#    # # #######"),
        list("################"),
    ],

    [
        list("################"),
        list("#P#            #"),
        list("# ###########  #"),
        list("#         ? #  #"),
        list("# ###########E##"),
        list("#              #"),
        list("#  ###### ######"),
        list("################"),
    ],
]

def select_map(pool):

    raw = random.choice(pool)
    new_map = []
    i = 0
    while i < len(raw):
        row = []
        j = 0
        while j < len(raw[i]):
            row.append(raw[i][j])
            j += 1
        new_map.append(row)
        i += 1
    return new_map

