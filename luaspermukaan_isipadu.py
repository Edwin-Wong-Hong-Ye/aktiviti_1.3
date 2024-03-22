#Atur cara mengira jumlah luas permuklaan dan isi padu tangiki yang berbentuk silinder

#Isytiharkan pemboleh ubah & pemalar
pi=22/7
jejari=float(input('Sila masukkan jejari:'))
tinggi=float(input('Sila masukkan tinggi:'))

#Proses pengiraan(luas)
luas_bulatan=pi*jejari*jejari
circumference=2*pi*jejari
luas_rectangle=(2*jejari*pi)*tinggi
jumlah_luas=(2*luas_bulatan)+luas_rectangle

#Proses pengiraan(isipadu)
isipadu=luas_bulatan*tinggi

#Output
print('Jumlah luas permukaan bagi tangki air yang berbentuk silider ialah',round(jumlah_luas,2),'dan isi padunya ialah',round(isipadu,2),'.')
