class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def hitung_luas(self):
        return self.panjang * self.lebar
    
    def __str__(self):
        return "Persegi : " + str(self.panjang) + "Lebar: " + str(self.lebar) + "keliling: " + str(self.hitung_keliling()) + "Luas: " + str(self.hitung_luas())