from random import choice
def baru(card_element, new_card):
    card_element=[1,2,3,4,5,6,7,8,9,10,10,10,10]
    new_card=choice(card_element)
    return new_card
def truf(new_card):
    new_card=int(input("Pilih 11 atau 1?: "))
    if (new_card==11 or new_card==1):
        print ("Anda memilih: "+str(new_card))
    elif (new_card!=11 or new_card!=1):
        while (new_card!=11 or new_card!=1):
            print("Cuman 2 angka itu aba")
            new_card=int(input("Mau berapa?11/1: "))
            if (new_card==11 or new_card==1):
                print ("Anda memilih: "+str(new_card))
                break
    return new_card
poin_player=0
poin_kom=0
print("===========Welcome to the game (24)==========")
print("==========Dapatkan kartu mendekati 21========")
main="y"
while(main=="y" or main=="Y"):
    i=0
    card_element=[1,2,3,4,5,6,7,8,9,10,10,10,10]
    new_card=choice(card_element)
    card_player=[
        baru(card_element, new_card), 
        baru(card_element, new_card)]
    card3= choice(card_element)
    card4= choice(card_element)

    print("#########################################")
    print("Poin Anda: "+str(poin_player))
    print("Poin Komputer: "+str(poin_kom))
    print("_____________________________")
    print("Kartu yang anda dapat adalah "+str(card_player))
    print("Kartu yang didapat komputer: "+str(card3)+" & ?")
    if (card_player[0]==1):
        card_player[0]=truf(new_card=1)
    if (card_player[1]==1):
        card_player[1]=truf(new_card=1)
    if (card3==1):
        if (card4==10):
            card3=11
        elif (card4<=9):
            card3=1
            print("--------------------------")
            print("Komputer menambah kartu")
            print("Kartu komputer menjadi "+str(card3)+" & ? & ?")
            print("--------------------------")
    if (card4==1):
        if (card3==10):
            card4=11
        elif (card3<=9):
            card4=truf(new_card=1)
            print("--------------------------")
            print("Komputer menambah kartu")
            print("Kartu komputer menjadi "+str(card3)+" & ? & ?")
            print("--------------------------")
    jum_cplayer=sum(card_player)
    card_computer=[card3, card4]
    jum_ckom=sum(card_computer)
    if (jum_ckom<=14):
        while (jum_ckom<=14):
            card_computer.append(baru(card_element=0, new_card=0))
            jum_ckom=sum(card_computer)
            print("--------------------------")
            print("Komputer menambah kartu")
            print("Kartu komputer menjadi "+str(card3)+" & ? & ?")
            print("--------------------------")
            if jum_ckom>14:
                break
    print("Kartu anda:  "+str(card_player))
    print("Jumlah kartu anda sekarang: "+ str(jum_cplayer))
    again=input("Ingin menambah kartu?(y/t): ")
    while (again=="y"):
        card_player.append(baru(card_element, new_card))
        jum_cplayer=sum(card_player)
        if jum_cplayer>21:
            break
        print("Kartu anda:"+str(card_player))
        again=input("Ingin menambah kartu?(y/t): ")

    print("======[Hasil]======")
    print("Kartu anda : "+str(card_player))
    print("Kartu komputer : "+str(card_computer))
    print("Total kartu anda : "+str(jum_cplayer))
    print("Total kartu komputer : "+str(jum_ckom))
    if (jum_cplayer==jum_ckom or (jum_ckom>21 and jum_cplayer>21)):
        print("SERI. Sugoi-desu")
    elif (jum_cplayer>21):
        print("Anda kalah! Noob. Tetap semangat")
        poin_kom+=1
    elif (jum_ckom>21):
        print ("Anda menang! Selamat!")
        poin_player+=1
    else:
        if(jum_cplayer==21):
            print("BLACK JACK. Hoki 1 bulan t pake selamat")
            poin_player+=1
        elif (jum_cplayer>jum_ckom):
            print("Anda menang! Selamat!")
            poin_player+=1
        else:
            print("Anda kalah! YOWAI MOO")
            poin_kom+=1
    print("=====[PEROLEHAN POIN]=====")
    print("Poin Anda: "+str(poin_player))
    print("Poin Komputer: "+str(poin_kom))
    main=input("Main lagi?(y/t): ")
    if(main=="y" or main=="Y"):
        main="y"
    else:
        if (poin_player>poin_kom):
            print("Anda menang. Selamat... Anda bisa beli rumah")
            n=input("Enter to close...")
        else:
            print("Anda kalah. Tetap semangat")
            n=input("Enter to close...")
        break
