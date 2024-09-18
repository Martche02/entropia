from sympy import symbols, Plane, Point3D, solve, Line

# Suponha que você tenha três pontos
p1 = Point3D(1, 0, 0)
p2 = Point3D(0, 1, 0)
p3 = Point3D(0, 0, 1)

# Crie os planos equidistantes à origem
plane1 = Plane(p1/2, normal_vector=p1)
plane2 = Plane(p2/2, normal_vector=p2)
plane3 = Plane(p3/2, normal_vector=p3)

# Encontre a linha de intersecção dos dois primeiros planos
line = plane1.intersection(plane2)[0]

# Agora verifique se essa linha intersecta o terceiro plano
intersection = plane3.intersection(line)

if intersection:
    print("A linha intersecta o plano")
else:
    print("A linha se estende até o infinito")
