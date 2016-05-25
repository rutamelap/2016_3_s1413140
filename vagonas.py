class Vagonas():

    def __init__(self, v_mase, k_mase, max_k_mase, v_id):
        """ Sukuria objekta - vagona. Cia:
        v_mase - vagono mase,
        k_mase - krovinio mase,
        max_k_mase - maksimali krovinio mase,
        v_id - vagono unikalus numeris"""
        self.v_mase = v_mase
        self.k_mase = k_mase
        self.max_k_mase = max_k_mase
        self.v_id = v_id

    @property
    def getv_id(self):
        return self.getv_id
