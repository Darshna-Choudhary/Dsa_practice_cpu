# Input: L = {1, -1, -3},
#        points = [[-3, -2], [-1, 0], 
#             [-1, 2], [1, 2], [3, 4]]
# Output: 20.77

import math
def findOptimumCost(line, n, points):
  a, b, c = line
  def compute(x):
    if b != 0:
      y = (-c - a * x) / b
    else:
      x = -c / a
      total = 0
      for px, py in points:
        total += math.sqrt((x - px)**2 + (0 - py)**2)
      return total

    total = 0
    for px, py in points:
      total += math.sqrt((x - px)**2 + (y - py)**2)
    return total

  left, right = -1e6, 1e6
  for _ in range(100):
    mid1 = left + (right - left) / 3
    mid2 = right - (right - left) / 3
    if compute(mid1) < compute(mid2):
      right = mid2
    else:
      left = mid1

  return round(compute(left), 2)

findOptimumCost(L, 5, points)
