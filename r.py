def recursiveSheep(x, howExcitedisthesheep):
    if len(x) > howExcitedisthesheep:
        return x
    else:
        return recursiveSheep(x+"a", howExcitedisthesheep)

print(recursiveSheep("b", 9001))