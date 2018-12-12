import os,django
import pandas as pd
from orm.models import Mahasiswa,Jaringan,Rpl,Multimedia,Tesdasar
import math
import operator

mhs = Mahasiswa.objects.all()
mul = Multimedia.objects.all()
rpl = Rpl.objects.all()
jar = Jaringan.objects.all()
tes = Tesdasar.objects.all()

def ListMultimedia(mul):
    if len(mul)>0:
        cols = ['Interaksi Manusia Dan Komputer','Artificial Intelligent','Grafika Komputer',
                'Prak.Grafika Komputer']
        
        kel ={
            cols[0] : [str(a.IMK) for a in mul],
            cols[1] : [str(a.ArtificialIntelligent) for a in mul],
            cols[2] : [str(a.GrafikaKomputer) for a in mul],
            cols[3] : [str(a.PrakGrafikaKomputer) for a in mul],            
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]
    
def ListJaringan(jar):
    if len(jar)>0:
        cols = ['Pengantar Sistem Digital','Organisasi Dan Arsitektur Komputer','Sistem Operasi',
                'Prak.Sistem Operasi','Komunikasi Data Dan Pengantar Jaringan','Jaringan Komputer',
                'Prak.Jaringan Komputer']
        
        kel ={
            cols[0] : [str(a.Psd) for a in jar],
            cols[1] : [str(a.Orkom) for a in jar],
            cols[2] : [str(a.SistemOperasi) for a in jar],
            cols[3] : [str(a.PrakSistemOperasi) for a in jar],
            cols[4] : [str(a.Komdat) for a in jar],
            cols[5] : [str(a.JaringanKomputer) for a in jar],
            cols[6] : [str(a.PrakJaringanKomputer) for a in jar],
            
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]    
        
def ListRpl(rpl):
    if len(rpl)>0:
        cols = ['Algoritma Dan Pemrograman','Prak.Algoritma Dan Pemrograman','Pengantar Teknologi Informasi',
                'Struktur Data','Sistem Basis Data','Prak.Sistem Basis Data','Pemrograman I','Prak.Pemrograman I',
                'Sistem Informasi','Pemrograman II','Prak.Pemrograman II','Analisa Dan Desain Perangkat Lunak']
        
        kel ={            
            cols[0] : [str(a.AlgoritmaDanPemrograman) for a in rpl],
            cols[1] : [str(a.PrakAlgoritmaDanPemrograman) for a in rpl],
            cols[2] : [str(a.PTI) for a in rpl],
            cols[3] : [str(a.StrukturData) for a in rpl],
            cols[4] : [str(a.SistemBasisData) for a in rpl],
            cols[5] : [str(a.PrakSistemBasisData) for a in rpl],
            cols[6] : [str(a.Pemrograman1) for a in rpl],
            cols[7] : [str(a.PrakPemrograman1) for a in rpl],
            cols[8] : [str(a.SistemInformasi) for a in rpl],
            cols[9] : [str(a.Pemrograman2) for a in rpl],
            cols[10] : [str(a.PrakPemrograman2) for a in rpl],
            cols[11] : [str(a.Adpl) for a in rpl],
        }        
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]
    
def ListTest(tes):
    if len(tes)>0:
        cols = ['Multimedia','Jaringan','Rpl']
        
        kel ={
            cols[0] : [str(a.NilaiMultimedia) for a in tes],
            cols[1] : [str(a.NilaiJaringan) for a in tes],
            cols[2] : [str(a.NilaiRPL) for a in tes],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]

def Mhsis(mhs):
    if len(mhs)>0:
        cols = ['nim','nama']
        
        kel ={
            cols[0] : [str(a.nim) for a in mhs],
            cols[1] : [str(a.nama) for a in mhs],
        }
        df = pd.DataFrame(data=kel)
        return df
    else:
        return[]

mu = pd.DataFrame(data = ListTest(tes).Multimedia)
ja = pd.DataFrame(data = ListTest(tes).Jaringan)
rp = pd.DataFrame(data = ListTest(tes).Rpl)

def Hitung(a,b,c):
    tamp = []
    for x in range(len(mhs)):
        tampung = list()
        for i in a:
            if i is 'A':        
                tampung.append(6)
            elif i == 'B+':        
                tampung.append(5)
            elif i is 'B':        
                tampung.append(4)
            elif i == 'C+':        
                tampung.append(3)
            elif i is 'C':        
                tampung.append(2)
            elif i is 'D':
                tampung.append(1)
            else:
                continue            
            rata2 = sum(tampung)/len(tampung)
            tmp = [rata2, b]
            dframe = pd.DataFrame(data=tmp,columns=[c])
    tamp.append(dframe)
    return tamp

def Multimedia():
    tampung = []
    for i in range(len(mhs)):
        x = Hitung(ListMultimedia(mul).loc[i],mu.loc[i][0],'Multimedia')
        tampung.append(x)
    return tampung

def Jaringan():
    tampung = []
    for i in range(len(mhs)):
        x = Hitung(ListJaringan(jar).loc[i],ja.loc[i][0],'Jaringan')
        tampung.append(x)
    return tampung
def Rpls():
    tampung = []
    for i in range(len(mhs)):
        x = Hitung(ListRpl(rpl).loc[i],rp.loc[i][0],'Rpl')
        tampung.append(x)
    return tampung

tampung1 = []
for i in range(len(mhs)):
    gabungan = pd.concat([Multimedia()[i][0],Jaringan()[i][0],Rpls()[i][0]],axis=1)
    tampung1.append(gabungan)        

def Total():
    t = []
    for i in range(len(mhs)):
        gabungan = pd.concat([Multimedia()[i][0],Jaringan()[i][0],Rpls()[i][0]],axis=1)
        t.append(gabungan)
    return t

p1 = tampung1[0].shape[1]
p2 = tampung1[0].shape[1]
p3 = len(tampung1[0].iloc[:,0])
arr0 = []
hasil0 = []
for y in range(len(mhs)):
    arr = []
    hasil = []
    for i in range(p1):
        arr1 = []
        hasil1 = []
        for j in range(p2):
            arr2 = []
            hasil2= []
            for k in range(p3):
                z = float(tampung1[y].iloc[:,i][k])-float(tampung1[y].iloc[:,j][k])
                m = 0            
                if (z <= 0):
                    m = 0
                else:
                    m = 1
                hasil2.append(z)
                arr2.append(m)
            arr1.append(arr2)
            hasil1.append(hasil2)
        arr.append(arr1)
        hasil.append(hasil1)
    arr0.append(arr)
    hasil0.append(hasil)

hasil1 = pd.DataFrame(arr0)
hasil2 = pd.DataFrame(hasil0)

def Tindex():
    akhir = []
    for v in range(len(mhs)):
        akhir1 = []
        for i in range(len(tampung1[v].iloc[0])):
            akhir2 = []
            for j in range(len(hasil1[i].loc[v])):
                bla = sum(hasil1.loc[v].loc[i][j])*(1/len(hasil1.loc[v].iloc[i][j]))
                akhir2.append(bla)
            akhir1.append(akhir2)
        akhir.append(akhir1)
    return akhir

promethee1 = []
for m in range(len(mhs)):
    tmp1 = []
    for i in range(len(Tindex()[m])):
        tmp2 = []
        for j in range(len(Tindex()[m])):
            tmp2.append(Tindex()[m][i][j])
        tmp1.append(tmp2)
    prometh = pd.DataFrame(data=tmp1, columns = ['A','B','C'], index = ['A', 'B', 'C'])
    promethee1.append(prometh)

def Lflow():
    lf = []
    for k in range(len(promethee1)):
        lf1 = []
        for i in range(len(promethee1[k])):
            jwb = (1/(len(promethee1[k]) - 1)) * sum(promethee1[k].iloc[i])
            lf1.append(jwb)        
        leaving = pd.DataFrame(data=lf1,columns=['Leaaving Flow'])
        lf.append(leaving)
    return lf

def Eflow():
    ef = []
    for k in range(len(promethee1)):
        ef1 = []
        for i in range(len(promethee1[k])):
            jwb = (1/(len(promethee1[k])-1)) * sum(promethee1[k].iloc[:,i])
            ef1.append(jwb)        
        entring = pd.DataFrame(data=ef1,columns=['Entring Flow'])
        ef.append(entring)
    return ef

def Nflow():
    nf = []
    for k in range(len(promethee1)):
        nf1 = []
        for i in range(len(promethee1[k])):
            jwb = Lflow()[k].iloc[i][0] - Eflow()[k].iloc[i][0]
            nf1.append(jwb)        
        net = pd.DataFrame(data=nf1,columns=['Net Flow'])
        nf.append(net)
    return nf

def Nilai(mhs):
    if len(mhs)>0:
        nf = []
        gh = []
        rek = []
        for k in range(len(promethee1)):
            nf1 = []
            for i in range(len(promethee1[k])):
                jwb = Lflow()[k].iloc[i][0] - Eflow()[k].iloc[i][0]
                nf1.append(jwb)
            if(nf1.index(max(nf1)) == 0):
                rek.append('Jaringan')
            elif(nf1.index(max(nf1)) == 1):
                rek.append('Multimedia')
            elif(nf1.index(max(nf1)) == 2):
                rek.append('RPL')
            else:
                rek.append('Tidak ada')
            gh.append(max(nf1))
            net = pd.DataFrame(data=gh,columns=['Net Flow'])
            rekom = pd.DataFrame(data=rek,columns=['Rekomendasi'])
            a=Mhsis(mhs).index.get_values()
            b=pd.DataFrame(a,columns=['index'])
            hasil=pd.concat([Mhsis(mhs),rekom,b],axis=1)
        return hasil
    else:
        pass

alt = pd.DataFrame(['Multimedia','Jaringan','Rpl'],columns=['Rekomendasi'])
def Gabung():
    gaboeng = []
    for x in range(len(mhs)):
        z = pd.concat([Lflow()[x],Eflow()[x],Nflow()[x],alt],axis=1)
        gaboeng.append(z)
    return gaboeng

for k,v in enumerate(Gabung()):
    Gabung()[k].index.name=str(mhs[k])
for k,v in enumerate(tampung1):
    tampung1[k].index.name=str(mhs[k])

def Perangkingan():
    rangking = []
    for x in range(len(Gabung())):
        rank = Gabung()[x].sort_values(by='Net Flow', ascending=False)
        rangking.append(rank)
        
    return rangking

def Penggabungan():
    gab = []
    for x in range(len(mhs)):
        z = pd.concat([Lflow()[x],Eflow()[x],Nflow()[x],alt],axis=1)
        gab.append(z)

    return gab

def Dmultimedia():
    multi = []
    for k in range(len(promethee1)):
        multi.append(tampung1[k].loc[0][0])
    e = pd.DataFrame(data=multi,columns=['Multimedia'])
    return e

def Djaringan():
    jar = []
    for k in range(len(promethee1)):
        jar.append(tampung1[k].loc[0][1])
    e = pd.DataFrame(data=jar,columns=['Jaringan'])    
    return e

def Drpl():
    rpl = []
    for k in range(len(promethee1)):
        rpl.append(tampung1[k].loc[0][2])
    e = pd.DataFrame(data=rpl,columns=['RPL'])    
    return e

def Akademik():
    a = pd.concat([Mhsis(mhs),Dmultimedia(),Djaringan(),Drpl()],axis=1)
    return a    

def Tmultimedia():
    multi = []
    for k in range(len(promethee1)):
        multi.append(tampung1[k].loc[1][0])
    e = pd.DataFrame(data=multi,columns=['Multimedia'])
    return e

def Tjaringan():
    jar = []
    for k in range(len(promethee1)):
        jar.append(tampung1[k].loc[1][1])
    e = pd.DataFrame(data=jar,columns=['Jaringan'])    
    return e

def Trpl():
    rpl = []
    for k in range(len(promethee1)):
        rpl.append(tampung1[k].loc[1][2])
    e = pd.DataFrame(data=rpl,columns=['RPL'])    
    return e
def TesDasar():        
    a = pd.concat([Mhsis(mhs),Tmultimedia(),Tjaringan(),Trpl()],axis=1)
    return a