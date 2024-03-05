import turtle

# Shape'yi hareket ettiren ve döndüren fonksiyon
def hareket_ve_don(shape, adim, aci):
    shape.forward(adim)  # Belirli bir mesafe ileri git
    shape.right(aci)# Belirli bir açıda sağa dön
    shape.backward(adim)# Belirli bir mesafe geri git
    shape.right(aci)# Belirli bir açıda sağa dön
    shape.forward(adim)  # Belirli bir mesafe ileri git
    shape.right(aci)# Belirli bir açıda sağa dön
    shape.backward(adim)  # Belirli bir mesafe geri git
    shape.right(aci)# Belirli bir açıda sağa dön
    shape.backward(adim)  # Belirli bir mesafe geri git
    shape.left(aci)# Belirli bir açıda sola dön
    shape.backward(adim)  # Belirli bir mesafe geri git
    shape.right(aci)# Belirli bir açıda sağa dön
    shape.forward(adim)  # Belirli bir mesafe ileri git
    shape.left(aci)# Belirli bir açıda sola dön
    shape.forward(adim)  # Belirli bir mesafe ileri git
       

# Ana program
def main():
    pencere = turtle.Screen()  # Ekranı oluştur
    pencere.bgcolor("black")   # Arka plan rengini beyaz yap

    shape = turtle.Turtle()    # Şekil nesnesini oluştur
    shape.color("blue")        # Şekil rengini mavi yap
    shape.shape("turtle")      # Şekli turtle olarak ayarla

    adim = 250   # İleri gitme adım miktarı
    aci = 90  # Dönüş açısı (derece cinsinden)

    hareket_ve_don(shape, adim, aci) # Shape'i hareket ettir ve döndür

    pencere.mainloop()  # Programın kapanmasını engelle

if __name__ == "__main__":
    main()
