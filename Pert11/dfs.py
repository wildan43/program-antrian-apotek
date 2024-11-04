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

checkpoint = set()

def dfs(checkpoint,graph,start):
    if start not in checkpoint:
        print(start)
        checkpoint.add(start)
        for neighbour in graph[start]:
            dfs(checkpoint, graph, neighbour)

dfs(checkpoint, graph, '0')
