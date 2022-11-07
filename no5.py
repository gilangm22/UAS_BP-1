def jualan():
    a = "capucino"
    b = "teh"
    print ("Pilihan")
    print ("1.", a)
    print ("2.", b)
    print ("3. Exit")

def capucino():
    cap = "memilih capucino"
    print(cap)
    capucino = int(input("masukkan harga : "))
    ppn = capucino/10
    total = capucino+ppn
    print("Harga Yang Di Bayar : " + str(total))

def teh():
    te = "memilih TEH"
    print(te)
    teh = int(input("masukkan harga : "))
    ppn = teh/10
    total = teh+ppn
    print("Harga Yang Di Bayar : " + str(total))

def welcome():
    nim = 20210801098
    nama = "Muhamad Fikri Ruli Husaini"
    print ("NIM : ", nim)
    print ("NAMA : ", nama)

while True:
    welcome()
    jualan()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    elif pil == 3:
        break
    else:
        print ("pilihan salah")
