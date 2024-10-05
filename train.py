from typing import List

class Solution:
   def fizzBuzz(self, n: int) -> List[str]:
      answer = []
      for i in range(1, n + 1):
         if i % 15 == 0:
            answer.append("FizzBuzz")
         elif i % 3 == 0:
            answer.append("Fizz")
         elif i % 5 == 0:
            answer.append("Buzz")
         else:
            answer.append(str(i))
         
         # print(i)

      return answer


result1 = Solution().fizzBuzz(3)
result2 = Solution().fizzBuzz(5)
result3 = Solution().fizzBuzz(15)
print("\n", result1, result2, result3, sep="\n")