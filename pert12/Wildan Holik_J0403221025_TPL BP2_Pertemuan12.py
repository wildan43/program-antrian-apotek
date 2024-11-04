print ("==============")
print (" WILDAN HOLIK ")
print (" J0403221025  ")
print ("==============")

print("================================================")

class Graf:
    def _init_(self):
        self.verteks = ["A", "B", "C", "D", "E", "F"]
        self.edge = {
            "A": {"E": 0.1, "F": 0.9},
            "B": {"A": 0.3, "C": 0.3, "D": 0.4},
            "C": {"D": 0.6, "E": 0.4},
            "D": {"E": 1},
            "E": {"A": 0.55, "F": 0.45},
            "F": {"D": 1}
        }

    def cetak_vertek(self):
        print("Verteks:")
        for vertek in self.verteks:
            print(vertek)

    def cetak_edge(self):
        print("Edge:")
        for u, edges in self.edge.items():
            for v, bobot in edges.items():
                print(f"{u} -({bobot})-> {v}")
                
#Membuat objek Graf
graf = Graf()
#Mencetak verteks
graf.cetak_vertek()
#Mencetak edge
graf.cetak_edge()