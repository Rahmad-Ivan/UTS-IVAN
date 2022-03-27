
import sys
#RAHMAD IVAN ACHMAD
gj_pokok=int(0)
gj_bersih=int(0)
gj_kotor=int(0)
ptgn=float(0)
kd=str("")
nm=str("")
gl=str("")
stts=int(0)
jml_anak=0
tunjangan_pasangan=0
tunjangan_anak=0
status_menikah=""

print('=====================================================\n')
print('Program penentuan gaji pokok dan gaji bersih karyawan\n')
print('=====================================================\n')

kd = str(raw_input("Masukkan kode karyawan : "))
nm = str(raw_input("Masukkan nama karyawan : "))
gl = str(raw_input("Masukkan golongan (A,B,C,D): "))
stts = int(input("Masukkan status (1: menikah, 2: belum) : "))

if stts == 1:
    jml_anak = int(input("Masukkan jumlah anak : "))
    
print('\n')

if gl not in ["A", "B", "C", "D"]:
    print("Golongan yang anda inputkan tidak sesuai")
    sys.exit()
else:
    if gl == "A":
        gj_pokok = 10000000
        ptgn = 2.5
    elif gl == "B":
        gj_pokok = 8500000
        ptgn = 2.0
    elif gl == "C":
        gj_pokok = 7000000
        ptgn = 1.5
    elif gl == "D":
        gj_pokok = 5500000
        ptgn = 1.0
        
if stts not in [1, 2]:
    print("Status yang anda inputkan tidak sesuai")
    sys.exit()

if stts == 1:
    tunjangan_pasangan = gj_pokok*10/100
    status_menikah = 'Menikah'
    if jml_anak != 0:
        tunjangan_anak = gj_pokok*5/100
    else:
        tunjangan_anak = 0
else:
