from math import sin, cos, hypot

R = 6378137
F, G, T = map(int, input().split())

posF = (T*F, 0)

theta = T*G/R
posG = (R*sin(theta), R-R*cos(theta))

print(hypot(posF[0]-posG[0], posF[1]-posG[1]))