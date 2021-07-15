from arcpy import *
#this help us to find the detereminant of a liste or a tuple
def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
#the determinant of an arcpy Point object
def det1(a, b):
        return a.X * b.Y- a.Y * b.X
def line_intersection(A, B, C, D):
    xdiff = (A.X - B.X), (C.X - D.X) #find the x differenes
    ydiff = (A.Y - B.Y), (C.Y - D.Y) #find the y differences
    
    div = det(xdiff, ydiff)
    if div == 0:
        return 0 #lines dont interset, they are parrallel

    d = (det1(A, B), det1(C, D)) 
    x = det(d, xdiff) / div #the x of intersection point
    y = det(d, ydiff) / div #the y of intersection point
    return x, y

A = Point(1, 1)
B = Point(3, 4)
C = Point(0, 4) 
D = Point(7, 0)

line_intersection(A, B, C, D)
#the algorithm runs only one time, so the complexity is O(1)
