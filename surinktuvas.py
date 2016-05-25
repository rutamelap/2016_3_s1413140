from lokomotyvas import Lokomotyvas
from vagonas import Vagonas
from traukinys import Traukinys
import argparse
import sys
import random


def meniuSarasas():
    """ Pateikia meniu skydeli konsoleje """
    print ("""
    1. Vagonų sąrašas
    2. Lokomotyvų sąrašas
    3. Traukinių sąrašas
    4. Sukurti lokomotyvą
    5. Sukurti vagona
    6. Sukurti traukini
    7. Pakeisti traukinio lokomotyva
    8. Prideti prie traukinio vagona
    9. Pasalinti traukinio vagona
    10. Traukinio vagonai
    11. Traukinio lokomotyvas
    12. Isrusiuoti traukinius
    13. Istrinti traukini
    14. Istrinti lokomotyva
    15. Istrinti vagona
    ENTER - iseiti is programos
    """)

parser = argparse.ArgumentParser()
parser.add_argument("-j", dest="json",
                    help="Duomenys įkelti iš json", action="store_true")
parser.add_argument("-k", dest="konsole",
                    help="Duomenys pateikti iš konsolės", action="store_true")
args = parser.parse_args()

lokomotyvai = []
vagonai = []
traukiniai = []

if args.json is False and args.konsole is False:
    parser.parse_args(["-h"])

if args.json is True:
    pass


def vagonuSarasas():
    """ Spausdina egzistuojanciu vagonu sarasa """
    if len(vagonai) == 0:
        print("Vagonu nera")
    else:
        for v in vagonai:
            print(
                "Vagonu mase:", str(v.v_mase), ". Krovinio mase:",
                str(v.k_mase), ". MAX krovinio mase:",
                str(v.max_k_mase), ". Unikalus nr:", str(v.v_id)
            )


def lokomotyvuSarasas():
    """ Spausdina egzistuojanciu lokomotyvu sarasa """
    if len(lokomotyvai) == 0:
        print("Lokomotyvu nera")
    else:
        for l in lokomotyvai:
            print(
                "Lokomotyvo mase:", str(l.l_mase),
                ". MAX tempiamoji mase:", str(l.max_t_mase),
                ". Unikalus nr:", str(l.l_id)
            )


def traukiniuSarasas():
    """ Spausdina egzistuojanciu traukiniu sarasa """
    if len(traukiniai) == 0:
        print("Traukiniu nera")
    else:
        for t in traukiniai:
            print(
                "Traukinio pavadinimas:", str(t.pavadinimas),
                ". Id:", str(t.t_id)
            )


def kurtiLokomotyva():
    """ Sukuria lokomotyva """
    print("Iveskite naujo lokomotyvo mase(priimami tik skaičiai): ")
    try:
        l_mase = int(input())
    except ValueError:
        print('\033[1m')
        print('\nNaujas lokomotyvas nesukurtas. Ivedete ne skaiciu')
        print('\033[0m')
        meniuSarasas()
        return
    print("Iveskite naujo lokomotyvo maksimalia tempiama mase: ")
    try:
        max_t_mase = int(input())
    except ValueError:
        print('\033[1m')
        print('\nNaujas lokomotyvas nesukurtas. Ivedete ne skaiciu')
        print('\033[0m')
        meniuSarasas()
        return
    unikalusNr = random.randint(0, 9999)
    l = Lokomotyvas(l_mase, max_t_mase, unikalusNr)
    lokomotyvai.append(l)
    print("Lokomotyvas sukurtas")
    meniuSarasas()


def kurtiVagona():
    """ Sukuria vagona """
    try:
        v_mase = int(input("Iveskite naujo vagono mase(priimami tik sk): "))
    except ValueError:
        print('\033[1m')
        print('\nNaujas vagonas nesukurtas. Ivedete ne skaiciu')
        print('\033[0m')
        meniuSarasas()
        return
    try:
        k_mase = int(input("Iveskite naujo vagono krovinio mase: "))
    except ValueError:
        print('\033[1m')
        print('\nNaujas vagonas nesukurtas. Ivedete ne skaiciu')
        print('\033[0m')
        meniuSarasas()
        return
    try:
        max_k_mase = int(input("Iveskite naujo vagono krovinio max mase: "))
    except ValueError:
        print('\033[1m')
        print('\nNaujas vagonas nesukurtas. Ivedete ne skaiciu')
        print('\033[0m')
        meniuSarasas()
        return
    while k_mase > max_k_mase:
        try:
            max_k_mase = int(input("""
                                    Krovinis sunkesnis nei nurodyta jo max mase
                                    Iveskite nauja max krovinio mase:"""))
        except ValueError:
            print('\033[1m')
            print('\nNaujas vagonas nesukurtas. Ivedete ne skaiciu')
            print('\033[0m')
            meniuSarasas()
            return
    unikalusNr = random.randint(0, 9999)
    v = Vagonas(v_mase, k_mase, max_k_mase, unikalusNr)
    vagonai.append(v)
    print("Vagonas sukurtas")
    meniuSarasas()


def kurtiTraukini():
    """ Sukuria traukini ir priskyria jam egzistuojanti lokomotyva """
    if len(lokomotyvai) == 0:
        print('\033[1m')
        print('\nDeja, bet nera jokiu lokomotyvu, o jis butinas traukiniui')
        print('\033[0m')
        meniuSarasas()
        return
    pavadinimas = input("Iveskite naujo traukinio pavadinima: ")
    unikalusNr = random.randint(0, 9999)
    t = Traukinys(pavadinimas, unikalusNr)
    traukiniai.append(t)
    print("Traukinys sekmingai sukurtas!!! Dabar pridekite lokomotyva")
    lokomotyvuSarasas()
    try:
        lId = int(input("Iveskite lokomotyvo unikalu nr is pateikto saraso"
                        "(tik skaiciu): "))
    except ValueError:
        print('\033[1m')
        print('\nIsitikinkite, jog vedate skaicius')
        print('\033[0m')
        meniuSarasas()
        return
    for l in lokomotyvai:
        if str(l.l_id) == str(lId):
            ikelsim = l
    for t in traukiniai:
        if str(t.t_id) == str(unikalusNr):
            t.pridetasLokomotyvas(ikelsim)
    print('Lokomotyvas sekmingai pridetas. Traukinys uzbaigtas')
    meniuSarasas()


def pridetiLokomotyva():
    """ Prideda prie egzistuojancio traukinio lokomotyva """
    if len(lokomotyvai) == 0:
        print('\033[1m')
        print('\nDeja, bet nera jokiu lokomotyvu')
        print('\033[0m')
        meniuSarasas()
        return
    if len(traukiniai) == 0:
        print('\033[1m')
        print('\nDeja, bet nera jokiu traukiniu')
        print('\033[0m')
        meniuSarasas()
        return
    lokomotyvuSarasas()
    try:
        lId = int(input("Iveskite lokomotyvo unikalu nr is pateikto saraso"
                        "(tik skaiciu): "))
    except ValueError:
        print('\033[1m')
        print('\nIsitikinkite, jog vedate skaicius')
        print('\033[0m')
        meniuSarasas()
        return
    for l in lokomotyvai:
        if str(l.l_id) == str(lId):
            ikelsim = l
    traukiniuSarasas()
    try:
        tId = int(input("Iveskite traukinio unikalu nr is pateikto saraso"
                        "(tik skaiciu): "))
    except ValueError:
        print('\033[1m')
        print('\nIsitikinkite, jog vedate skaicius')
        print('\033[0m')
        meniuSarasas()
        return
    for t in traukiniai:
        if str(t.t_id) == str(tId):
            t.pridetasLokomotyvas(ikelsim)
    print('Lokomotyvas sekmingai pridetas')
    meniuSarasas()


def traukinioVagonai():
    """ Pateikia isrinkto traukinio jam priskirtus vagonus """
    if len(traukiniai) == 0:
        print('\033[1m')
        print('\nDeja, bet nera jokiu traukiniu')
        print('\033[0m')
        meniuSarasas()
        return
    traukiniuSarasas()
    try:
        tId = int(input("Iveskite traukinio unikalu nr is pateikto saraso"
                        "(tik skaiciu): "))
    except ValueError:
        print('\033[1m')
        print('\nIsitikinkite, jog vedate skaicius')
        print('\033[0m')
        meniuSarasas()
        return
    for t in traukiniai:
        if str(t.t_id) == str(tId):
            t.uzimtiVagonai()
    meniuSarasas()


def pridetiVagona():
    """ Prideda prie egzistuojancio traukinio vagona """
    if len(vagonai) == 0:
        print('\033[1m')
        print('\nDeja, bet nera jokiu vagonu')
        print('\033[0m')
        meniuSarasas()
        return
    if len(traukiniai) == 0:
        print('\033[1m')
        print('\nDeja, bet nera jokiu traukiniu')
        print('\033[0m')
        meniuSarasas()
        return
    traukiniuSarasas()
    try:
        tId = int(input("Iveskite traukinio unikalu nr is pateikto saraso"
                        "(tik skaiciu): "))
    except ValueError:
        print('\033[1m')
        print('\nIsitikinkite, jog vedate skaicius')
        print('\033[0m')
        meniuSarasas()
        return
    vagonuSarasas()
    try:
        vId = int(input("Iveskite vagono unikalu nr is pateikto saraso"
                        "(tik skaiciu): "))
    except ValueError:
        print('\033[1m')
        print('\nIsitikinkite, jog vedate skaicius')
        print('\033[0m')
        meniuSarasas()
        return
    for t in traukiniai:
        rezas = t.uzimtasNeleidziamasVagonai(vId)
        if rezas is True:
            print('\033[1m')
            print("\nSis vagonas JAU pridetas. Bandykit is naujo su kt vagonu")
            print('\033[0m')
            meniuSarasas()
            return
        else:
            pass
    for v in vagonai:
        if str(v.v_id) == str(vId):
            ikelsim = v
    for t in traukiniai:
        if str(t.t_id) == str(tId):
            t.__add__(ikelsim)
    print('Vagonas sekmingai pridetas')
    meniuSarasas()


def atjungtiVagona():
    """ Atjungia nuo egzistuojancio traukinio jam priskirta vagona """
    if len(traukiniai) == 0:
        print('\033[1m')
        print('\nDeja, bet nera jokiu traukiniu')
        print('\033[0m')
        meniuSarasas()
        return
    traukiniuSarasas()
    try:
        tId = int(input("Iveskite traukinio unikalu nr is pateikto saraso"
                        "(tik skaiciu): "))
    except ValueError:
        print('\033[1m')
        print('\nIsitikinkite, jog vedate skaicius')
        print('\033[0m')
        meniuSarasas()
        return
    for t in traukiniai:
        if str(t.t_id) == str(tId):
            t.uzimtiVagonai()
    try:
        vId = int(input("Iveskite vagono ID is pateikto traukiniu saraso: "))
    except ValueError:
        print('\033[1m')
        print('\nIsitikinkite, jog vedate skaicius')
        print('\033[0m')
        meniuSarasas()
        return
    for v in vagonai:
        if str(v.v_id) == str(vId):
            ikelsim = v
    for t in traukiniai:
        if str(t.t_id) == str(tId):
            t.__sub__(ikelsim)
    print('Vagonas sekmingai atjungtas')
    meniuSarasas()


def traukinioLokomotyvas():
    """ Pateikia pasirinkto traukinio jam priskirta lokomotyva """
    if len(traukiniai) == 0:
        print('\033[1m')
        print('\nDeja, bet nera jokiu traukiniu')
        print('\033[0m')
        meniuSarasas()
        return
    traukiniuSarasas()
    try:
        tId = int(input("Iveskite traukinio unikalu nr is pateikto saraso"
                        "(tik skaiciu): "))
    except ValueError:
        print('\033[1m')
        print('\nIsitikinkite, jog vedate skaicius')
        print('\033[0m')
        meniuSarasas()
        return
    for t in traukiniai:
        if str(t.t_id) == str(tId):
            t.uzimtasLokomotyvas()
    meniuSarasas()


def istrintiTraukini():
    """ Istrina parinkta traukini """
    if len(traukiniai) == 0:
        print('\033[1m')
        print('\nDeja, bet nera ka trinti, nes nera traukiniu')
        print('\033[0m')
        meniuSarasas()
        return
    traukiniuSarasas()
    try:
        tId = int(input("Iveskite traukinio unikalu nr is pateikto saraso"
                        "(tik skaiciu): "))
    except ValueError:
        print('\033[1m')
        print('\nIsitikinkite, jog vedate skaicius')
        print('\033[0m')
        meniuSarasas()
        return
    for t in traukiniai:
        if str(t.t_id) == str(tId):
            traukiniai.remove(t)
    print("Traukinys sekmingai istrintas")
    meniuSarasas()


def istrintiLokomotyva():
    """ Istrina parinkta lokomotyva """
    if len(lokomotyvai) == 0:
        print('\033[1m')
        print('\nDeja, bet nera ka trinti, nes nera lokomotyvu')
        print('\033[0m')
        meniuSarasas()
        return
    lokomotyvuSarasas()
    try:
        lId = int(input("Iveskite lokomotyvo unikalu nr is pateikto saraso"
                        "(tik skaiciu): "))
    except ValueError:
        print('\033[1m')
        print('\nIsitikinkite, jog vedate skaicius')
        print('\033[0m')
        meniuSarasas()
        return
    for l in lokomotyvai:
        if str(l.l_id) == str(lId):
            lokomotyvai.remove(l)
    print("Lokomotyvas sekmingai istrintas")
    meniuSarasas()


def istrintiVagona():
    """ Istrina parinkta vagona """
    if len(vagonai) == 0:
        print('\033[1m')
        print('\nDeja, bet nera ka trinti, nes nera vagonu')
        print('\033[0m')
        meniuSarasas()
        return
    vagonuSarasas()
    try:
        vId = int(input("Iveskite vagono unikalu nr is pateikto saraso"
                        "(tik skaiciu): "))
    except ValueError:
        print('\033[1m')
        print('\nIsitikinkite, jog vedate skaicius')
        print('\033[0m')
        meniuSarasas()
        return
    for v in vagonai:
        if str(v.v_id) == str(vId):
            vagonai.remove(v)
    print("Vagonas sekmingai istrintas")
    meniuSarasas()


def rusiuotiTraukinius():
    """ Surusiuoja traukinius pagal pasirenkta tvarka """
    if len(traukiniai) == 0:
        print('\033[1m')
        print('\nDeja, bet nera jokiu traukiniu')
        print('\033[0m')
        meniuSarasas()
        return

    def meniuS():
        """ Pateikia traukiniu rusiavimo meniu """
        print ("""
        1. Pagal traukiniu pavadinimus abc tvarka
        2. Pagal traukiniu pavadinimus cba tvarka
        ENTER - iseiti is traukiniu rusiavimo
        """)

    def pagalABC():
        """ Rusiuoja egzistuojancius traukinius abeceles tvarka """
        traukiniuSarasas()
        bus_abc = []
        for t in traukiniai:
            bus_abc.append(str(t.pavadinimas))
        print("Isrusiuotas traukiniu sarasas:", sorted(bus_abc))

    def pagalCBA():
        """ Rusiuoja egzistuojancius traukinius priesinga abeceles tvarka """
        traukiniuSarasas()
        bus_abc = []
        for t in traukiniai:
            bus_abc.append(str(t.pavadinimas))
        print("Isrusiuotas traukiniu sarasas:", sorted(bus_abc, reverse=True))

    meniuS()
    meniuu = True
    while meniuu:
        meniuu = input("Kaip noresite, kad traukiniai butu isrusiuoti:  ")
        if meniuu == "1":
            print("\nNeisrusiuotu traukiniu sarasas:\n")
            pagalABC()
        elif meniuu == "2":
            print("\nNeisrusiuotu traukiniu sarasas:\n")
            pagalCBA()
        elif meniuu != "":
            print('\033[1m')
            print('\nTokio numerio nėra. Bandykite tik iš pateiktų pasiūlymų')
            print('\033[0m')
            meniuS()

meniuSarasas()
meniu = True
while meniu:
    print("Jei nematote meniu, rasykite m")
    meniu = input("Pasirinkite veiksmo numerį:  ")
    if meniu == "1":
        print("\nVagonų sąrašas:\n")
        vagonuSarasas()
        meniuSarasas()
    elif meniu == "2":
        print("\nLokomotyvų sąrašas:\n")
        lokomotyvuSarasas()
        meniuSarasas()
    elif meniu == "3":
        print("\nTraukinių sąrašas:\n")
        traukiniuSarasas()
        meniuSarasas()
    elif meniu == "4":
        kurtiLokomotyva()
    elif meniu == "5":
        kurtiVagona()
    elif meniu == "6":
        kurtiTraukini()
    elif meniu == "7":
        pridetiLokomotyva()
    elif meniu == "8":
        pridetiVagona()
    elif meniu == "9":
        atjungtiVagona()
    elif meniu == "10":
        traukinioVagonai()
    elif meniu == "11":
        traukinioLokomotyvas()
    elif meniu == "12":
        rusiuotiTraukinius()
    elif meniu == "13":
        istrintiTraukini()
    elif meniu == "14":
        istrintiLokomotyva()
    elif meniu == "15":
        istrintiVagona()
    elif meniu == "m":
        meniuSarasas()
    elif meniu == "0":
        sys.exit()
    elif meniu != "":
        print('\033[1m')
        print('\nTokio numerio nėra. Bandykite tik iš pateiktų pasiūlymų')
        print('\033[0m')
        meniuSarasas()
