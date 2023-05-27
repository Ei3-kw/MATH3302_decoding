import string

def char2index(c):
    return string.ascii_letters.index(c)

def index2char(i):
    return string.ascii_letters[i]

def fiboLFSR(seed, taps, step, outputs):
    outputs.append(seed[-1])
    seed = f"{sum(int(seed[t-1]) for t in taps)%2}{seed[:-1]}"
    if step <= 0:
        return seed, int(''.join(outputs), 2)
    else:
        return fiboLFSR(seed, taps, step-1, outputs)

if __name__ == '__main__':
    codeword = 'WezrjB tRPGbAfS dGLXp bvjahTdC'.replace(" ", "")
    seed = '0000110011100101'
    taps = [3,5,11,16]
    plaintext = ''

    for c in codeword:
        seed, key = fiboLFSR(seed, taps, 7, [])
        plaintext += index2char((char2index(c)-key)%52)

    print(plaintext)