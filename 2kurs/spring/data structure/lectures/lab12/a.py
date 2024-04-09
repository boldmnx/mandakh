'''
min
max
findgt
findlt

why heregtei 
1. Үр дүнтэй хайлт

sortolson engiines ylgaatai
3. Мэдээллийг сортолсноороо тухайн мэдээллтэй ажилхад илүү хялбар болно.


zip is 2array niiluuldeg
index
'''


class SortedMap:
    def __init__(self):
        self.sortedMap = []

    def setitem(self, e):
        self.sortedMap.append(e)

    def getitem(self):
        print(self.sortedMap)

    def delitem(self, e):
        del self.sortedMap[e]

    def sortedRecord(self):

        return sorted(i['grade'] for i in self.SortedMap)

    def minitem(self):
        m = self.sortedMap[0]
        for i in self.sortedMap:
            if i['grade'] < m['grade']:
                m = i
        return m

    def maxitem(self):
        m = self.sortedMap[0]
        for i in self.sortedMap:
            if i['grade'] > m['grade']:
                m = i
        return m

    def findgt(self):
        pass

    def findlt(self):
        pass


sMap = SortedMap()
sMap.setitem({
    'name': 'Bold',
    'grade': 90
})
sMap.setitem({
    'name': 'Anugo',
    'grade': 80
})
sMap.setitem({
    'name': 'Davka',
    'grade': 100
})
sMap.setitem({
    'name': 'Telmen',
    'grade': 101
})
# sMap.getitem()
# print(f'min grade: {sMap.minitem()}')
# print(f'max grade: {sMap.maxitem()}')
print(sMap.sortedRecord())
