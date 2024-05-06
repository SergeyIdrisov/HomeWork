#Алгоритм КМП
#Эффиктивный подсчёт суппрефикса
prava_naprava_ne_davai_na_levo = input()
def perefecisitaca_funikcia(stroka_lutaya):
    dlina_pipiska = len(stroka_lutaya)
    otvet_kotoryi_nado_vyvesty = [0 for i in range(dlina_pipiska)]
    for i in range(1,dlina_pipiska):
        luti_supremum = otvet_kotoryi_nado_vyvesty[i-1]
        while luti_supremum > 0 and stroka_lutaya[luti_supremum] != stroka_lutaya[i]:
            luti_supremum = otvet_kotoryi_nado_vyvesty[luti_supremum-1]
        if stroka_lutaya[luti_supremum]==stroka_lutaya[i]:
            luti_supremum+=1
        otvet_kotoryi_nado_vyvesty[i] = luti_supremum
    return otvet_kotoryi_nado_vyvesty
print(perefecisitaca_funikcia(prava_naprava_ne_davai_na_levo))
def lutay_z_funiciler(stroka_lutaya_no_uje_2):
    spisok_sosisok = perefecisitaca_funikcia(stroka_lutaya_no_uje_2)
    i = 0
    a = 0
    while i == 0:
        a+=1
        i = spisok_sosisok[a]
    atvet_na_vyvod = []
    b=0
    for i in range(len(spisok_sosisok)):
        if not (i+1)%a:
            atvet_na_vyvod.append(spisok_sosisok[b*a-1])
            b-=1
        else:
            atvet_na_vyvod.append(0)
    atvet_na_vyvod.insert(0,atvet_na_vyvod.pop(-1))
    return atvet_na_vyvod
print(lutay_z_funiciler(prava_naprava_ne_davai_na_levo))