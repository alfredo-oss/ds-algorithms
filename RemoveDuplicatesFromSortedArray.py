
# Input: [1,1,2]
# Output: [1,2,_]

# Supuestos: - Siempre viene el arreglo ordenado
#            - El primer numero siempre sera unico si siempre esta ordenado
#            - Necesito recorrer el arreglo hacia la derecha
#            - Cuando encuentre un numero distinto del anterior numero unico, debo intercambiar sus posiciones
#            - La posicion de intercambio va a ser con la posicion que le sigue al anterior numero 
#            - Luego el puntero que apunta al numero unico, debería ser actualizado +=1

from typing import List, Tuple

class Solution:
    def RemoveDuplicatesFromSortedArray(self, arr: List[int]) -> Tuple[int, List[int]]:
         l = 1
         for r in range(1, len(arr)):
              if arr[r] != arr[r-1]:
                   arr[l] = arr[r]
                   l += 1
         return l, arr

myArray = [0,0,1,1,1,2,2,3,3,4]
print(f"Remove duplicates from sorted array: \n Original: {myArray}")
solution = Solution()
length, modifiedArray = solution.RemoveDuplicatesFromSortedArray(myArray)
print(f"\n Length: {length}\n Modified: {modifiedArray}")
