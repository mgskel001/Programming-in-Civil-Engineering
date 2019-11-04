#Open Channel Shear Centre Program by Keletso Mogashoa

#Input dimensions
print ("Please note for this program, left is x+ and up is y+")
la = float(input("Top Flange Length="))
lb = float(input("Web Length="))
lc = float(input("Bottom Flange Length="))
ta = float(input("Top Flange Thickness="))
tb = float(input("Web Thickness="))
tc = float(input("Bottom Flange Thickness="))

#Array of initial co-ordinates
X = [la, tb/2, tb/2, lc]
Y = [ta/2, ta/2, lb - tc/2, lb - tc/2]

#Centroid calc
xc = (la*ta*la/2 + (lb-ta-tc)*tb*tb/2 + lc*tc*lc/2)/(la*ta + (lb-ta-tc)*tb + lc*tc)
yc = (la*ta*ta/2 + (lb-ta-tc)*tb*lb/2 + lc*tc*(lb-tc/2))/(la*ta + (lb-ta-tc)*tb + lc*tc)
print ("Centroid Coordinates: ",-xc, -yc)
for i in range (4):
    X[i] = X[i] - xc
    Y[i] = Y[i] - yc
    
#print (X, Y)


# In[2]:
L=[la-tb/2, lb-ta/2-tc/2, lc-tb/2]

w_ij = [L[0]*abs(Y[0]), L[1]*abs(X[1]), L[2]*abs(Y[2])]
#print(w_ij)


# In[3]:


w = [0]
sumw = 0
for i in range (1,4):
    sumw = sumw + w_ij[i-1]
    w.append(sumw)
#print (w)


# In[4]:


wi_xi, wj_xj, wi_xj, wj_xi = [],[],[],[]
wi_yi, wj_yj, wi_yj, wj_yi = [],[],[],[]

for i in range (3):
    xi = X[i]
    xj = X[i+1]
    yi = Y[i]
    yj = Y[i+1]
    wi = w[i]
    wj = w[i+1]
    
    wi_xi.append(wi*xi)
    wj_xj.append(wj*xj)
    wi_xj.append(wi*xj)
    wj_xi.append(wj*xi)
    wi_yi.append(wi*yi)
    wj_yj.append(wj*yj)
    wi_yj.append(wi*yj)
    wj_yi.append(wj*yi)
    
#print(wi_xi, wj_xj, wi_xj, wj_xi)    
#print(wi_yi, wj_yj, wi_yj, wj_yi)


# In[6]:



t=[ta, tb, tc]
col5, col6, col11, col12 = [],[],[],[]
for i in range (3):
    col5.append((wi_xi[i]+wj_xj[i])*L[i]*t[i])
    col6.append((wi_xj[i] + wj_xi[i])*t[i]*L[i])
    col11.append((wi_yi[i] + wj_yj[i])*t[i]*L[i]) 
    col12.append((wi_yj[i] + wj_yi[i])*t[i]*L[i])
    
#print(sum5, sum6, sum11, sum12)


# In[7]:


Iwx = (1/3)*sum(col5) + (1/6)*sum(col6)
Iwy = (1/3)*sum(col11) + (1/6)*sum(col12)

#print(Iwx, Iwy)


# In[ ]:
Ixa = ((ta**3)*la)/12 + (ta*la)*(abs(yc - ta/2))**2
Ixb = (((lb-ta-tc)**3)*tb)/12 + (tb*(lb-ta-tc))*(abs(yc - (lb)/2))**2
Ixc = ((tc**3)*lc)/12 + (tc*lc)*(abs(lb - yc - tc/2))**2

Ix = Ixa + Ixb + Ixc

Iya = ((la**3)*ta)/12 + (ta*la)*(abs(la/2 - xc))**2
Iyb = ((tb**3)*(lb-ta-tc))/12 + (tb*(lb-ta-tc))*(abs(xc - tb/2))**2
Iyc = ((lc**3)*tc)/12 + (tc*lc)*(abs(lc/2 - xc))**2

Iy = Iya + Iyb + Iyc


Ixya = (ta/2 - yc)*(la/2 - xc)*(ta*la)
Ixyb = (-yc + ta + (lb-ta-tc)/2)*(tb/2 - xc)*(tb*(lb-ta-tc))
Ixyc = (lb - tc/2 - yc)*(lc/2 - xc)*(tc*lc)

Ixy = Ixya + Ixyb + Ixyc


#print(Ix, Iy, Ixy)
Xo = (Ixy*Iwx - Iy*Iwy)/((Ixy**2) - Ix*Iy)
Yo = (Ix*Iwx - Ixy*Iwy)/((Ixy**2) - Ix*Iy)

print ("Shear Centre Coordinates w.r.t the centroid: ", Xo, Yo)




