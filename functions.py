def collision_circle(xm,ym,xc,yc,r):
    if ((xm - xc)*(xm - xc)+((ym - yc)*(ym - 100))) <= r*r:
        return True
