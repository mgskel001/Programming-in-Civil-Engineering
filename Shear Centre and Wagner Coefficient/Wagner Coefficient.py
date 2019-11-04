#Wagner Coefficient Program
#by Keletso Mogashoa

from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title('Shear Centre & Wagner Coefficient')
#root.wm_attributes('-topmost', 1)

sum_int1, sum_int2 = 0,0
def calculate():
    global Bc, tc, t1, B1, hw, tw, D, t2, B2, tL, DL, sum_int1, sum_int2

    Bc = float(Bc_.get())
    tc = float(tc_.get())
    t1 = float(t1_.get())
    B1 = float(B1_.get())
    hw = float(hw_.get())
    tw = float(tw_.get())
    D = float(D_.get())
    t2 = float(t2_.get())
    B2 = float(B2_.get())
    tL = float(tL_.get())
    DL = float(DL_.get())
    
    #Intermediate Calc
    DL_tc = DL  - tc  
    hc = D  - t2/2
    hb = hw  - t1/2 + t2/2
    h = t1 + hw + t2  
    #centroid
    y1 = B2 *(t2**2)/2
    y2 = hw *tw *(t2 + hw/2)
    y3 = B1 *t1*(hw + t2 + t1/2)
    y4 = Bc*tc*(D - tc/2)
    y5 = DL_tc*tL*(D - tc - DL_tc/2)
    y6 = y5

    A1 = B2*t2
    A2 = hw*tw
    A3 = B1*t1
    A4 = Bc*tc
    A5 = DL_tc*tL
    A6 = A5

    #ȳ
    y_ = (y1 + y2 + y3 + y4 + y5 + y6)/(A1 + A2 + A3 + A4 + A5 + A6)

    #Iy
    Iy1 = (t2*(B2**3))/12
    Iy2 = (hw*(tw**3))/12
    Iy3 = (t1*(B1**3))/12
    Iy4 = (tc*(Bc**3))/12
    Iy5 = (DL_tc*(tL**3))/12 + DL_tc*tL*(Bc/2 - tL/2)**2
    Iy6 = Iy5
    Iy = (Iy1 + Iy2 + Iy3 + Iy4 + Iy5 + Iy6)

    #Ix
    Ix1 = (B2*(t2**3))/12 + B2*t2*(y_ - t2/2)**2
    Ix2 = (tw*(hw**3))/12 + tw*hw*(y_ - hw/2 - t2)**2
    Ix3 = (B1*(t1**3))/12 + B1*t1*(t2 + hw + t1/2 - y_)**2
    Ix4 = (Bc*(tc**3))/12 + Bc*tc*(D - tc/2 - y_)**2
    Ix5 = (tL*(DL_tc**3))/12 + DL_tc*tL*(D - tc - DL_tc/2 - y_)**2
    Ix6 = Ix5
    Ix = (Ix1 + Ix2 + Ix3 + Ix4 + Ix5 + Ix6)

  

    #CraneBeamCalcs
    Lcm = DL - tc/2
    bcm = Bc - tL
    hcm = D - t2/2 - tc/2
    hwm = D - (t1 + tc)/2 - t2/2
    gamma = ((bcm - B1)/2)*hcm + B1*hwm/2

    Iwx1 = (Lcm*bcm/2)*((hcm*bcm - hcm*B1) + hwm*B1 + bcm*Lcm/2)*tL
    Iwx2 =((bcm - B1)/6)*((hwm*(B1**2)/2) + B1*hwm*bcm/4 + gamma*bcm + gamma*B1/2)*tc
    Iwx3 = (B1**3)*(hwm/12)*(t1 + tc)
    Iwx = Iwx1 + Iwx2 + Iwx3

    y = Iwx/Iy
    ysc = y + t1/2
    y0 = y_ - ysc


    #Wagner Coefficient
    #X1
    E1_x1 = B2/2
    E2_x1 = tw/2
    E3_x1 = B1/2
    E4_x1 = Bc/2
    E5_x1 = Bc/2
    E6_x1 = -Bc/2 + tL
    X1 = [E1_x1, E2_x1, E3_x1, E4_x1, E5_x1, E6_x1]

    #X2
    E1_x2 = -B2/2
    E2_x2 = -tw/2
    E3_x2 = -B1/2
    E4_x2 = -Bc/2
    E5_x2 = Bc/2 - tL
    E6_x2 = -Bc/2
    X2 = [E1_x2, E2_x2, E3_x2, E4_x2, E5_x2, E6_x2]
    
    #Y1
    E1_y1 = y_
    E2_y1 = y_ - t2
    E3_y1 = y_ - D + tc + t1
    E4_y1 = y_ - D + tc
    E5_y1 = y_ - D + DL
    E6_y1 = y_ - D + DL
    Y1 = [E1_y1, E2_y1, E3_y1, E4_y1, E5_y1, E6_y1]

    #Y2
    E1_y2 = y_ - t2
    E2_y2 = y_ - D + tc + t1
    E3_y2 = y_ - D + tc
    E4_y2 = y_ - D
    E5_y2 = y_ - D + tc
    E6_y2 = y_ - D + tc
    Y2 = [E1_y2, E2_y2, E3_y2, E4_y2, E5_y2, E6_y2]

    #Integral Calcs
    Int1, Int2 = [],[]
    for i in range (len(X1)):
        
        Int1.append((1/6)*((X2[i]**3 - X1[i]**3)*(Y2[i]**2 - Y1[i]**2)))
        Int2.append((1/4)*((X2[i] - X1[i])*(Y2[i]**4 - Y1[i]**4)))

        sum_int1 += Int1[i]
        sum_int2 += Int2[i]
      

    #β
    beta = (1/Ix)*(sum_int1 + sum_int2) - 2*y0
    sum_int1, sum_int2 = 0,0

    ans_y_.set(round(y_,3))
    ans_Iy.set(round(Iy,3))
    ans_Ix.set(round(Ix,3))
    ans_y0.set(round(y0,3))
    ans_beta.set(round(beta,3))

#Insert Image of section
image = PhotoImage(file="Section1.png")
pic = Label(root, image=image).grid(row=0, column=5, columnspan=4, rowspan=25, sticky=W+E+N+S)

#labels for dimension input
Dim_label = Label(root, text = 'Dimensions (mm)').grid(row=2, column=0)
Bc_label = Label(root, text = 'Bc').grid(row=3, column=0)
tc_label = Label(root, text = 'tc').grid(row=4, column=0)
t1_label = Label(root, text = 't1').grid(row=5, column=0)
B1_label = Label(root, text = 'B1').grid(row=6, column=0)
hw_label = Label(root, text = 'hw').grid(row=7, column=0)
tw_label = Label(root, text = 'tw').grid(row=8, column=0)
D_label = Label(root, text = 'D').grid(row=9, column=0)
t2_label = Label(root, text = 't2').grid(row=10, column=0)
B2_label = Label(root, text = 'B2').grid(row=11, column=0)
tL_label = Label(root, text = 'tL').grid(row=12, column=0)
Dl_label = Label(root, text = 'DL').grid(row=13, column=0)

#Labels for outputs
Y_label = Label(root, text = 'ȳ').grid(row=16, column=0)
Iy_label = Label(root, text = 'Iy').grid(row=17, column=0)
Ix_label = Label(root, text = 'Ix').grid(row=18, column=0)
y0_Label = Label(root, text = 'Shear Centre (y0)').grid(row=19, column=0)
beta_Label = Label(root, text = 'β').grid(row=20, column=0)



#Entries for dimension input

Bc_ = Entry(root)
Bc_.grid(row=3, column=1)
tc_ = Entry(root)
tc_.grid(row=4, column=1) 
t1_ = Entry(root)
t1_.grid(row=5, column=1) 
B1_ = Entry(root)
B1_.grid(row=6, column=1) 
hw_ = Entry(root)
hw_.grid(row=7, column=1) 
tw_ = Entry(root)
tw_.grid(row=8, column=1) 
D_ = Entry(root)
D_.grid(row=9, column=1) 
t2_ = Entry(root)
t2_.grid(row=10, column=1) 
B2_ = Entry(root)
B2_.grid(row=11, column=1) 
tL_ = Entry(root)
tL_.grid(row=12, column=1) 
DL_ = Entry(root)
DL_.grid(row=13, column=1) 

#Display

ans_y_ = StringVar()
display1 = Entry(root, textvariable = ans_y_)
display1.grid(row=16, column=1)

ans_Iy = StringVar()
display2 = Entry(root, textvariable = ans_Iy)
display2.grid(row=17, column=1)

ans_Ix = StringVar()
display3 = Entry(root, textvariable = ans_Ix)
display3.grid(row=18, column=1)

ans_y0 = StringVar()
display4 = Entry(root, textvariable = ans_y0)
display4.grid(row=19, column=1)

ans_beta = StringVar()
display5 = Entry(root, textvariable = ans_beta)
display5.grid(row=20, column=1)

#Button
btnReset=Button(root, padx=10, pady=8, bd=1, fg="black", width=10, text='Calculate', command = calculate).grid(row=15, column=0, columnspan=2)





root.mainloop()
