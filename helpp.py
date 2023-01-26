def size(topon):
    l_c = list(map(float, topon['boundedBy']['Envelope']['lowerCorner'].split()))
    u_c = list(map(float, topon['boundedBy']['Envelope']['upperCorner'].split()))

    shi, dol = u_c[0] - l_c[0], u_c[1] - l_c[1]
    return [str(shi), str(dol)]
