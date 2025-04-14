"""""
Actividad:
Dada una matriz de números enteros y un número entero , devuelve índices de los dos números tales que se suman al objetivo.numstarget

Puede suponer que cada entrada tendría exactamente una solución, y no puede usar el mismo elemento dos veces.

Puede devolver la respuesta en cualquier orden. 

Ejemplo 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Ejemplo 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Ejemplo 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Restricciones:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Solo existe una respuesta válida.

Seguimiento: ¿Se puede llegar a un algoritmo que sea menos complejo que el tiempo? O(n2)
"""""
class Solution:
    def twoSum(self, nums, target):

        num_map = {}  # Diccionario para almacenar los números y sus índices
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []  # No se alcanzará debido a las restricciones del problema