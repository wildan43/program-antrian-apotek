#Wildan Holik
#J0403221025

graph = {
   '0' : set (['3','1']),
   '1' : set (['0','5','2','3']),
   '2' : set (['3','1','5','4']),
   '3' : set (['0','2','4','1']),
   '4' : set (['3','2','6']),
   '5' : set (['2','1']),
   '6' : set (['4','1'])
    }

def bfs_lintasan_terpendek(graph, mulai,tujuan):
    explored=[]
    queue=[[mulai]]

    if mulai == tujuan :
        return "Awal adalah tujuan"
    while queue :
        jalur = queue.pop(0)
        node = jalur[-1]

        if node not in explored :
            neighbour = graph[node]

            for neighbour in neighbour :
                jalur_baru = list(jalur)
                jalur_baru.append(neighbour)
                queue.append(jalur_baru)

                if neighbour == tujuan :
                    return jalur_baru
            
            explored.append(node)
    return "Mohon maaf node yang dicari tidak ada"

mulai = input("masukan awal : ")
tujuan = input("masukan akhir : ")
print(bfs_lintasan_terpendek(graph, mulai,tujuan))