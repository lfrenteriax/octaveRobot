from FreeCAD import Vector
from robot.pyooml import *
import HMatrix

v1 = Vector(30, 10, 0)
v1.x
sv1 = svector(v1)

v2 = Vector(10, 30, 0)
sv2 = svector(v2)
sv3 = svector(v1 + v2)
sv3.color("yellow")
sv2.translate(v1)

v4 = v1.cross(v2).normalize() * 10

sv4 = svector(v4).color("blue")

sv5 = svector( v2.cross(v1).normalize() * 10 )

sv6 = svector ( v4 - (v1 + v2)).color("green")

sv6.translate(v1 + v2)



frame()
v = Vector(10,10,10)
p = point(v)
sv = svector(v).color("yellow")
c = cube(v)
c.ice(80)
f2 = frame()
f2.translate(v)
f3 = frame()
f3.rotx(30)
f3.translate(v)
f3.translate(10,0,0)



a1 = -60
a2 = 70
L1 = 40
L2 = 40
 
v1 = Vector(L1, 0, 0)
v2 = Vector(L2, 0, 0)
 
f0 = frame()
f1 = frame()
f2 = frame()
 
sv1 = svector(v1).color("yellow")
sv2 = svector(v2).color("yellow")
 
Ma = HMatrix.Roty(a1)
Mb = HMatrix.Translation(v1)
Mc = HMatrix.Roty(a2)
Md = HMatrix.Translation(v2)
 
sv1.T = Ma
f1.T = Ma * Mb
 
sv2.T = Ma * Mb * Mc
f2.T = Ma * Mb * Mc * Md
 
vr = f2.T.multiply(Vector(0,0,0))
svr = svector(vr).color("orange")
 
l1 = link(l = L1, D = 10, w = 5).ice(80)
l2 = link(l = L2, D = 10, w = 3).ice(80)
 
l2.T = Ma * Mb * Mc
l1.T = Ma
 
base = sphere(r = 14, angle1 = 0).translate(0, 0, -6).ice(80)
 
 