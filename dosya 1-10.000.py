for i in range(1,10000,1):
    dosya=open("sayilar.txt","a")
    veri=str(i)+"\n"
    dosya.write(veri)
    dosya.close()
    print(i)

