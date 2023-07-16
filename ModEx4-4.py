class intSet(object):

    def __init__(self):

        self.vals = []

    def insert(self, e):

        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):

        return e in self.vals

    def remove(self, e):

        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):

        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, uncommon):

        commonvals = intSet()

        for x in self.vals:
            if uncommon.member(x):
                commonvals.insert(x)
        return commonvals

    def __len__(self):
        return len(self.vals)


s1 = intSet()
s2 = intSet()
s1.insert(1)
s1.insert(2)
s1.insert(3)
s2.insert(3)
s2.insert(4)
s2.insert(5)
s2.insert(6)
print(s1.intersect(s2))
print(len(s1))
print(len(s2))
