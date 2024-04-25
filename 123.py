import time
meme_dict = {    
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL":"bir şakaya karşılık cevap",
            "SHEESH":"onaylamamak",
            "CREEPY" :"korkunç",
            "AGGRO" : "agresifleşmek/sinirlenmek"
            }
print("1.CRINGE,2.LOL,3.ROFL,4.SHEESH,5.CREEPY,6.AGGRO")
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    time.sleep(1/3)
    print(meme_dict[word])
else:
    print("eror verdi canım")
