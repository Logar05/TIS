from collections import Counter
def encode(vhod: list) -> tuple[list, list]:
    S = []
    for i in range (256):
        S.append(i)
    
    zap = []
    for i in range(len(vhod)):
        zap.append(ord(vhod[i]))
    while True:
        pari = []
        for i in range(len(zap) - 1):
            pari.append((zap[i], zap[i + 1]))
        freq = Counter(pari)
        max_par = None
        max_freq = 0
        for i in range (len(zap) - 1):
            par = (zap[i], zap[i+1])
            if freq[par] > max_freq:
                max_freq = freq[par]
                max_par = par
        if len(S) >= 4096:
            break
        if max_freq < 2:
            break
        newList = []
        S.append(max_par)
        max_ix = len(S) - 1
        i = 0
        while i < len(zap):
            if i + 1 < len(zap) and (zap[i], zap[i+1]) == max_par:
                newList.append(max_ix)
                i = i + 2
            else:
                newList.append(zap[i])
                i = i + 1
        zap = newList
    return (zap, S)

def decode(vhod: list, S: list) -> list:
    zap = []
    for i in range(len(vhod)):
        zap.append(vhod[i])
    
    i = len(S) - 1
    
    while i >= 256:
        newList = []
        for j in range(len(zap)):
            if zap[j] == i:
                par = S[i]
                newList.append(par[0])
                newList.append(par[1])
            else:
                newList.append(zap[j])
        zap = newList
        i = i - 1
    izhod = []
    for i in range(len(zap)):
        izhod.append(chr(zap[i]))
    return izhod

def compute_compression_ratio(vhod: list, izhod:list, mode: str) -> float:
    vhodSize = len(vhod)
    izhodSize = len(izhod)
    if izhodSize == 0:
        return float('nan')
    R = float((vhodSize * 8) / (izhodSize * 12))
    return R

