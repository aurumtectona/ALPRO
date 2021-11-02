#KASUS 1
#MENENTUKAN LUAS DAN KELILING SEGITIGA, LINGKARAN DAN PERSEGI PANJANG

#menghitung luas segitiga
#kamus
#a = int(input("masukkan alas : "))
#t = int(input("masukkan tinggi : "))
#algoritma
#L = print("luas segitiga adalah : ") + int(input(a * t / 2))

#menghitung keliling segitiga
#kamus
#s = int(input("masukkan sisi segitiga : "))
#algoritma
#k = print("keliling segitiga adalah : ") + int(input(s * 3))

#menghitung luas lingkaran
#kamus
#phi = int(input("masukkan phi : "))
#r = int(input("masukkan jari-jari : "))
#algoritma
#L = print("luas lingkaran adalah : ") + int(input(phi * r * r))

#menghitung keliling lingkaran
#kamus
#phi = int(input("masukkan phi : "))
#r = int(input("masukkan jari-jari : "))
#algoritma
#k = print("keliling lingkaran adalah : ") + int(input(phi * r * 2))

#menghitung luas persegi panjang
#kamus
#p = int(input("masukkan panjang : "))
#l = int(input("masukkan lebar : "))
#algoritma
#L = print("luas persegi panjang adalah : ") + int(input(p * l))

#menghitung keliling persegi panjang
#kamus
#p = int(input("masukkan panjang : "))
#l = int(input("masukkan lebar : "))
#algoritma
#K = print("keliling persegi panjang adalah : ") + int(input(2 * p + l))



#KASUS 2
#MENENTUKAN WAKTU PAGI, SIANG, SORE DAN MALAM

#kamus
#jam = int(input("masukkan waktu: "))
#algoritma
#if jam >= 7 and jam < 12:
    #print("pagi")
#elif jam >= 12 and jam < 15:
    #print("siang")
#elif jam >= 15 and jam < 18:
    #print("sore")
#elif jam >= 18 and jam < 24:
    #print("malam")
#else:
    #print("inputan salah")


#NAMA : NELLIS NERIA AURUM TECTONA
#NIM : A11.2020.12668
#KELAS : 4210

#MENGHITUNG FUNGSI NOTASI ALGORITMIK (8 * 7) + (80 - 99) / 2) * 120)

#Kamus
#angka1 = 8
#angka2 = 7
#angka3 = 80
#angka4 = 99
#angka5 = 2
#angka6 = 120

#hasil1 = int(angka1 * angka2) #fungsi perkalian 
#hasil2 = int(angka3 - angka4) #fungsi pengurangan
#hasil3 = int(hasil2 / angka5) #fungsi pembagian
#hasil4 = int(hasil1 + hasil3) #fungsi penjumlahan
#hasil5 = int(hasil4 * angka6) #hasil akhir

#Algoritma
#print("hasil dari fungsi pengurangan adalah " + str(hasil2))
#print("hasil dari fungsi perkalian adalah " + str(hasil1))
#print("hasil dari fungsi pembagian adalah " + str(hasil3))
#print("hasil dari fungsi pembagian adalah " + str(hasil4))
#print("hasil dari aritmatika ((8 * 7) + (80 - 99) / 2) * 120) adalah " + str(hasil5))


#MENGHITUNG FUNGSI PROSEDUR

#Kamus

#nama = "Nellis Neria Aurum Tectona"
#umur = "18"
#mafa = "cilok"
#mifa = "susu"
#hobby = "membaca"
#citacita = "engineer"

#Algortima

#print("Nama : " + str(nama))
#print("umur : " + str(umur))
#print("mafa : " + str(mafa))
#print("mifa : " + str(mifa))
#print("hobby : " + str(hobby))
#print("citacita : " + str (citacita))

#x = [12, 34, 23, 1, 3]
#penjumlahan dari variabel x
# s akan berisi hasi; penjumlahan 12 + 34 + 23 + 1 + 3
#s = 0
#s = s + x0 # s = 0 + 12, s = 12, #s++ sama aja dengan s
#s = s + x1


#nama : nellis neria aurum tectona
#nim : A11.2020.12668
#kelas : 4210

#VEKTOR

#kamus
#def vektorperkalian(v1, v2):
    #vektorkali = []
    #if len(v1) != len(v2):
        #return -1
    #else:
        #for a in range(len(v1)):
            #vektorkali.append(v1[a] * v2[a])
    #return vektorkali

#def vektorpembagian(v1, v2):
    #vektorbagi = []
    #if len(v1) != len(v2):
        #return -1
    #else:
        #for r in range(len(v1)):
            #vektorbagi.append(v1[r] // v2[r])
    #return vektorbagi

#def vektorpenjumlahan(v1, v2):
    #vektorjumlah = []
    #if len(v1) != len(v2):
        #return -1
    #else:
        #for u in range(len(v1)):
            #vektorjumlah.append(v1[u] + v2[u])
    #return vektorjumlah

#def vektorpengurangan(v1, v2):
    #vektorkurang = []
    #if len(v1) != len(v2):
        #return -1
    #else:
        #for m in range(len(v1)):
            #vektorkurang.append(v1[m] - v2[m])
    #return vektorkurang

#v1 = [9, 8, 7]
#v2 = [1, 2, 3]

#algoritma
#print("hasil dari vektor perkalian adalah" + str(vektorperkalian(v1, v2)))
#print("hasil dari vektor pembagian adalah " + str(vektorpembagian(v1, v2)))
#print("hasil dari vektor penjumlahan adalah " + str(vektorpenjumlahan(v1, v2)))
#print("hasil dari vektor pengurangan adalah " + str(vektorpengurangan(v1, v2)))

#nama : nellis neria aurum tectona
#nim : A11.2020.12668
#kelas : 4210

#MATRIKS

#kamus
#def matrikspenjumlahan(ma, mb):
    #b1 = len(ma)
    #k1 = len(ma[0])
    #b2 = len(mb)
    #k2 = len(mb[0])

    #if b1 != b2 or k1 != k2:
        #return -1
    #else:
        #hasiljumlah = [0] * b1
        #for d in range(b1):
            #hasiljumlah[d] = [0] * k1
        #for d in range(b1):
            #for c in range(k2):
                #hasiljumlah[d][c] = ma[d][c] + mb[d][c]
    #return hasiljumlah

#def matrikspengurangan(ma, mb):
    #b1 = len(ma)
    #k1 = len(mb[0])
    #b2 = len(ma)
    #k2 = len(mb[0])
    
    #if b1 != b2 or k1 != k2:
        #return -1
    #else:
        #hasilkurang = [0] * b1
        #for e in range(b1):
            #hasilkurang[e] = [0] * k1
        #for e in range(b1):
            #for f in range(k2):
                #hasilkurang[e][f] = ma[e][f] - mb[e][f]
    #return hasilkurang

#def matriksperkalian(ma, mb):
    #b1 = len(ma)
    #k1 = len(mb[0])
    #b2 = len(ma)
    #k2 = len(mb[0])

    #if b1 != b2 or k1 != k2:
        #return -1
    #else:
        #hasilkali = [0] * b1
        #for r in range(b1):
            #hasilkali[r] = [0] * k1
        #for r in range(b1):
            #for s in range(k2):
                #hasilkali[r][s] = ma[r][s] * mb[r][s]
    #return hasilkali

#def matrikspembagian(ma, mb):
    #b1 = len(ma)
    #k1 = len(mb[0])
    #b2 = len(ma)
    #k2 = len(mb[0])

    #if b1 != b2 or k1 != k2:
        #return -1
    #else:
        #hasilbagi = [0] * b1
        #for t in range(b1):
            #hasilbagi[t] = [0] * k1
        #for t in range(b1):
            #for u in range(k2):
                #hasilbagi[t][u] = ma[t][u] // mb[t][u]
    #return hasilbagi
#ma = [1, 2, 3, 4], [10, 20, 30, 40], [1, 1, 1, 1]
#mb = [5, 6, 7, 8], [15, 25, 35, 45], [2, 2, 2, 2]

#algoritma
#print("hasil dari matriks penjumlahan adalah " + str(matrikspenjumlahan(ma, mb)))
#print("hasil dari matriks pengurangan adalah " + str(matrikspengurangan(ma, mb)))
#print("hasil dari matriks perkalian adalah " + str(matriksperkalian(ma, mb)))
#print("hasil dari matriks pembagian adalah " + str(matrikspembagian(ma, mb)))

#nama : nellis neria aurum tectona
#nim : A11.2020.12668
#kelas : 4210

#print("NAMA : NELLIS NERIA AURUM TECTONA")
#print("NIM : A11.2020.12668")
#print("KELAS : 4210")
#print("MATA KULIAH : ALGORITMA PEMPROGRAMAN")

#def SelectionSort(n, A):
    #n = panjang list
    #a = listnya itu sendiri

    #nilai awalan untuk looping dengan index 0
    #i = 0

    #algoritma
    #while i != n:
        # looping j = i
            #j = 0 sampai dengan n / jumlah array
            # 0 sampai 5
        #for j in range(i, n):
            #buat perbandingan yang kondisinya harus di swap
            #nilai awal a2 = [11, 334, 523, 12, 12] #5
            #if A[i] > A[j]:
                #loop 0, i = 0 j = i / j = 0
                    # A[i] > A[j]
                    # A[0] > A[0]
                    # 11 > 11, false
                # Hasil a2 = [11, 334, 523, 12, 12] #5
                # j++

                #loop 1, i = 0 j = 1
                    # A[i] > A[j]
                    # A[0] > A[1]
                    # 11 > 334, false
                # hasil a2 = [11, 334, 523, 12, 12] #5
                #j++

                #loop 1, i = 0, j = 2
                    #A[i] > A[j]
                    #A[0] > A[2]
                    # 11 > 532, false
                #hasil a2 = [11, 334, 523, 12, 12] #5
                #j++

                #loop 1, i = 0 j = 3
                    #A[i] > A[j]
                    #A[0] > A[3]
                    #11 > 12, false
                #hasil a2 = [11, 334, 523, 12, 12] #5
                #j++

            # i = i + 1
            # i = 0 + 1
                #loop 1, i = 1 j = i / j = 1
                    #A[i] > A[j]
                    #A[1] > A[1]
                    #334 > 334, false
                #hasil a2 = [11, 334,523, 12, 12] #5
                #j++

                #loop 1, i = 1 j = i / j = 2
                    #A[i] > A[j]
                    #A[1] > A[2]
                    #334 > 523, false
                #hasil a2 = [11, 334, 523, 12,12] #5
                #j++
                # loop 1, i = 1 j = i / j = 3
                    #A[i] > A[j]
                    #A[1] > A[3]
                    #334 > 12, true
                #temp = A[j]
                    #temp = A[3]
                    #temp = 12
                #A[j] = A[i]
                    #A[3] = A[1]
                    #A[3] = 334
                #A[i] = temp
                    #A[1] = temp
                    #A[1] = 12
                #hasil a2 = [11, 334, 523, 12, 12] #5
                #j++

            #i = i + 1
            #i = 1 + 1
                #loop 1, i = 2 j = i / j = 2
                    #A[i] > A[j]
                    #A[2] > A[2]
                    #523 > 523, false
                #hasil a3 = [11, 12, 523, 334, 12] #5
                #j++

                #loop 1, i = 2 j = i / j = 2
                    #A[i] > A[j]
                    #A[2] > A[3]
                    #523 > 334, true
                #temp = A[j]
                    #temp = A[3]
                    #temp = 334
                #A[j] = A[i]
                    #A[3] = A[2]
                    #A[3] = 523
                #A[i] = temp
                    #A[2] = temp
                    #A[2] = 334
                #hasil a2 = [11, 12, 334, 523, 12] #5
                #j++

                #loop 1, i = 2 j = 1 / j = 4
                    #A[i] > A[j]
                    #A[2] > A[4]
                    #334 > 12, true
                #temp = A[j]
                    # temp = A[4]
                    #temp = 12
                #A[j] = A[i]
                    #A[4] = A[2]
                    #A[4] = 334
                #A[i] = temp
                    #A[2] = temp
                    #A[2] = 12
                #hasil a2 = [11, 12, 12, 523, 334] #5
                #j++
            
            #i = i + 1
            #1 = 2 + 1
                #loop 1, i = 3 j = i / j = 3
                    #A[i] > A[j]
                    #A[3] > A[3]
                    #523 > 523, false
                #hasil a2 = [11, 12, 12, 523, 334] #5
                #j++

                #loop 1, i = 3 j = i / j = 4
                    #A[i] > A[j]
                    #A[3] > A[4]
                    #523 > 334, true
                #temp = A[j]
                    #temp = A[4]
                    #temp = 334
                #A[j] = A[i]
                    #A[4] = A[3]
                    #A[4] = 523
                #A[i] = temp
                    #A[3] = temp
                    #A[3] = 334
                #Hasil a2 = [11, 12, 12, 12, 334, 523] #5
                #j++
            # i = i + 1
            # i = 3 + 1
                
                #loop 1, i = 4 j = i / j = 4
                    #A[i] > A[j]
                    #A[4] > A[4]
                    #523 > 523, false
                #hasil a2 = [11, 12, 12, 334, 523] #5
                #j++

                #temp = A[j]
                #A[j] = A[i]
                #A[i] = temp
            #print(A) #hasil loop 1-15
        #i=i+1
    #return A

#a2 = [11, 334, 523, 12, 12] #5
#print(SelectionSort(5, a2))

#print("NAMA : NELLIS NERIA AURUM TECTONA")
#print("NIM : A11.2020.12668")
#print("KELAS : 4210")

#n adalah panjang array
#a adalah array yang dimasukkan

#def insertionSort(n,A):
    #temp = 0 # menyimpan temporary data
    #for i in range(1, n): #looping dari 1 sampai ke n = 5
        #temp = A[i]
        #temp = A[1]
            # temp = 334
        
        #j = i - 1
        #j = 1 - 1
            #j = 0
        #while j >= 0 and temp < A[j]:
            #temp = A[1]
                #temp = 334
            #j = i - 1
                #j = 1 - 1
                    #j = 0
            #j >= 0 and temp < A[j]
                #j >= 0 and temp < A[0]
                    #0 >= 0 and 334 < 11 false, tidak bertukar
            #kondisi array a2 = [11, 334, 523, 12, 12]

            #i++ , i = 1 + 1 = 2
            #temp = A[i]
                #temp = A[2]
                    #temp = 523
            #j = i - 1
                #j = 2 - 1
                    # j = 1
            #j >= 0 and temp < A[j]
                #1 >= 0 and 523 < A[1]
                    #1 >= 0 and 523 < 334 false, tidak bertukar
            #Kondisi array a2 = [11, 334, 523, 12, 12]

            #i++, i = 2 + 1 = 3
            #temp = A[i]
                #temp = A[3]
                    #temp = 12
            #j = i - 1
                # j = 3 - 1
                    # j = 2
            #j >= 0 and temp < A[j]
                #2 >= 0 and 12 < A[12]
                    # 2 >= 0 and 12 < 523 true, bertukar
            #A[j + 1] = A[j]
                #A[2 + 1] = A[2]
                    #A[3] = A[2]
                        #A[3] = 523           
            #j = j - 1
                #j = 2 - 1
                    # j = 1
            #i = i - 2
                #i = 3 - 2
                    #i = 1
            #A[1 + 1] = temp
                #A[2] = 12
            #kondisi array a2 = [11, 334, 12, 523, 12]

            #i++, i = 0 + 1 = 1
            #temp = A[i]
                #temp = A[1]
                    #temp = 12
            #j = i - 1
                # j = 1 - 1
                    #j = 0
            #j >= 0 and temp < A[j]
                #0 >= 0 and 12 < 11 false, tidak bertukar
            #kondisi array a2 = [11, 12, 334, 523, 12]
            
            #i++, i = 1 + 1 = 2
            #temp = A[2]
                #temp = A[2]
                    #temp = 334
            #j = i - 1
                #j = 2 - 1
                    #j = 1
            #j >= 0 and temp < A[j]
                #1 >= 0 and 334 < A[1]
                # 1 >=0 and 334 < 12 False, tidak tukar
            # Kondisi Array a2 = [11, 12, 334, 523, 12] 
                    

            # i++, i=2+1=3
            # temp = A[i]
                # temp = A[3]
                    # temp = 523
            # j = i - 1
                # j = 3 - 1
                    # j = 2
            # j >= 0 and temp < A[j]
                # 2 >= 0 and 523 < A[2]
                    # 2 >= 0 and 523 < 334 False, tidak tukar
            # Kondisi Array a2 = [11, 12, 334, 523, 12] 

            # i++, i=3+1=4
            # temp = A[i]
                # temp = A[4]
                    # temp = 12
            # j = i - 1
                # j = 4 - 1
                    # j = 3
            # j >= 0 and temp < A[j]
                # 3 >= 0 and 12 < A[3]
                    # 3 >= 0 and 12 < 523 True, tukar
            # A[j+1] = A[j]
                # A[3+1] = A[3]
                    # A[4] = A[3]
                        # A[4] = 523
            # j = 3 - 1=2
            # i = 4 - 2=2
            # A[j+1]=temp
                # A[2+1] = 12
                    # A[3] = 12
            # Kondisi Array a2 = [11, 12, 334, 12, 523]

            # i++, i=2+1=3
            # temp = A[i]
                # temp = A[3]
                    # temp = 12
            # j = i - 1
                # j = 3 - 1=2
            # j >= 0 and temp < A[j]
                # 2 >= 0 and 12 < A[2]
                    # 2 >= 0 and 12 < 334 True, tukar
            # A[j+1] = A[j]
                # A[2+1] = A[2]
                    # A[3] = 334
            # j = 2 - 1=1
            # i = 3 - 2=1
            # A[j+1]=temp
                # A[1+1] = 12
                    # A[2] = 12
            # Kondisi Array a2 = [11, 12, 12, 334, 523]

            # i++, i=1+1=2
            # temp = A[i]
                # temp = 12
            # j = i - 1
                # j = 1
            # j >= 0 and temp < A[j]
                # 1 >= 0 and 12 < 12 False, tidak tukar
            # Kondisi Array a2 = [11, 12, 12, 334, 523]

            # i++, i=2+1=3
            # temp = A[i]
                # temp = 334
            # j = i - 1
                # j = 2
            # j >= 0 and temp < A[j]
                # 2 >= 0 and 334 < 12 False, tidak tukar
            # Kondisi Array a2 = [11, 12, 12, 334, 523]

            # i++, i=3+1=4
            # temp = A[i]
                # temp = 523
            # j = i - 1
                # j = 3
            # j >= 0 and temp < A[j]
                # 3 >= 0 and 523 < 334 False, tidak tukar
            # Kondisi Array a2 = [11, 12, 12, 334, 523]

            # i++, i=4+1=5
            # temp = A[5]
                # temp = error, maka out looping
            
            #A[j+1] = A[j]
            #j = j-1
            #i = i-2
        #A[j+1] = temp
        #return A

#a2 = [11, 334, 523, 12, 12] #5
#print(insertionSort(5, a2))

#print("NAMA : NELLIS NERIA AURUM TECTONA")
#print("NIM : A11.2020.12668")
#print("KELAS : 4210")

# n adalah panjang array
# A adalah array yang dimasukkan
#def insertionSort(n,A):
    #temp = 0 # menyimpan temporary data
    #for i in range(1, n): # looping dari 1 sampai ke n=5
        #temp = A[i]
        # temp = A[1]
            # temp = 9
        
        #j = i -1
        # j = 1 -1
            # j = 0
        #while j >= 0 and temp < A[j]:
            # temp = A[1]
                # temp = 9
            # j = i - 1
                # j = 1 -1
                    # j = 0
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[0]
                    # 0 >= 0 and 9 < 12 true, ditukar          

            #A[j + 1] = A[j]
                #A[0 + 1] = A[0]
                    #A[1] = 12
            #j = j - 1
                #j = 0 - 1
                    #j = -1
            #i = i - i
                #i = 1 - 1
                    #i = 0
            #A[j + 1] = temp
                #A[-1 + 1] = 9
                    #A[0] = 9
            #Kondisi array aa = [9, 12, 2003, 111, 90, 91, 10000]
            
            #i++, i = 0 + 1 = 1

            #temp = A[i]
                #temp = A[1]
                    #temp = A[12]
            #j = i - 1
                #j = 1 -1
                    #j = 0
            #j >= 0 and temp < A[j]
                #0 >= 0 and 12 < A[j]
                    # 0 >= 0 and 12 < 9 false, tidak ditukar
            #kondisi array aa = [9, 12, 2003, 111, 90, 91, 92, 10000]

            #i++, i = 1 + 1 = 2
            # temp = A[i]
                #temp = A[2]
                    #temp = A[2]
                        #emp = A[2003]
            #j = i - 1
                #j = 2 - 1
                    #j = 1 
            #j >= 0 and temp < A[j]
                #1 >= 0 and 2003 < A[j]
                    #1 >= 0 and 2003 < 12 false, tidak ditukar
            #kondisi array aa = [9, 12, 2003, 111, 90, 91, 92, 10000]

            #i++, i = 2 + 1 = 3

            #temp = A[i]
                #temp = A[3]
                    #temp = 111
            #j = i -1
                #j = 3 - 1
                    #j = 2
            #j >= 0 and temp < A[j]
                #2 >= 0 and 111 < 2003 true, ditukar
            #A[j + 1] = A[j]
                #A[2 + 1] = A[2]
                    #A[3] = 2003
            #j = j - 1
                #j = 2 - 1
                    #j = 1
            #i = i - 2
                #i = 3 - 2
                    #i = 1
            #A[j + 1] = temp
                #A[1 + 1] = temp 
                    #A[2] = 111
            #kondisi array aa = [9, 12, 111, 2003, 90, 91, 92, 10000]

            #i++, i = 1 + 1 = 2

            #temp = A[i]
                #temp = A[2]
                    #temp = 111
            #j = i - 1
                #j = 2 - 1
                    #j = 1
            #j >= 0 and temp < A[j]
                # 1 >= 0 and 111 < A[1]
                    # 1 >= 0 and 111 < 12 false, tidak ditukar
            #kondisi array aa = [9, 12, 111, 2003, 90, 91, 92, 10000]

            #i++, i = 2 + 1 = 3

            #temp = A[i]
                #temp = A[3]
                    #temp = 2003
            #j = i - 1
                #j = 3 - 1
                    #j = 2
            #j >= 0 and temp < A[j]
                #2 >= 0 and 2003 < A[2]
                    #2 >= 0 and 2003 < 111 false, tidak ditukar.

            #i++, i = 3 + 1 = 4

            #temp = A[i]
                #temp = A[4]
                    #temp = 90
            #j = i - 1
                #j = 4 - 1
                    #j = 3
            #j >= 0 and temp < A[j]
                #3 >= 0 and 90 < A[j]
                    #3 >= 0 and 90 < 2003 true, ditukar
            #A[j + 1] = A[j]
                #A[3 + 1] = A[3]
                    #A[4] = 2003
            #j = j - 1
                #j = 3 - 1
                    #j = 2
            #i = i - 2
                #i = 3 - 1
                    #j = 2
            #i = i - 2
                #i = 4 - 2
                    #i = 2
            #A[j + 1] = temp
                #A[2 + 1] = temp
                    #A[3] = 90
            #kondisi array aa = [9, 12, 111, 90, 2003, 91,92, 10000]

            #i++, i = 2 + 1 = 3

            #temp = A[i]
                #temp = A[3]
                    #temp = 2003
            #j = i - 1
                #j = 3 - 1
                    #j = 2
            #j >= 0 and temp < A[j]
                #2 >= 0 and 2003 < A[2]
                    #2 >= 0 and temp 2003 < 111 false, tidak ditukar
            #kondisi array aa = [9, 12, 111, 2003, 90, 91, 92, 10000]

            #i++, i = 3 + 1 = 4

            #temp = A[i]
                #temp = A[4]
                    #temp = 90
            #j = i + 1
                #j = 4 - 1
                    #j = 3
            #j >= 0 and temp < A[j]
                #3 >= 0 and 90 < A[3]
                    #3 >= 0 and 90 < 2003 true, ditukar
            #A[j + 1] = A[j]
                #A[3+1] = A[3]
                    #A[4] = 2003
            #j = j - 1
                #j = 3 - 1
                    #j = 2
            #i = i - 1
                #i = 4 - 2
                    #i = 2
            #A[j + 1] = temp
                #A[2 + 1] = temp
                    #A[3] = 90
            #kondisi array aa = [9, 12, 111, 90, 2003, 91, 92, 10000]
            
            #i++ i = 2 + 1 = 3
            #temp = A[i]
                #temp = A[3]
                    #temp = 90
            #j = i - 1
                #j = 3 - 1
                    #j = 2
            #j >= 0 and temp < A[j]
                #2 >= 0 and 90 < A[2]
                    #2 >= 0 and 90 < 111 true, ditukar
            #A[j + 1] = A[j]
                #A[2 + 1] = A[2]
                    #2 >= 0 and 90 < 111 true, ditukar
            #A[j + 1] = A[j]
                #A[2 + 1] = A[2]
                    #A[3] = 111
            #j = j + 1
                #j = 2 + 1
                    #j = 1
            #i = i - 2
                #i = 3 - 2
                    #i = 1
            #A[j + 1] = temp
                #A[1 + 1] = 90
                    #A[2] = 90
            #kondisi array aa = [9, 12, 90, 111, 2003, 91, 92, 10000]

            #i++, i = 1 + 1 = 2

            #temp = A[i]
                #temp = A[2]
                    #temp = 90
            #j = i - 1
                #j = 2 - 1
                    #j = 1
            #j >= 0 and temp < A[j]
                #1 >= 0 and 90 < A[1]
                    #1 >= 0 and 90 , 12 false, tidak ditukar
            #kondisi array aa = [9, 12, 90, 111, 2003, 91, 92, 10000]

            #i++, i = 2 + 1 = 3
            #temp = A[i]
                #temp = A[3]
                    #temp = 111
            #j = i - 1
                #j = 3 - 1
                    #j = 2
            #j >= 0 and temp < A[j]
                #2 >= 0 and 111 < A[2]
                    #2 >= 0 and 111 < 90 false, tidak ditukar
            #kondisi array aa = [9, 12, 90, 111, 2003, 91, 92, 10000]

            #i++, i = 3 + 1 = 4

            #temp = A[i]
                #temp = A[4]
                    #temp = 2003
            #j = i - 1
                #j = 4 - 1
                    #j = 3
            #j >= 0 and temp < A[j]
                #3 >= 0 and 2003 < A[3]
                    #3 >= 0 and 2003 < 111 false, tidak ditukar
            #kondisi array aa = [9, 12, 90, 111, 2003, 91, 92, 10000]

            #i++ i = 4 + 1 = 5
            #temp = A[i]
                #temp = A[5]
                    #temp = 91
            #j = i + 1
                #j = 5 - 1
                    #j = 4
            #j >= 0 and temp < A[j]
                #j >= 0 and 91 < A[4]
                    #j >= 0 and 91 < 2003 true, ditukar
            #A[j + 1] = A[j]
                #A[4 + 1] = A[4]
                    #A[5] = 2003
            #j = j - 1
                #j = 4 - 1
                    #A[5] = 2003
            #j = j - 1
                #j = 4 - 1
                    #j = 3
            #i = i - 2
                #i = 5 - 2
                    #i = 3
            #A[j + 1] = temp
                #A[3 + 1] = 91
                    #A[4] = 91
            #kondisi array aa = [9, 12, 90, 111, 91, 2003, 92, 10000]
            
            #i++, i = 3 + 1 = 4
            #temp = A[i]
                #temp = A[4]
                    #temp = 91
            #j = i - 1
                #j = 4 - 1
                    #j = 3
            #j >= 0 and temp < A[j]
                #3 >= 0 and 91 < A[3]
                    #3 >= 0 and 91 < 111 true, ditukar
            #A[j + 1] = A[j]
                #A[3 + 1] = A[3]
                    #A[4] = 111
            #j = j - 1
                #j = 3 - 1
                    #j = 2
            #A[j + 1] = temp
                #A[2 + 1] = 91
                    #A[3] = 91
            #Kondisi array aa = [9, 12, 90, 91, 111, 2003, 92, 10000]

            #i++, i = 2 + 1 = 3

            #temp = A[i]
                #temp = A[3]
                    #temp = 91
            #j = i - 1
                #j = 3 - 1
                    #j = 2
            #j >= 0 and temp < A[j]
                #2 >= 0 and 91 < A[2]
                    #2 >= 0 and 91 < 90 false, tidak ditukar
            #kondisi array aa = [9, 12, 90, 91, 111, 2003, 92, 10000]

            #i++ i = 3 + 1 = 4

            #temp = A[i]
                #temp = A[4]
                    #temp = 111
            #j = i - 1
                #j = 4 - 1
                    #j = 3
            #j >= 0 and temp < A[j]
                #3 >= 0 and 111 < A[3]
                    #3 >= 0 and 111 < 91 false, tidak ditukar
            #kondisi array aa = [9, 12, 90, 91, 111, 2003, 92, 10000]

            #i++ i = 4 + 1 = 5

            #temp = A[i]
                #temp = A[5]
                    #temp = 2003
            #j = i + 1
                #j = 5 - 1
                    #j = 4
            #j >= 0 and temp < A[j]
                #4 >= 0 and temp < A[4]
                    #4 >= 0 and 2003 < 111 false, tidak bertukar
            
            #i++ i = 5 + 1 = 6

            #temp = A[i]
                #temp = A[6]
                    #temp = 92
            #j = i - 1
                #j = 6 - 1
                    #j = 5
            #j >= 0 and temp < A[j]
                #5 >= 0 and 92 < A[5]
                    #5 >= 0 and 92 < 2003 true, ditukar
            #A[j + 1] = A[j]
                #A[5 + 1] = A[5]
                    #A[6] = 2003
            #j = j - 1
                #j = 5 - 1 
                    #j = 4
            #i = i - 2
                #i = 6 - 2
                    #i = 4
            #A[j + 1] = temp
                #A[4 + 1] = 92
                    #A[5] = 92
            #Kondisi array aa = [9, 12, 90, 91, 111, 92, 2003, 10000]

            #i++ i = 4 + 1 = 5

            #temp = A[i]
                #temp = A[5]
                    #temp = 92
            #j = i - 1
                #j = 5 - 1
                    #j = 4
            #j >= 0 and temp < A[j]
                #A[4 + 1] = A[4]
                    #A[5] = 111
            #j = j - 1
                #j = 4 - 1
                    #j = 3
            #i = i - 2
                #i = 5 - 2
                    #i = 3
            #A[j + 1] = temp 
                #A[3 + 1] = 92
                    #A[4] = 92
            #Kondisi array aa = [9, 12, 90, 91, 92, 111, 2003, 10000]

            #i++ i = 3 + 1 = 4
            #temp = A[i]
                #temp = A[4]
                    #temp = 92
            #j = i - 1
                #j = 4 - 1
                    #j = 3
            #j >= 0 and temp < A[j]
                #3 >= 0 and 92 < A[3]
                    #3 >= 0 and 92 < 91 false, tidak ditukar
            #kondisi array aa = [9, 12, 90, 91, 92, 111, 2003, 10000]

            #i++ i = 4 + 1 = 5

            #temp = A[i]
                #temp = A[5]
                    #temp = 111
            #j = i - 1
                #j = 5 - 1
                    #j = 4
            #j >= 0 and temp < A[j]
                #4 >= 0 and 111 < A[4]
                    #4 >= 0 and 111 < 92 false, tidak ditukar
            #kondisi array aa = [9, 12, 90, 91, 92, 111, 2003, 10000]

            #i++, i = 5 + 1 = 6

            #temp = A[i]
                #temp = A[6]
                    #temp = 2003
            #j = i - 1
                #j = 6 - 1
                    #j = 5
            #j >= 0 and temp < A[j]
                #5 >= 0 and 2003 < 111 false, tidak ditukar
            #kondisi array aa = [9, 12, 90, 91, 92, 111, 2003, 10000]

            #i++, i = 6 + 1 = 7

            #temp = A[i]
                #temp = A[7]
                    #temp = 10000
            #j = i - 1
                #j = 7 - 1
                    #j = 6
            #j >= 0 and temp < A[j]
                #6 >= 0 and 10000 < A[6]
                    #6 >= 0 and 10000 < 2003 false, tidak ditukar
            #kondisi array aa = [9, 12, 90, 91, 92, 111, 2003, 10000]

            #i++ i = 7 + 1 = 8
            #temp = A[i]
                #temp = A[8]
                    #temp = error, out looping
            #A[j+1] = A[j]
            #j = j-1
            #i = i-2
        #A[j+1]=temp
    #return A

#aa = [12, 9, 2003, 111, 90, 91, 92, 10000] #5
#print (insertionSort(8, aa))

#print("NAMA: NELLIS NERIA AURUM TECTONA")
#print("NIM: A11.2020.12668")
#print("KELAS: 4210")
#print("\n")
#print("1. Bubble sort")
#def Bubble(n, A):
    #n merupakan panjang array, A merupakan array
    #kamus lokal
    #swap = False
    #algoritma
    #while not swap:
        #swap = True
        #for s in range(1, n):
            #if A[s-1]>A[s]:
                #swap = False
                #temp = A[s]
                #A[s] = A[s-1]
                #A[s-1] = temp
    #return A

#def binary(k,n,A):
    #parameter k merupakan bilangan yang dicari
    # n merupakan panjang array, a merupakan array
    #kamus lokal
    #found = False
    #bb = 0 #left
    #ba = n-1 #right
    #algoritma
    #while bb <= ba and not found:
        #mid =(ba + bb) // 2 #middle
        #if A[mid] == k:
            #found = True
        #else:
            #if A[mid] > k:
                #ba = mid-1
            #else:
                #bb = mid+1
    #return found

#list =[33, 11, 22, 99, 100, 102, 200, 50, 20]
#cari = int(input("cari angka: "))
#print("hasil bubble sort adalah: ", Bubble(9,list))
#print("bubble + binary: ", binary (cari,7, Bubble(7,list)))

#print("\n")

#print("2. selection sort dan binary search")
#def selection(n,A):
    #n=panjang list
    #a=listnya
    #i=0
    #while i != n: #apabila n != 0
        #looping j=i
        #j=0 sampai dengan n atau jumlah array
        #0 sampai 5
        #for j in range (i,n):
            #buat perbandingan yang kondisinya harus di swap
            #if A[i] > A[j]:
                #temp = A[j]
                #A[j] = A[i]
                #A[i] = temp
        #i = i + 1
    #return A
#def binary(k,n,A):
    #parameter k merupakan bilangan yang dicari
    # n merupakan panjang array, a merupakan array
    #kamus lokal
    #found = False
    #bb = 0 #left
    #ba = n-1 #right
    #algoritma
    #while bb <= ba and not found:
        #mid =(ba + bb) // 2 #middle
        #if A[mid] == k:
            #found = True
        #else:
            #if A[mid] > k:
                #ba = mid-1
            #else:
                #bb = mid+1
    #return found
#list = [11, 5, 13, 14, 7, 17, 16]
#cari = int(input("cari angka: "))
#print("hasil selection sort: ", selection(7, list))
#print("selection dan binary: ", binary(cari, 7, selection(7, list)))

#print("\n")

#print(" insertion sort dan binary search")
#def insertion(C):
    #mengurutkan insertion sort
    #c merupakan list
    #i = 0
    #while i != (len(C)):
        #for j in range(i, len(C)):
            #if C[i] > C[j]:
                #temp = C[j]
                #C[j] = C[i]
                #C[i] = temp
        #i +=1
    #return C
#def binary(k,n,A):
    #parameter k merupakan bilangan yang dicari
    # n merupakan panjang array, a merupakan array
    #kamus lokal
    #found = False
    #bb = 0 #left
    #ba = len(A)-1 #right
    #algoritma
    #while bb <= ba and not found:
        #mid =(ba + bb) // 2 #middle
        #if A[mid] == k:
            #found = True
        #else:
            #if A[mid] > k:
                #ba = mid-1
            #else:
                #bb = mid+1
    #return found
#list = [145, 77, 20, 1, 120, 3, 4]
#cari = int(input("cari angka: "))
#print("hasil insertion sort: ", insertion(list))
#print("insertion dan binary: ", binary (cari, 7, insertion(list)))

#nama : nellis neria aurum tectona
#nim : A11.2020.12668
#kelas : 4210

#print("NAMA: NELLIS NERIA")
#print("NIM: A11.2020.12668")
#print("KELAS: 4210")

#print("\n")

#def LinierSearch(k,n,A):
    #K merupakan bilangan yang dicari
    #n merupakan panjang array
    #A merupakan array
#kamus lokal
    #found = False
    #templast = A[n - 1]
    #A[n - 1] = k
    #i = 0
    #algoritma
    #while A[i] != k:
        #i=i+1
    #A[n - 1] = templast
    #if i < n - 1 or k == A[n - 1]:
        #found = True
    #return found

#list = [3, 7, 9, 13, 15, 16, 17, 11]
#print("hasil linier search list [3, 7, 9, 13, 15, 16, 17, 11] adalah", LinierSearch(15, 8, list))


#print("nama: nellis neria")
#print("nim: A11.2020.12668")
#print("kelas: 4210")

#mengitung volume air yang dibutuhkan untuk mandi selama satu bulan

#kamus
#p = int(input("masukkan panjang: "))
#l = int(input("masukkan lebar: "))
#t = int(input("masukkan tinggi: "))
#volume = int(input(p * l * t * 3 / 4))
#sehari = 2
#sebulan = 30
#algoritma
#air = volume * sehari * sebulan
#print("volume air yang butuhkan dalam sebulan adalah " , int(air))




# print("NAMA: NELLIS NERI AURUM TECTONA")
# print("NIM: A11.2020.12668")
# print("KELAS: 4210")
# print("\n")

# print("contoh rekursif bagi")
# def pembagian(a,b):
    # i = a
    # result = 0
    # while i > 0:
        # i = i - b
        # result = result + 1 #result++
    # return result
# print("1. hasil dari 45 dibagi 9 adalah: ", (pembagian(45,9)))
# '''
    # i = 45
    # while i > 0:
        # True
        # i = 45 - 9 = 36, True
        # result = 0 + 1 = 1

        # i = 36 - 9 = 27, True
        # result = 1 + 1 = 2

        # i = 27 - 9 = 18, True
        # result = 2 + 1 = 3

        # i = 18 - 9 = 9, True
        # result = 3 + 1 = 4

        # i = 9 - 9 = 0, False
        # result = 4 + 1 = 5
    # return result // return 5
# '''
# def pembagiankedua(a,b):
    # i = a
    # result = 0
    # while i > 0:
        # i = i - b
        # result = result + 1 #result++
    # return result
# print("2. hasil dari 49 dibagi 7 adalah: ", (pembagiankedua(49,7)))
# '''
    # i = 49
    # while i > 0:
        # True
        # i = 49 - 7 = 42, True
        # result = 0 + 1 = 1

        # i = 42 - 7 = 35, True
        # result = 1 + 1 = 2

        # i = 35 - 7 = 28, True
        # result = 2 + 1 = 3

        # i = 28 - 7= 21, True
        # result = 3 + 1 = 4

        # i = 21 - 7 = 14, True
        # result = 4 + 1 = 5

        # i = 14 - 7 = 7, True
        # result = 5 + 1 = 6

        # i = 7 - 7 = 0, False
        # result = 6 + 1 = 7
    # return result // return 7
# '''
print("\n")
print("NAMA: NELLIS NERIA AURUM TECTONA")
print("NIM: A11.2020.12668")
print("KELAS: 4210")
print("\n")

#Kamuspertama = {1: 'Karina', 2: 'Giselle', 3: 'Winter', 4: 'Ningning'}
#Kamuskedua = {1: 2000, 2: 2000, 3: 2001, 4: 2002}
#Kamusketiga = {'nama girl group': 'AESPA', 'anggota': '4'}

#print("1. CONTOH MENGHAPUS DATA")
#print(Kamuspertama, "setelah dihapus menjadi ")
#del Kamuspertama[1]
#print(Kamuspertama)
#print("2. CONTOH MEMPERBAHARUI DATA")
#print(Kamuskedua, "setelah dirubah menjadi ") 
#Kamuskedua[4] = 'Maknae'
#print(Kamuskedua)
#print("3. CONTOH MENGHAPUS SELURUH DATA")
#print(Kamusketiga, "setelah data seluruhnya dihapus maka ")
#Kamusketiga.clear()
#print(Kamusketiga)
#listpertama = ['NCT', 'AESPA', 'EXO']
#listkedua = ['Leon', 'Louis', 'Bella'], ['Bongshik', 'Seol', 'Nal', 'Daegal']
#listketiga = [4, 5, 9, 11, 23] 

#print("1. CONTOH MENAMBAHKAN DATA")
#print(listpertama, "setelah ditambahkan menjadi ") , listpertama.append('Red Velvet')
#print(listpertama)
#print("2. CONTOH MENGHAPUS DATA")
#print(listketiga, "setelah dihapus menjadi ")
#del(listketiga[3])
#print(listketiga)
#print("3. CONTOH MENCARI DATA")
#anabul_dreamies = ['Bongshik', 'Seol', 'Nal', 'Daegal'] in listkedua
#print(listkedua, "apakah ada hewan peliharaan NCT DREAM? jawabannya adalah ", anabul_dreamies)


#print("Koleksi Novelku")
#print("\n")

#novel1 = {
   # 'judul' : 'tujuh hari untuk keshia',
  #  'penerbit' : 'elex komputindo',
 #   'harga' : 70000
#}
#novel2 = {
 #   'judul' : 'dream launch project',
 #   'penerbit' : 'bukune',
 #   'harga' : 99000
#}
#novel3 = {
#    'judul' : 'laut bercerita',
#    'penerbit' : 'gramedia',
#    'harga' : 75000
#}
#novel4 = {
  #  'judul' : 'noir',
 #   'penerbit' : 'loveable',
 #   'harga' : 85000
#}#
#novel5 = {
#    'judul' : 'say hi!',
#    'penerbit' : 'elex komputindo',
#    'harga' : 92000
#}
#print("PENERAPAN DALAM NESTED DICTIONARY")
#print("\n")
#sampul_hitam = {
 #   'kiri' : novel1,
 #   'tengah' : novel4,
 #   'kanan' : novel5
#}
#sampul_biru = {
  #  'kiri' : novel2,
 #   'kanan' : novel3
#}
#print("koleksi novelku di rak buku pertama adalah: ")
#print("1. ", sampul_hitam['kiri'])
#print("2. ",sampul_hitam['tengah'])
#print("3. ",sampul_hitam['kanan'])
#print("koleksi novelku di rak buku kedua adalah: ")
#print("1. ", sampul_biru['kiri'])
#print("2. ",sampul_biru['kanan'])

#class :

#def __init__(self, perpustakaan, username, draf, notifikasi):
#self.perpustakaan = perpustakaan
#         self.draf = draf
#         self.username = username
#         self.notifikasi = notifikasi

#     def account(self):
#         print(f"\n username: {self.username} \n perpustakaan: {self.perpustakaan} \n notifikasi: {self.notifikasi} \n draf: {self.draf} ")

#     def notification(self, umpan_berita, papan_pengumuman):
#         self.umpan = umpan_berita
#         self.papan = papan_pengumuman
#         print(f"Tenderlova mengunggah cerita baru: ", self.umpan)
#         print(f"papan pengumuman: ", self.papan)

#     def post(self, upfoto, ebook):
#         self.profil = upfoto
#         self.pencarian = ebook
#         print(f"foto profil telah berhasil diubah menjadi ", self.profil)
#         print(f"cari novel atau penulis ", self.pencarian)

# nellis = Wattpad("Oceanite, Arah Asa, A+", "Kichiku_", "Draf kosong", "Terdapat 1 Notifikasi")
# nellis.account()
# nellis.notification("Crayola's Tale", "\n Comeback with chapter 10, please go read it! \n -Dirorimochi <3")
# nellis.post("Jungwoo NCT", "Lutte")
# print("\n")

# class Node(object):
#     def __init__(self, data=None, next_node=None):
#         self.data = data #data dari node
#         self.next_node = next_node #poiner dari node
#     #menentukan next node
#     def set_next(self, new_next):
#         self.next_node = new_next
#     #mengambil data node
#     def get_data(self):
#         return self.data
#     #mengambil next node
#     def get_next(self):
#         return self.next_node
# class LinkedList(object):
#     def __init__(self, head=None, tail=None):
#         self.head = head
#         self.tail = tail
#     def selanjutnya(self, data):
#         #objek baru dari class node
#         new_node = Node(data)
#         #jika head masih kosong
#         if (self.head is None):
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next_node = new_node
#             self.tail = new_node
#     def ShowData(self):
#         #os.system(clear)
#             print("\n Menampilkan list kegiatanku sehari hari: ")
#             current_node = self.head
#             if (self.head is None):
#                 print("Data belum diisi!")
#             else:
#                 while current_node is not None:
#                     print(current_node.data, end=" ")
#                     print(" ==> ", end=" ")
#                     current_node = current_node.next_node
#     def main(self):
#           self.selanjutnya("Bangun tidur")
#           self.selanjutnya("Sholat")
#           self.selanjutnya("Mandi")
#           self.selanjutnya("Makan")
#           self.selanjutnya("Kuliah online")
#           self.selanjutnya("Tidur")
#           self.ShowData()
#           print()
# if __name__ == "__main__":
#     l = LinkedList()
#     l.main()
# print("\n")

# def sum (x):
#     #jika x adalah 8
#     res = 0 #T = 1, karena assignment
#     for i in range (x+1): #T=1
#         #x + 1
#         #8 + 1 = 9
#         # for i in range (9), looping 0 sampai 8 atau 9 kali looping
#             #i = 0
#                 #res = 0 + 1
#             #i = 1
#                 #res = 1 + 1
#             #i = 2
#                 #res = 2 + 1
#             #i = 3
#                 #res = 3 + 1
#             #i = 4
#                 #res = 4 + 1
#             #i = 5
#                 #res = 5 + 1
#             #i = 6
#                 #res = 6 + 1
#             #i = 7
#                 #res = 7 + 1
#             #i = 8
#                 #res = 8 + 1
#                 #res = 9
#         res += 1
#     return res #return 9
# print(sum(8))
#print("1. faktorial")
#def faktorial(a):
    #if a == 1:
        #return (a)
    #else:
        #return (a * faktorial(a - 1))
#bil = int(input("masukkan angka: "))
#print("%d! = %d" % (bil, faktorial(bil)))
#print("\n")
#print("2. fungsi pangkat")
#def pangkat(x,y):
    #if y == 0:
        #return 1
    #else:
        #return x * pangkat(x,y-1)
#x = int(input("masukkan angka x: "))
#y = int(input("masukkan angka y: "))
#print("%d dipangkatkan %d = %d" % (x,y, pangkat(x,y)))
#print("\n")
#print("3. memanggil dirinya sendiri")
#def mengulang():
 #   print("teknik informatika udinus")
#print(mengulang)
def get_data(self):
        return self.data
def get_next(self):
        return self.next_node

class LinkedList(object):
    def _init_(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def tambahBelakang(self, data):
        new_node = None,(data)
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
            
        else :
            self.tail.next_node = new_node
            self.tail = new_node
    def showData(self):
        print("\n List Tampilan daftar Belanja  : \n")
        current_node= self.head
        if (self.head is None):
            print("Data Masih Kosong")
        else:
            while current_node is not None:
                print(current_node.data, end="")
                print("=>", end="")
                current_node = current_node.next_node

    def main(self):
        self.tambahBelakang('Beras 5kg')
        self.tambahBelakang('Bawang Merah 1/2kg')
        self.tambahBelakang('Kopi Bubuk 1kg')
        self.tambahBelakang('Lombok 1,5kg')
        self.tambahBelakang('Gula 1kg')
        self.showData()
        print()

if __name__ == "_main_":
    l = LinkedList()
    l.main()
print(LinkedList(object))