from random import *
from numpy import *

def milieu_triangle0 (Triangle(p1,p2,p3)) :
    C=Point(0,0,0) #somme des sommets du triangle
    C=Point((xp1+xp2+xp3)/3,(yp1+yp2+yp3)/3,(zp1+zp2+zp3)/3)#C devient le centre du triangle
    return (C)

def milieu_triangle (T) :
    C=Point(0,0,0) #somme des sommets du triangle
    C=Point((T.point1.xP+T.point2.xP+T.point3.xP)/3,(T.point1.yP+T.point2.yP+T.point3.yP)/3,(T.point1.zP+T.point2.zP+T.point3.zP)/3)#C devient le centre du triangle
    return(C)

def Normale0(Triangle(p1,p2,p3), distance):
    u=array([xp1-px2),(yp1-yp2),(zp1-zp2)])#On calcule les deux vecteurs
    v=array([xp1-px3),(yp1-yp3),(zp1-zp3)])
    #Voilà fifi le produit vectoriel
    w=array([(yp1-yp2)*(zp1-zp3)-(zp1-zp3)*(yp1-yp3),(zp1-zp2)*(xp1-xp3)-(xp1-xp3)*(zp1-zp3),(xp1-xp2)*(yp1-yp3)-(yp1-yp3)*(xp1-xp3)])
    p4=milieu_triangle(Triangle(p1,p2,p3)+ w*distance#point sur la normale
    return(p4)
    
def Normale(T, distance):
    M=milieu_triangle(T)
    u=array([(T.point1.xP-T.point2.xP),(T.point1.yP-T.point2.yP),(T.point1.zP-T.point2.zP)])#On calcule les deux vecteurs
    v=array([(T.point1.xP-T.point3.xP),(T.point1.yP-T.point3.yP),(T.point1.zP-T.point3.zP)])
    #Voilà fifi le produit vectoriel
    w=array([(u[1])*(v[2])-(u[2])*(v[1]),(u[2])*(v[0])-(u[0])*(v[2]),(u[0])*(v[1])-(u[1])*(v[0])])
    p4=Point(M.xP + w[0]*distance, M.yP + w[1]*distance, M.zP + w[2]*distance)#point sur la normale
    return(p4)

def creation_triangle(T,distance):
    T1=Triangle(A=T.point1,B=T.point2,C=Normale(T,distance))
    T2=Triangle(A=T.point1,B=T.point3,C=Normale(T,distance))
    T3=Triangle(A=T.point2,B=T.point3,C=Normale(T,distance))
    return(T1,T2,T3) #retourner les triangles d'une façon spéciale ?

triangle_0=Triangle(Point(0,0,0),Point(1,0,0),Point(0,1,0))
liste=[triangle_0]
for i in range(nb_etapes):
    for j in range(len(liste)):
            distance = abs(gauss(4**(-i),0.1**(i+1)))#Donne un nombre aléatoire selon une répartition gaussienne. A voir pour les paramètres ( le premier est la valeur moyenne, le second l’écart type)
            liste=liste+[liste.pop(0).creation_triangle(distance)]#Enlève un triangle à la liste pour ajouter les trois triangles qui en sont issus

for i in range(len(liste)):#On transforme chaque élément de la liste, pour que le module d'affichage 3d puisse en faire qqchose
    triangle=liste[i]
    liste[i]=[(triangle.point1.xP,triangle.point1.yP,triangle.point1.zP),(triangle.point2.xP,triangle.point2.yP,triangle.point2.zP),(triangle.point3.xP,triangle.point3.yP,triangle.point3.zP)]
