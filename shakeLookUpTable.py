import numpy
theTable = numpy.ones(256)

theTable[0] = 63
theTable[1] = theTable[0]
theTable[2] = 75
theTable[3] = 84
theTable[4] = 90
theTable[5] = 95
theTable[6] = 103
theTable[7] = theTable[6]
for i in range(8, 11):
    theTable[i] = 113
for i in range(11, 16):
    theTable[i] = 126
for i in range(16, 21):
    theTable[i] = 134
for i in range(21, 31):
    theTable[i] = 149
for i in range(31, 41):
    theTable[i] = 160
for i in range(41, 51):
    theTable[i] = 169
for i in range(51, 61):
    theTable[i] = 177
for i in range(61, 81):
    theTable[i] = 191
for i in range(81, 101):
    theTable[i] = 201
for i in range(101, 121):
    theTable[i] = 211
for i in range(121, 141):
    theTable[i] = 220
for i in range(141, 161):
    theTable[i] = 227
for i in range(161, 181):
    theTable[i] = 234
for i in range(181, 201):
    theTable[i] = 240
for i in range(201, 221):
    theTable[i] = 246
for i in range(221, 241):
    theTable[i] = 251
for i in range(241, 255):
    theTable[i] = 253
theTable[255] = 255


def B(x):
    return theTable[x]
