from linkedList import Node, LinkedList


class PlayList(LinkedList):
    pass


play = PlayList()
print('originial play list:')
play.ad('цагаан баавгай')
play.add_begin('хамгийн сайхан нь')
play.add_begin('хурим')
play.add_begin('гүнж')
play.read()
