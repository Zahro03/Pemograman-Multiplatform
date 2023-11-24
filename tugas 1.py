def konversi_suhu(nilai, satuan):
    fahrenheit = (nilai* 9/5) + 32
    celsius = (satuan - 32) *  5/9
    print("Hasil konveri celcius ke fahrenheit: ", celsius)
    print("Hasil konveri fahrenheit ke celcius: ", fahrenheit)

suhu = float (input("masukan nilai celcius: "))
cuaca = float (input("masukan nilai fahreinheit: "))

konversi_suhu(suhu,cuaca)

