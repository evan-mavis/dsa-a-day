class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source_cities = set()
       
        for i in range(len(paths)):
            source_cities.add(paths[i][0])
           
        for j in range(len(paths)):
            if paths[j][1] not in source_cities:
                return paths[j][1]
        