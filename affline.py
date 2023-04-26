import string

def inverse(n):
    for i in range(26):
        if n*i%26 == 1:
            return i

def affline_decrypt(a, b, c):
    return inverse(a)*((c-b)%26)%26

if __name__ == '__main__':
    d = {}
    for i in range(26):
        d[string.ascii_lowercase[i]] = i 

    cyphertext = [d[c.lower()] for c in input("cypher text:")]

    for a in (1,3,5,7,9,11,15,17,19,21,23,25):
        for b in range(26):
            print(a)
            print(b)
            for i in cyphertext:
                print(string.ascii_lowercase[affline_decrypt(a, b, i)], end ='')
            print()

# ex:
# cyphertext: OGHYLXEEQOGWNYJYGHYNKESOETHFYOGLOGHYLXEEPLEIQWYHEXEDYKESJELYDYLIELY
# a=11, b=6
# plain text: 
# waterloo i was defeated 
# you won the war 
# waterloo promise to love you forever more
