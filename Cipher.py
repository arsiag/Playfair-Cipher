

class Cipher(object):
    def __init__(self, phrase):
        self.cipher = phrase.upper()
        self.alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        self.mytblstr = []
        self.mytable = []
        self.mytable2 = []
        self.makeTable()

    def __str__(self):
        result = ''
        for i in range(5):
            for j in range(5):
                result = result + self.mytable[i][j] + ' | '
            result = result + '\n-------------------\n'
        return result

    def makeTable(self):
        for c in self.cipher:
            if c.isalpha() and c not in self.mytblstr:
                if c == 'J':
                    if 'I' not in self.mytblstr:
                        self.mytblstr.append('I')
                else:
                    self.mytblstr.append(c)
        for c in self.alphabet:
            if c not in self.mytblstr:
                self.mytblstr.append(c)
        for i in range(5):
            self.mytable.append([self.mytblstr[i*5+j] for j in range(5)])

    def encrypt(self, msg):
        msg = msg.replace(" ","").upper()
        msg = msg.replace("J","I")
        mlen = len(msg)
        encmsg = ''
        k = 0
        while mlen - k > 1:
            pair = msg[k:k+2]
            if pair[0] == pair[1]:
                pair = pair[0] + 'X'
                k -= 1
            cord1 = self.findCordinates(pair[0])
            cord2 = self.findCordinates(pair[1])
            if cord1[0] == cord2[0]: # same row
                newpair = self.rowRule(cord1, cord2)
            elif cord1[1] == cord2[1]: # same col
                newpair = self.colRule(cord1, cord2)
            else:
                newpair = self.recRule(cord1, cord2)
            encmsg = encmsg + newpair
            k += 2
        if mlen - k == 1:
            pair = msg[k:] + 'X'
            cord1 = self.findCordinates(pair[0])
            cord2 = self.findCordinates(pair[1])
            if cord1[0] == cord2[0]:    # same row
                newpair = self.rowRule(cord1, cord2)
            elif cord1[1] == cord2[1]:  # same col
                newpair = self.colRule(cord1, cord2)
            else:                       # rectangle
                newpair = self.recRule(cord1, cord2)
            encmsg = encmsg + newpair
        return encmsg

    def decrypt(self, msg):
        msg = msg.replace(" ", "").upper()
        mlen = len(msg)
        decmsg = ''
        k = 0
        while mlen - k > 1:
            pair = msg[k:k + 2]
            cord1 = self.findCordinates(pair[0])
            cord2 = self.findCordinates(pair[1])
            if cord1[0] == cord2[0]:    # same row
                newpair = self.rowRuleRvrs(cord1, cord2)
            elif cord1[1] == cord2[1]:  # same col
                newpair = self.colRuleRvrs(cord1, cord2)
            else:                       # rectanglee
                newpair = self.recRule(cord1, cord2)
            decmsg = decmsg + newpair
            k += 2
        dlen = len(decmsg)
        c = 1
        while c < dlen-1:
            if decmsg[c-1] == decmsg[c+1] and decmsg[c] == 'X':
                decmsg = decmsg[:c]+decmsg[c+1:]
                dlen -= 1
            c += 1
        return decmsg

    def findCordinates(self, chr):
        cords = []
        i = (self.mytblstr.index(chr)) // 5
        j = (self.mytblstr.index(chr)) % 5
        cords.append(i)
        cords.append(j)
        return cords

    def rowRule(self, pos1, pos2):
        retpair = ''
        i1 = pos1[0]
        j1 = pos1[1]
        i2 = pos2[0]
        j2 = pos2[1]
        if j1 == 4:
            retpair = retpair + self.mytblstr[i1 * 5]
        else:
            retpair = retpair + self.mytblstr[i1 * 5 + j1 + 1]
        if j2 == 4:
            retpair = retpair + self.mytblstr[i2 * 5]
        else:
            retpair = retpair + self.mytblstr[i2 * 5 + j2 + 1]
        return retpair

    def colRule(self, pos1, pos2):
        retpair = ''
        i1 = pos1[0]
        j1 = pos1[1]
        i2 = pos2[0]
        j2 = pos2[1]
        if i1 == 4:
            retpair = retpair + self.mytblstr[j1]
        else:
            retpair = retpair + self.mytblstr[(i1 + 1) * 5 + j1]
        if i2 == 4:
            retpair = retpair + self.mytblstr[j2]
        else:
            retpair = retpair + self.mytblstr[(i2 + 1) * 5 + j2]
        return retpair

    def recRule(self, pos1, pos2):
        retpair = ''
        i1 = pos1[0]
        j1 = pos1[1]
        i2 = pos2[0]
        j2 = pos2[1]
        retpair = retpair + self.mytblstr[i1 * 5 + j2]
        retpair = retpair + self.mytblstr[i2 * 5 + j1]
        return retpair

    def rowRuleRvrs(self, pos1, pos2):
        retpair = ''
        i1 = pos1[0]
        j1 = pos1[1]
        i2 = pos2[0]
        j2 = pos2[1]
        if j1 == 0:
            retpair = retpair + self.mytblstr[i1 * 5 + 4]
        else:
            retpair = retpair + self.mytblstr[i1 * 5 + j1 - 1]
        if j2 == 0:
            retpair = retpair + self.mytblstr[i2 * 5 + 4]
        else:
            retpair = retpair + self.mytblstr[i2 * 5 + j2 - 1]
        return retpair

    def colRuleRvrs(self, pos1, pos2):
        retpair = ''
        i1 = pos1[0]
        j1 = pos1[1]
        i2 = pos2[0]
        j2 = pos2[1]
        if i1 == 0:
            retpair = retpair + self.mytblstr[(i1 + 4) * 5 + j1]
        else:
            retpair = retpair + self.mytblstr[(i1 - 1) * 5 + j1]
        if i2 == 0:
            retpair = retpair + self.mytblstr[(i2 + 4) * 5 + j2]
        else:
            retpair = retpair + self.mytblstr[(i2 - 1) * 5 + j2]
        return retpair


