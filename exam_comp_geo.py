from arcpy import * 
#function to calculate crossproduct(produit vectoriel)
def produitVetoriel(A):
    X1, Y1, X2, Y2 = (A[1].X - A[0].X), (A[1].Y - A[0].Y), (A[2].X - A[0].X), (A[2].Y- A[0].Y)#stores Xs and Ys of each point 
    return (X1 * Y2 - Y1 * X2)

#fct that checks whether a polyon is convex or not with the help of produitVectoriel funtion 
def isPoly_Convex(pts):
    n = len(pts)
    prev = 0 #diretion of previus traversed edges
    current = 0 #diretion of current traversed edges
    for i in range(n): #looping through the elements of pts
        temp = [points[i], points[(i + 1) % n],points[(i + 2) % n]]

        current = produitVetoriel(temp) #updating current
        if (current != 0):
            if (current * prev < 0): #if direction of produit vectoriel of all edges is not the same
                return False
            else:
                prev = current #updating prev
    return True
 
points = [ Point(1, 1) ,  Point(3, 4),
          Point(0, 4) , Point(7, 0)]

if isPoly_Convex(points):
    print 1 #yes, it's a polyon
else:
    print 0 #it's not a polygon
#the algo runs n times(loop), so the omplexity of this algorithm is O(n) where is the number of points
