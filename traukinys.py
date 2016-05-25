class Traukinys():

    def __init__(self, pavadinimas, t_id):
        """ Sukuria objekta - traukini. Cia:
        pavadinimas - traukinio pavadinimas,
        t_id - traukinio unikalus numeris,
        prijungti_vagonai - talpina savyje prijungtu vagonu sarasa
        uzimti_lokomotyvai - talpina savyje traukinio lokomotyva"""
        self.pavadinimas = pavadinimas
        self.t_id = t_id
        self.prijungti_vagonai = []
        self.uzimti_lokomotyvai = []

    def pridetasLokomotyvas(self, prijungtas_lokomotyvas):
        """ Priskyria traukiniui lokomotyva """
        self.prijungtas_lokomotyvas = prijungtas_lokomotyvas
        self.uzimti_lokomotyvai.append(prijungtas_lokomotyvas)

    def uzimtasLokomotyvas(self):
        """ Pateikia traukinioLokomotyvas() f-ai, koks traukinio lokomotyvas"""
        for l in self.uzimti_lokomotyvai:
            print(
                "SIO TRAUKINIO Lokomotyvo mase:",
                str(l.l_mase), ". MAX tempiamoji mase:",
                str(l.max_t_mase), ". Unikalus nr:", str(l.l_id)
            )

    def __add__(self, prijungtas_vagonas):
        """ Prideda prie traukinio vagonus """
        self.prijungti_vagonai.append(prijungtas_vagonas)

    def uzimtiVagonai(self):
        """ Pateikia traukinioVagonai() funkcijai, kokie traukinio vagonai """
        if len(self.prijungti_vagonai) == 0:
            print("Nera siame traukiny vagonu")
        else:
            for v in self.prijungti_vagonai:
                print(
                    "SIO TRAUKINIO VAGONAI: Vagonu mase:",
                    str(v.v_mase), ". Krovinio mase:",
                    str(v.k_mase), ". MAX krovinio mase:", str(v.max_k_mase),
                    ". Unikalus nr:", str(v.v_id)
                )

    def uzimtasNeleidziamasVagonai(self, ar_yra):
        """ Neleidzia pridetiVagona() funkcijai prideti jau turimo vagono """
        for v in self.prijungti_vagonai:
            if str(v.v_id) == str(ar_yra):
                return True

    def __sub__(self, atjungtas_vagonas):
        """ Pasalina traukinio vagonus """
        self.prijungti_vagonai.remove(atjungtas_vagonas)
