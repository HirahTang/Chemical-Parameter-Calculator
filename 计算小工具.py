#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:22:25 2017

@author: TH
"""

from tkinter import *
desktop = Tk()
desktop.title("计算小工具")

def Hcalc():
     hnumber = [0,0,0,0,0,0]
     
     try:
         hnumber[0] = float(h0.get())
     except:
         hnumber[0] = 0
         
     try:
         hnumber[1] = float(h1.get())
     except:
         hnumber[1] = 0
         
     try:
         hnumber[2] = float(h2.get())
     except:
         hnumber[2] = 0    
         
     try:
         hnumber[3] = float(h3.get())
     except:
         hnumber[3] = 0
         
     try:
         hnumber[4] = float(h4.get())
     except:
         hnumber[4] = 0
         
     try:
         hnumber[5] = float(h5.get())
     except:
         hnumber[5] = 0
         
         
         
         
#     hnumber[0] = float(h[0].get())
#     hnumber[1] = float(h[1].get())
#     hnumber[2] = float(h[2].get())
#     hnumber[3] = float(h[3].get())
#     hnumber[4] = float(h[4].get())
#     hnumber[5] = float(h[5].get())
     try:
         anumber = float(an.get())
     except:
         anumber = 0
     
     try:
         bnumber = float(bn.get())
     except:
         bnumber = 0
         
     try:
         cnumber = float(cn.get())
     except:
         cnumber = 0
         
     try:
         dnumber = float(dn.get())
     except:
         dnumber = 0
         
     try:
         enumber = float(en.get())
     except:
         enumber = 0
         
     try:
         fnumber = float(fn.get())
     except:
         fnumber = 0
    
#anumber = float(an.get())
#     bnumber = float(bn.get())
#     cnumber = float(cn.get())
#     dnumber = float(dn.get())
#     enumber = float(en.get())
#     fnumber = float(fn.get())
     snumber = [0,0,0,0,0,0]
     try:
         snumber[0] = float(s0.get())
     except:
         snumber[0] = 0
         
     try:
         snumber[1] = float(s1.get())
     except:
         snumber[1] = 0
         
     try:
         snumber[2] = float(s2.get())
     except:
         snumber[2] = 0    
         
     try:
         snumber[3] = float(s3.get())
     except:
         snumber[3] = 0
         
     try:
         snumber[4] = float(s4.get())
     except:
         snumber[4] = 0
         
     try:
         snumber[5] = float(s5.get())
     except:
         snumber[5] = 0
         
     try:
         temperature = float(temp.get())
     except:
         temperature = 298
         
     summah = (dnumber * hnumber[3] + enumber * hnumber[4] + fnumber * hnumber[5]) - (anumber * hnumber[0] + bnumber * hnumber[1] + cnumber * hnumber[2])    
     summas = (dnumber * snumber[3] + enumber * snumber[4] + fnumber * snumber[5]) - (anumber * snumber[0] + bnumber * snumber[1] + cnumber * snumber[2])   
     gibbs = summah - temperature * summas * 0.001
     resulth.delete(0,END)
     results.delete(0,END)
     resultg.delete(0,END)
     resulth.insert(0, summah)
     results.insert(0, summas)
     resultg.insert(0, gibbs)
    
#    i = [0, 1, 2, 3, 4, 5]
#    hnumber = [0,0,0,0,0,0]
#    for i in h:
#        hnumber[i] = h[i].get()
#        
#    print (hnumber)
        
#    print ('nickynicky')

def empty_them_all():
    
    resulth.delete(0,END)
    results.delete(0,END)
    resultg.delete(0,END)
    s0.delete(0,END)
    s1.delete(0,END)
    s2.delete(0,END)
    s3.delete(0,END)
    s4.delete(0,END)
    s5.delete(0,END)
    h0.delete(0,END)
    h1.delete(0,END)
    h2.delete(0,END)
    h3.delete(0,END)
    h4.delete(0,END)
    h5.delete(0,END)
    an.delete(0,END)
    bn.delete(0,END)
    cn.delete(0,END)
    dn.delete(0,END)
    en.delete(0,END)
    fn.delete(0,END)
    temp.delete(0,END)
    
    
    

label1 = Label(desktop, text = '反应方程式：').grid(column = 5, row = 5)
label2 = Label(desktop, text = '物质a化学计量数').grid(column = 5, row = 10)
label3 = Label(desktop, text = '物质b化学计量数').grid(column = 20, row = 10)
label4 = Label(desktop, text = '物质c化学计量数').grid(column = 35, row = 10)
label5 = Label(desktop, text = '物质d化学计量数').grid(column = 5, row = 17)
label6 = Label(desktop, text = '物质e化学计量数').grid(column = 20, row = 17)
label7 = Label(desktop, text = '物质f化学计量数').grid(column = 35, row = 17)

label8 = Label(desktop, text = 'a').grid(column = 10, row = 15)
label9 = Label(desktop, text = 'b').grid(column = 25, row = 15)
label10 = Label(desktop, text = 'c').grid(column = 40, row = 15)
label11 = Label(desktop, text = 'd').grid(column = 10, row = 18)
label12 = Label(desktop, text = 'e').grid(column = 25, row = 18)
label13 = Label(desktop, text = 'f').grid(column = 40, row = 18)

label14 = Label(desktop, text = '+').grid(column = 15, row = 15)
label15 = Label(desktop, text = '+').grid(column = 30, row = 15)
label16 = Label(desktop, text = '+').grid(column = 15, row = 18)
label17 = Label(desktop, text = '+').grid(column = 30, row = 18)
label18 = Label(desktop, text = '----------->').grid(column = 5, row = 16)

label19 = Label(desktop, text = '标准摩尔生成焓(KJ/mol)').grid(column = 10, row = 20)
label20 = Label(desktop, text = '标准熵(J/(mol·K))').grid(column = 15, row = 20)
label21 = Label(desktop, text = '反应温度(T):').grid(column = 25, row = 20)
label22 = Label(desktop, text = '化合物a').grid(column = 5, row = 25)
label23 = Label(desktop, text = '化合物b').grid(column = 5, row = 30)
label24 = Label(desktop, text = '化合物c').grid(column = 5, row = 35)
label25 = Label(desktop, text = '化合物d').grid(column = 5, row = 40)
label26 = Label(desktop, text = '化合物e').grid(column = 5, row = 45)
label27 = Label(desktop, text = '化合物f').grid(column = 5, row = 50)

label28 = Label(desktop, text = '标准摩尔反映焓变:').grid(column = 25, row = 25)
label29 = Label(desktop, text = '标准摩尔反应熵:').grid(column = 25, row = 30)
label30 = Label(desktop, text = '标准摩尔反应吉布斯函数变:').grid(column = 25, row = 35)
label31 = Label(desktop, text = 'K(如不设置则为默认298K)').grid(column = 35, row = 20)
label32 = Label(desktop, text = 'KJ/mol').grid(column = 35, row = 25)
label33 = Label(desktop, text = 'J/(mol·K)').grid(column = 35, row = 30)
label34 = Label(desktop, text = 'KJ/mol').grid(column = 35, row = 35)
#以上内容均为绘制文本

h = [0,0,0,0,0,0]
s = [0,0,0,0,0,0]
h0 = Entry(desktop)
h0.grid(column = 10, row = 25) #the h of a 
s0 = Entry(desktop)
s0.grid(column = 15, row = 25) #the s of a
h1 = Entry(desktop)
h1.grid(column = 10, row = 30) #the h of b
s1 = Entry(desktop)
s1.grid(column = 15, row = 30) #the s of b
h2 = Entry(desktop)
h2.grid(column = 10, row = 35) #the h of c
s2 = Entry(desktop)
s2.grid(column = 15, row = 35) #the s of c
h3 = Entry(desktop)
h3.grid(column = 10, row = 40) #the h of d
s3 = Entry(desktop)
s3.grid(column = 15, row = 40) #the s of d
h4 = Entry(desktop)
h4.grid(column = 10, row = 45) #the h of e
s4 = Entry(desktop)
s4.grid(column = 15, row = 45) #the s of e
h5 = Entry(desktop)
h5.grid(column = 10, row = 50) #the h of f
s5 = Entry(desktop)
s5.grid(column = 15, row = 50) #the s of f
temp = Entry(desktop)
temp.grid(column = 30, row = 20)

an = Entry(desktop)
an.grid(column = 5, row = 15)
bn = Entry(desktop)
bn.grid(column = 20, row = 15)
cn = Entry(desktop)
cn.grid(column = 35, row = 15)
dn = Entry(desktop)
dn.grid(column = 5, row = 18)
en = Entry(desktop)
en.grid(column = 20, row = 18)
fn = Entry(desktop)
fn.grid(column = 35, row = 18)

resulth = Entry(desktop)
resulth.grid(column = 30, row = 25)
results = Entry(desktop)
results.grid(column = 30, row = 30)
resultg = Entry(desktop)
resultg.grid(column = 30, row = 35)

calculate = Button(desktop, text = '计算', command = Hcalc).grid(row = 55, column = 25)
empty = Button(desktop, text = '清空', command = empty_them_all).grid(row = 55, column = 30)


desktop.mainloop()
