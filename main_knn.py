def fuzzi(n_emosi, n_provokasi):
    bEmosi_0 = 36
    bEmosi_1 = 40
    bEmosi_2 = 63
    bEmosi_3 = 64

    bProv_1 = 43
    bProv_2 = 44
    bProv_3 = 76
    bProv_4 = 77

    #PENENTUAN NILAI EMOSI
    #EMOSI SANGAT RENDAH
    if (n_emosi <= 36):
        s_rendah = 1
    elif (n_emosi > bEmosi_0) & (n_emosi < bEmosi_1):
        s_rendah = (bEmosi_1-n_emosi)/(bEmosi_1-bEmosi_0)
    else:
        s_rendah = 0

    #EMOSI RENDAH
    if (n_emosi < bEmosi_1) & (n_emosi > bEmosi_0):
        rendah = (n_emosi-bEmosi_0)/(bEmosi_1-bEmosi_0)
    elif (n_emosi >= bEmosi_1) & (n_emosi <= bEmosi_2):
        rendah = 1
    elif (n_emosi > bEmosi_2) & (n_emosi < bEmosi_3):
        rendah = (bEmosi_3 - n_emosi) / (bEmosi_3-bEmosi_2)
    else:
        rendah = 0

    #EMOSI SEDANG
    # if (n_emosi > bEmosi_2) & (n_emosi < bEmosi_3):
    #     sedang = (n_emosi-bEmosi_2)/(bEmosi_3-bEmosi_2)
    # elif (n_emosi >= bEmosi_3) & (n_emosi <= bEmosi_4):
    #     sedang = 1
    # elif (n_emosi > bEmosi_4) & (n_emosi < bEmosi_5):
    #     sedang = (bEmosi_5-n_emosi)/(bEmosi_5-bEmosi_4)
    # else:
    #     sedang = 0

    #EMOSI TINGGI
    if (n_emosi >= bEmosi_3):
        tinggi = 1
    elif (n_emosi > bEmosi_2) & (n_emosi < bEmosi_3):
        tinggi = (n_emosi-bEmosi_2)/(bEmosi_3-bEmosi_2)
    else:
        tinggi = 0

    ##########################################################
    #PENENTUAN NILAI PROVOKASI
    #PROVOKASI LOW
    if n_provokasi <= bProv_1:
        low = 1
    elif (n_provokasi > bProv_1) & (n_provokasi < bProv_2):
        low = (bProv_2-n_provokasi)/(bProv_2-bProv_1)
    else:
        low = 0

    #PROVOKASI MEDIUM
    if (n_provokasi > bProv_1) & (n_provokasi < bProv_2):
        medium = (n_provokasi-bProv_1)/(bProv_2-bProv_1)
    elif (n_provokasi >= bProv_2) & (n_provokasi <= bProv_3):
        medium = 1
    elif (n_provokasi > bProv_3) & (n_provokasi < bProv_4):
        medium = (bProv_4-n_provokasi)/(bProv_4-bProv_3)
    else:
        medium = 0

    #PROVOKASI HIGH
    if n_provokasi <= bProv_3:
        high = 0
    elif (n_provokasi > bProv_3) & (n_provokasi < bProv_4):
        high = (n_provokasi-bProv_3)/(bProv_4-bProv_3)
    else:
        high = 1


    #FUZZY RULE
    if s_rendah <= low:
        no_0 = s_rendah
    else:
        no_0 = low

    if s_rendah <= medium:
        no_1 = s_rendah
    else:
        no_1 = medium

    if s_rendah <= high:
        ya_1 = s_rendah
    else:
        ya_1 = high

    if rendah <= low: #rendah and low
        no_2 = rendah
    else:
        no_2 = low

    if rendah <= medium: #rendah and medium
        no_3 = rendah
    else:
        no_3 = medium

    if rendah <= high: #rendah and high
        ya_0 = rendah
    else:
        ya_0 = high

    if tinggi <= low: #tinggi and low
        no_4 = tinggi
    else:
        no_4 = low

    if tinggi <= medium: #tinggi and medium
        ya_2 = tinggi
    else:
        ya_2 = medium

    if tinggi <= high: #tinggi and high
        ya_3 = tinggi
    else:
        ya_3 = high

    #PENGAMBILAN NILAI NO
    no_ = [no_0, no_1, no_2, no_3, no_4]

    no_fix = 0
    i = 0
    while (i < 5): #mengambil nilai no terbesar dengan perbandingan
        if no_fix < no_[i]:
            no_fix = no_[i]
        else:
            no_fix = no_fix
        i += 1

    # PENGAMBILAN NILAI YA
    ya_ = [ya_0, ya_1, ya_2, ya_3]

    ya_fix = 0
    j = 0
    while (j < 4): #mengambil nilai yes terbesar dengan perbandingan
        if ya_fix < ya_[j]:
            ya_fix = ya_[j]
        else:
            ya_fix = ya_fix
        j += 1

    if (no_fix == 0) & (ya_fix == 0): #ada kondisi ini agar pembaginya tidak nol karena error jika nol
        y = 0
    else:
        y = (no_fix *2 + ya_fix *3) / (no_fix + ya_fix) #persamaan sugeno yang digunakan
    print('NILAI Y*  =',y)

    if (y > 2 ):
        print ("HOAX        = YA")
    else:
        print ("HOAX        = NO")

print "====D A T A T R A I N===="
fuzzi(97, 74) #YA
fuzzi(36, 85) #YA
fuzzi(63, 43) #TIDAK
fuzzi(82, 90) #YA
fuzzi(71, 25) #TIDAK
fuzzi(79, 81) #YA
fuzzi(55, 62) #TIDAK
fuzzi(57, 45) #TIDAK
fuzzi(40, 65) #TIDAK
fuzzi(57, 45) #TIDAK
print "====D A T A T R A I N===="
fuzzi(77, 70) #YA
fuzzi(68, 75) #YA
fuzzi(60, 70) #TIDAK
fuzzi(82, 90) #YA
fuzzi(40, 85) #TIDAK
fuzzi(80, 68) #YA
fuzzi(60, 72) #TIDAK
fuzzi(50, 95) #YA
fuzzi(100, 18) #TIDAK
fuzzi(11, 99) #YA
print "====D A T A T E S T===="
fuzzi(58, 63)
fuzzi(68, 70)
fuzzi(64, 66)
fuzzi(57, 77)
fuzzi(77, 55)
fuzzi(98, 64)
fuzzi(91, 59)
fuzzi(50, 95)
fuzzi(95, 55)
fuzzi(27, 79)
