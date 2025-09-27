class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr_coord = [0, 0]
        visited = set()
        visited.add(tuple(curr_coord))

        for d in path:
            if d == 'N':
                curr_coord[1] += 1
            elif d == 'S':
                curr_coord[1] -= 1
            elif d == 'E':
                curr_coord[0] += 1
            else:
                curr_coord[0] -= 1
            
            curr_coord_tuple = tuple(curr_coord) 
            if (curr_coord_tuple) in visited:
                return True
        
            visited.add(curr_coord_tuple)

        return False