sal = 3000000
hra = 38000*12
sd = 50000
pf = 11000*12
s80c = 150000
s80d = 25000
s = 25000
p = 26000
e = 400000
tf = 2400
rei = s+p+e+tf
taxable = sal - (hra+sd+pf+s80c+s80d+rei)
inhand=hra+sd+rei
ta10 = 0.30
mytax = 112500+(taxable - 1000000)*ta10
ih=taxable-mytax
tih=ih+inhand
print (tih/12)