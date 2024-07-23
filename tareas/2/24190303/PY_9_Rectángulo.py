def coord ():
  coord = input()
  x1, y1, x2, y2, x3, y3 = map(float, coord.split())
  return (x1, y1, x2, y2, x3, y3)
  
def dist (x1, y1, x2, y2, x3, y3):
  A = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
  B = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
  C = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
  return A, B, C

def rect(A, B, C):
  return (A**2 + B**2 == C**2) or (B**2 + C**2 == A**2) or (C**2 + A**2 == B**2)

x1, y1, x2, y2, x3, y3 = coord()
A, B, C = dist(x1, y1, x2, y2, x3, y3)
if rect(A, B, C):
    print("YES")
else:
    print("NO")