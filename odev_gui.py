import tkinter as tk

# --- 1. Olay İşleyici (Event Handler) ---
# Düğmeye basılınca (Olay) bu fonksiyon çalışır.
def butona_basildi():
    global sayac
    sayac += 1
    etiket.config(text=f"Tıklama Sayısı: {sayac}")
    print(f"Olay Tetiklendi: Butona basıldı. Yeni değer: {sayac}")

# --- Başlangıç Ayarları ---
sayac = 0

# --- 2. Ana Pencereyi Oluştur ---
pencere = tk.Tk()
pencere.title("Olay Güdümlü Uygulama")
pencere.geometry("300x200")

# Ekrana bir yazı (Label) koy
etiket = tk.Label(pencere, text="Henüz tıklanmadı", font=("Arial", 14))
etiket.pack(pady=20)

# Ekrana bir düğme (Button) koy
# 'command=butona_basildi' kısmı olayı fonksiyona bağlar (Binding)
buton = tk.Button(pencere, text="Bana Tıkla!", command=butona_basildi, font=("Arial", 12), bg="lightblue")
buton.pack()

# --- 3. Olay Döngüsü (Event Loop) ---
# Burası programı açık tutar ve sürekli fare/klavye olaylarını dinler.
print("Uygulama başladı ve olayları bekliyor...")
pencere.mainloop()