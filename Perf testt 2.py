import multitreading
import time
ajat = []
aika = 0
kerrat = 0
tkerta = 0
kerta = 7500000

while kerrat <= 9:
    laskuri = 0
    kerrat += 1
    a = []
     

    start = time.time()
    
    while laskuri <= (kerta):
        a.append(laskuri)
        laskuri += 1
        end = time.time()

    kerta += 3500000        
    print ("0 -" ,kerta, "Lukua laskettu")
    tkerta += 1
    ajat.append(end - start)
    aika = (end - start)
    print (tkerta, "Krt suoritettu, aikaa kului", "%.3f" % aika , "Sec")
    print ("")

tulos = sum(ajat)    
print ("Testiin kulunut aika","%.3f" % tulos, "Sec")
ttulos = 250 - tulos
pisteet = ttulos * 3
print("Pisteesi","%.3f" % pisteet, "pt")
        
    
        
        
    