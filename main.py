from turtle import Screen, Pen
def OruntuUcgen():
    ekran = Screen()

    uzunluk = ekran.numinput("Üçgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("üçgneler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Ucgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(3):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(120)

    ekran.exitonclick()

def OruntuKare():
    ekran = Screen()

    uzunluk = ekran.numinput("Kare", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("kareler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("kareler", "İstediğiniz kare sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(4):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(90)

    ekran.exitonclick()

def OruntuBesgen():
    ekran = Screen()

    uzunluk = ekran.numinput("Besgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("besgenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Besgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(5):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(72)

    ekran.exitonclick()

def OruntuAltıgen():
    ekran = Screen()

    uzunluk = ekran.numinput("Altıgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("Altıgenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Altıgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(6):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(60)

    ekran.exitonclick()

def OruntuYedigen():
    ekran = Screen()

    uzunluk = ekran.numinput("Yedigen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("Yedigenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Yedigenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(7):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(51.42857142)

    ekran.exitonclick()

def OruntuSekizgen():
    ekran = Screen()

    uzunluk = ekran.numinput("Üçgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("üçgneler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Ucgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(8):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(45)

    ekran.exitonclick()

def OruntuDokuzgen():
    ekran = Screen()

    uzunluk = ekran.numinput("Dokuzgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("Dokuzgenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Dokuzgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(9):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(40)

    ekran.exitonclick()

def OruntuOngen():
    ekran = Screen()

    uzunluk = ekran.numinput("Ongen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("Ongenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Ongenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(10):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(36)

    ekran.exitonclick()

def OruntuOnbirgen():
    ekran = Screen()

    uzunluk = ekran.numinput("Onbirgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("Onbirgenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Onbirgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(11):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(32.72727272)

    ekran.exitonclick()

def OruntuOnikigen():
    ekran = Screen()

    uzunluk = ekran.numinput("Onikigen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("Onikigenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Onikigenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(12):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(30)

    ekran.exitonclick()
from turtle import Screen, Pen
def OruntuUcgen():
    ekran = Screen()

    uzunluk = ekran.numinput("Üçgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("üçgneler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Ucgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(3):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(120)

    ekran.exitonclick()

def OruntuKare():
    ekran = Screen()

    uzunluk = ekran.numinput("Kare", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("kareler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("kareler", "İstediğiniz kare sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(4):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(90)

    ekran.exitonclick()

def OruntuBesgen():
    ekran = Screen()

    uzunluk = ekran.numinput("Besgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("besgenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Besgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(5):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(72)

    ekran.exitonclick()

def OruntuAltıgen():
    ekran = Screen()

    uzunluk = ekran.numinput("Altıgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("Altıgenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Altıgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(6):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(60)

    ekran.exitonclick()

def OruntuYedigen():
    ekran = Screen()

    uzunluk = ekran.numinput("Yedigen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("Yedigenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Yedigenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(7):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(51.42857142)

    ekran.exitonclick()

def OruntuSekizgen():
    ekran = Screen()

    uzunluk = ekran.numinput("Üçgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("üçgneler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Ucgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(8):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(45)

    ekran.exitonclick()

def OruntuDokuzgen():
    ekran = Screen()

    uzunluk = ekran.numinput("Dokuzgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("Dokuzgenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Dokuzgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(9):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(40)

    ekran.exitonclick()

def OruntuOngen():
    ekran = Screen()

    uzunluk = ekran.numinput("Ongen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("Ongenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Ongenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(10):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(36)

    ekran.exitonclick()

def OruntuOnbirgen():
    ekran = Screen()

    uzunluk = ekran.numinput("Onbirgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("Onbirgenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Onbirgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(11):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(32.72727272)

    ekran.exitonclick()


def OruntuParalelKenar():
    ekran = Screen()

    uzunluk = ekran.numinput("ParalelKenar", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("ParalelKenar", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("ParalelKenar", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(2):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(150)
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(30)

    ekran.exitonclick()


def ParalelKenar():
    ekran = Screen()
    uzunluk = ekran.numinput("ParalelKenar", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    pen = Pen()

    for sekil in range(2):

            pen.forward(uzunluk + sekil )
            pen.left(150)
            pen.forward(uzunluk + sekil )
            pen.left(30)

    ekran.exitonclick()



def OruntuYamuk():
    ekran = Screen()

    uzunluk = ekran.numinput("Yamuk", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)

    arttırmak = ekran.numinput("Yamuk", "Boyut artışını girin:", default=30, minval=10, maxval=50)

    # numinput() returns a float but we need an int for range()
    Sekiller = int(ekran.numinput("Yamuk", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))

    pen = Pen()

    for sekil in range(Sekiller):
        for _ in range(1):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(120)
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(60)
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(60)
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(120)
            pen.forward(uzunluk + sekil * arttırmak)


    ekran.exitonclick()


def Yamuk():
    ekran = Screen()

    uzunluk = ekran.numinput("Yamuk", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)


    pen = Pen()

    for sekil in range(1):

            pen.forward(uzunluk )
            pen.left(120)
            pen.forward(uzunluk )
            pen.left(60)
            pen.forward(uzunluk)
            pen.left(60)
            pen.forward(uzunluk)
            pen.left(120)
            pen.forward(uzunluk )


    ekran.exitonclick()

OruntuYamuk()









