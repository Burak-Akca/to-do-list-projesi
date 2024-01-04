import os
import tkinter as tk
from tkinter import messagebox, ttk

kullaniciAdi=0
kullaniciSifre=0
def kayitStage():#giriş ol sayfasındaki kayıt ol butonuna basınca çalışan fonksiyon

    global girisSayfasi,ikinciPencere



    def kapatEvent():#bu fonksiyon kayıt ol sayfasındaki kapat butonuna basınca çalışır
        #görevi kayıt ol sayfasını kapatıp giriş sayfasını  görünür hale getirir.
        global girisSayfasi, ikinciPencere
        ikinciPencere.destroy()
        girisSayfasi.deiconify()
    def tamamEvent():#kayıt ol sayfasında tamam butonu basınca çalışır kullanıcının bilgileri alınır
        global kullaniciSifre
        global kullaniciAdi
        kullaniciAdi=kayitAdEntry.get()
        kullaniciSifre=kayitSifreEntry.get()
        sifreDogrula=kayitSifreDogrulamaEntry.get()
        if sifreDogrula!=kullaniciSifre:
            messagebox.showerror("Hatalı İşlem","Şifreler Eşleşmiyor")
            kayitSifreEntry.delete(0,"end")
            kayitSifreDogrulamaEntry.delete(0,"end")
        elif kullaniciAdi.strip()=="" or kullaniciSifre.strip()=="":
            messagebox.showerror("Hatalı İşlem","Lütfen Tüm Alanları Doldurunuz")
        else:
         kapatEvent()#biligiler alındıktan sonra giriş sayfasına tekrar dönmek için kullanılır.

    girisSayfasi.withdraw()#kayıt ol butonuna basınca çalışan ilk satırdır görevi giriş sayfasını gizler
#kayıt ol sayfasının arayüz tasarımı 63.satıra kadar olan kısım
    ikinciPencere=tk.Tk()
    ikinciPencere.geometry("300x180+620+330")
    ikinciPencere.title("Kayıt Ol")
    ikinciPencere.configure(bg="#7AEAFF")

    kayitAdLabel=tk.Label(ikinciPencere,text="Kullanıcı Adı",bg="#7AEAFF")
    kayitAdLabel.place(x=40,y=30)
    kayitAdEntry=tk.Entry(ikinciPencere)
    kayitAdEntry.place(x=140,y=30)
    kayitSifreLabel=tk.Label(ikinciPencere,text="Şifre",bg="#7AEAFF")
    kayitSifreLabel.place(x=40,y=63)

    kayitSifreEntry=tk.Entry(ikinciPencere,show="*")#şifreleri gizlemek için show parametresi kullanıldı.
    kayitSifreEntry.place(x=140,y=63)
    kayitSifreDogrulamaLabel=tk.Label(ikinciPencere,text="Şifre Doğrulama",bg="#7AEAFF")
    kayitSifreDogrulamaLabel.place(x=40,y=96)

    kayitSifreDogrulamaEntry=tk.Entry(ikinciPencere,show="*")
    kayitSifreDogrulamaEntry.place(x=140,y=96)


    kapatButton=tk.Button(ikinciPencere,text="Kapat",bg="#FFFFFF",width=8,borderwidth=1,command=kapatEvent)
    kapatButton.place(x=90,y=136)

    tamamButton=tk.Button(ikinciPencere,text="Tamam",bg="#FFFFFF",width=8,borderwidth=1,command=tamamEvent)
    tamamButton.place(x=165,y=136)


    ikinciPencere.mainloop()
def anaStageAc():#giriş sayfasındaki giriş yap butonuna basınca çalışır

    global girisSayfasi,root
    girisSayfasi.withdraw()#giriş sayfası gizleniyor
    global  acikDosyaAdi
    acikDosyaAdi=0#açık olan dosyaya başlangıç olarak 0 değeri verildi

    def ekle():#ekle butonuna basınca çalışır entrylerdeki değerleri hem tabloya hemde açık olan dosyaya kaydeder
        gorev=entryGorev.get()
        ayrinti=entryAyrinti.get()
        onemSirasi=entryOnemSirasi.get()
        entryGorev.delete(0,"end")
        entryAyrinti.delete(0,"end")
        entryOnemSirasi.delete(0,"end")
        try:
            if not (gorev and ayrinti and onemSirasi):

                messagebox.showerror("Hatalı İşlem","Lütfen Görev Bilgilerini Eksiksiz Giriniz")

            elif (type(int(onemSirasi))!=int):
                messagebox.showerror("Hatalı İşlem","Lütfen Önem Sırası Kısmına Tam Sayı Giriniz")

            else:
                # eklenecek olan görevi tabodaki diğer ögelerin önem sırasıyla kendi önem sırası karşılaştırılarak tablodaki konumu bulunur
                konum = 0
                for item in tree.get_children():
                    values=tree.item(item,'values')
                    if int(onemSirasi)<int(values[2]):
                        break
                    konum+=1

                # Yeni görevi tabloya ekle
                tree.insert('',konum,values=(gorev,ayrinti,onemSirasi,'Tamamlanmadı'))#konumu bulunduktan sonra tabloya eklenir
                dosyayaKaydet()

        except ValueError :

            messagebox.showerror("Hatalı İşlem","Lütfen Önem Sırası Kısmına Tam Sayı Giriniz")

    def sil():#sil butonuna basınca çalışır
        secilenSatir=tree.selection()#tablodaki seçilen satır bilgisini alınır
        if not (secilenSatir):
            messagebox.showerror("Hatalı İşlem","Lütfen Silmek İstediğiniz Satırı Seçiniz")
        else:
            tree.delete(secilenSatir)#seçilen satır silinir
            dosyayaKaydet()

    def duzenle():#düzenle butonuna basınca çalışır
        secilenSatir=tree.selection()
        if not secilenSatir:
            messagebox.showerror("Hatalı İşlem","Lütfen Düzenlemek İstediğiniz Satırı Seçiniz")
        else:
            try:
                gorev=entryGorev.get()
                ayrinti=entryAyrinti.get()
                onemSirasi=entryOnemSirasi.get()
                if not (gorev and ayrinti and onemSirasi):
                    messagebox.showerror("Hatalı İşlem","Lütfen Görev Bilgilerini Eksiksiz Giriniz")

                else:
                    # Yeni önem sırasını int'e çevir
                    onemSirasi=int(onemSirasi)
                    tree.delete(secilenSatir)

                    # Yeni önem sırasına göre uygun konumu bul
                    konum = 0
                    for item in tree.get_children():
                        values=tree.item(item,'values')#buradan demet değer döner bu sözlük values değğişkeninde tutulur
                        if onemSirasi<int(values[2]):#values[2] içinde bulunduğumuz satırın 2 sütununu döner buda önemsırası sütununa denktir
                            break
                        konum+=1

                    # Yeni konumda öğeyi ekleyin
                    tree.insert('',konum,values=(gorev,ayrinti,onemSirasi,'Tamamlanmadı'))

                    entryGorev.delete(0,'end')
                    entryAyrinti.delete(0,'end')
                    entryOnemSirasi.delete(0,'end')
                    dosyayaKaydet()
            except(ValueError):
                messagebox.showerror("Hatalı İşlem","Lütfen Önem Sırası Kısmına Tam Sayı Giriniz")

    def tamamla():#tamamla butonuna basınca gerçekleşen fonksiyondur
        secilenSatir=tree.selection()
        if not secilenSatir:
            messagebox.showerror("Hatalı İşlem","Lütfen Tamamlamak İstediginiz Görevi Seçin")

        else:#seçilen ifadenin tamamlanmadı değeri tamamlandı olarak güncellenir
            tree.item(secilenSatir,values=(
                tree.item(secilenSatir,'values')[0],tree.item(secilenSatir,'values')[1],tree.item(secilenSatir,'values')[2], 'Tamamlandı'))
            dosyayaKaydet()

    def dosyaAc():#dosyayı aç butonuna basınca çağrılan fonksiyondur
        global acikDosyaAdi
        if acikDosyaAdi!=0:#eğer açık dosya varsa tekradan başka dosyasını engellemek için kullanılır.
            messagebox.showerror("Hatalı İşlem","Önce Açık Olan Dosyayı Kapatmalısınız")

        else:
          acikDosyaAdi=dosyaEntry.get()
          print(acikDosyaAdi)
          dosyaYolu= acikDosyaAdi + ".txt"
          if not acikDosyaAdi:
              messagebox.showerror("Hatalı İşlem","Lütfen Dosya Adına Bir İfade Giriniz")
          elif not os.path.exists(dosyaYolu):
              messagebox.showinfo("Bilgilendirme",acikDosyaAdi+" adlı dosya Oluşturuldu ve açıldı")
              for item in tree.get_children():
                  tree.delete(item)
              with open(dosyaYolu, 'w') as dosya:
                  pass


          else:
              with open(dosyaYolu, 'r') as dosya:
                  messagebox.showinfo("Bilgilendirme",acikDosyaAdi+" adlı dosya açıldı")

                  for item in tree.get_children():#tabloda var olan bilgiler silindi
                      tree.delete(item)
                      #açılan dosyadaki bilgiler tabloya eklendi

                  for line in dosya.readlines():
                      values=line.strip().split(',')
                      tree.insert('','end',values=values)

    def dosyayaKaydet():#her ekleme silme tamamlamave düzenleme işleminden sonra tabloyu yeni haliyle dosyaya baştan kaydeder.
        dosyaAdi=dosyaEntry.get()
        dosyaYolu=dosyaAdi+".txt"

        with open(dosyaYolu,'w') as dosya:

            for item in tree.get_children():
                satirlar=tree.item(item,'values')
                dosya.write(f"{satirlar[0]},{satirlar[1]},{satirlar[2]},{satirlar[3]}\n")
    def dosyaKapat():#dosyayı kapat butonuna basınca çağrılan fonksiyondur
        global acikDosyaAdi
        girilenDosyaAdi=dosyaEntry.get()

        if girilenDosyaAdi== "":
            messagebox.showerror("Hatalı İşlem","Lütfen bir ifade giriniz")
        elif acikDosyaAdi==0:#herhangi bir dosya açık değilse 0 değerinde olduğu için
            messagebox.showerror("Hatalı İşlem","Açık Olmayan Dosyayı Kapatamazsınız")

        elif girilenDosyaAdi!=acikDosyaAdi:
            messagebox.showerror("Hatalı İşlem","Açık Olan Dosya: "+acikDosyaAdi)
        else:
         messagebox.showinfo("Bilgilendirme",girilenDosyaAdi+" adlı dosya kapatıldı")
         dosyaEntry.delete(0,"end")#dosya kapatılır
         acikDosyaAdi=0
         for item in tree.get_children():
            tree.delete(item)

    def giriseDon():#anastageden giriş sayfasına dönmek için kullanılır
        global girisSayfasi,root
        root.destroy()  # anapencereyi pencereyi kapatır

        girisSayfasi.deiconify()#giriş sayfasını açığa çıkartır.


    root =tk.Tk()
    root.title("To-Do List")
    root.geometry("600x450+520+230")
    root.configure(bg="#7AEAFF")
    dosyaFrame=tk.Frame(root,bg="#7AEAFF",relief=tk.GROOVE,bd=8)

    dosyaFrame.place(x=0,y=0)
    dosyaAdiLabel=tk.Label(dosyaFrame,text="Dosya Adı",bg="#7AEAFF")
    dosyaAdiLabel.grid(row=0,column=0)
    dosyaEntry = tk.Entry(dosyaFrame, width=12)
    dosyaEntry.grid(row=0, column=1, pady=10)
    dosyaKapatButton=tk.Button(dosyaFrame,text="Dosyayı Kapat",width=10,bg="#FFFFFF",borderwidth=1,command=dosyaKapat)
    dosyaKapatButton.grid(row=1,column=0,padx=6)

    dosyaAcButton = tk.Button(dosyaFrame,text="Dosyayı Aç", command=dosyaAc, width=10, borderwidth=1, bg="#FFFFFF")
    dosyaAcButton.grid(row=1, column=1, padx=6)



    anaFrame = tk.Frame(root, relief=tk.GROOVE,bg="#7AEAFF",bd=8)
    anaFrame.place(x=400,y=100)

    gorevLabel = tk.Label(anaFrame, text="Görev:",bg="#7AEAFF")
    gorevLabel.grid(row=0,column=0)
    entryGorev = tk.Entry(anaFrame,width=20)
    entryGorev.grid(row=0,column=1)

    ayrintiLabel = tk.Label(anaFrame,text="Ayrıntı:",bg="#7AEAFF")
    ayrintiLabel.grid(row=1,column=0)
    entryAyrinti = tk.Entry(anaFrame,width=20)
    entryAyrinti.grid(row=1,column=1)

    onemLabel = tk.Label(anaFrame, text="Önem Sırası:",bg="#7AEAFF")
    onemLabel.grid(row=2,column=0)
    entryOnemSirasi = tk.Entry(anaFrame,width=20)
    entryOnemSirasi.grid(row=2,column=1)


    buttonFrame = tk.Frame(anaFrame,bg="#7AEAFF")
    buttonFrame.grid(row=3, column=0,columnspan=2, pady=10)

    ekleButton = tk.Button(buttonFrame,text="Ekle",bg="#FFFFFF",command=ekle,width=8,borderwidth=1)
    ekleButton.grid(row=0, column=0, padx=(0, 3))

    silButton = tk.Button(buttonFrame,text="Sil",bg="#FFFFFF",command=sil,width=8,borderwidth=1)
    silButton.grid(row=0, column=1, padx=(3, 0))

    duzenleButton = tk.Button(buttonFrame,text="Düzenle",bg="#FFFFFF",command=duzenle,width=8,borderwidth=1)
    duzenleButton.grid(row=1, column=0, padx=(0, 3), pady=5)

    tamamlaButton = tk.Button(buttonFrame,text="Tamamla",bg="#FFFFFF",command=tamamla,width=8,borderwidth=1)
    tamamlaButton.grid(row=1, column=1,pady=0, padx=(3, 0))



    anaFrame.pack()
    cikisButton=tk.Button(root,text="Çıkış Yap",command=giriseDon,bg="#FF0000",fg="#FFFFFF",width=8,borderwidth=1)
    cikisButton.pack(pady=10 )

    sutunlar = ('Görevler','Ayrıntı','Önem Sırası','Durum')
    tree=ttk.Treeview(root,columns=sutunlar,show='headings')

    for sutun in sutunlar:
        tree.heading(sutun,text=sutun)#sütunlar oluşturuldu
        tree.column(sutun,width=150)

    tree.place(y=226)

    root.mainloop()


def girisEvent():#giriş yap butonuna basınca gerçekleşen fonksiyondur
    #girilen bilgileri kontrol eder
    if kullaniciAdi==kullaniciAdiEntry.get()and kullaniciSifre == sifreEntry.get() and kullaniciAdiEntry.get().strip() != "" and sifreEntry.get().strip() != "":
        kullaniciAdiEntry.delete(0,"end")
        sifreEntry.delete(0,"end")

        anaStageAc()
    else:
        messagebox.showerror("Hatalı İşlem","Kayıtlı Kullanıcı Bulunamadı")

#giriş sayfasının tüm komponentleri oluşsturuldu.

girisSayfasi = tk.Tk()
girisSayfasi.title("Giriş")
girisSayfasi.geometry("300x150+620+330")
girisSayfasi.configure(bg="#7AEAFF")



kullaniciLabel = tk.Label(girisSayfasi,text="Kullanıcı Adı",bg="#7AEAFF")
kullaniciLabel.place(x=40,y=30)
kullaniciAdiEntry = tk.Entry(girisSayfasi)
kullaniciAdiEntry.place(x=140,y=30)
sifreLabel = tk.Label(girisSayfasi,text="Şifre",bg="#7AEAFF")
sifreLabel.place(x=40,y=63)
sifreEntry = tk.Entry(girisSayfasi,show="*")
sifreEntry.place(x=140,y=63)
kayıtOlButton = tk.Button(girisSayfasi, text="Kayıt Ol", command=kayitStage, bg="#FFFFFF", width=8, borderwidth=1)
kayıtOlButton.place(x=90, y=103)


girisYapButton = tk.Button(girisSayfasi, text="Giriş Yap", command=girisEvent, bg="#FFFFFF", width=8, borderwidth=1)
girisYapButton.place(x=165, y=103)


girisSayfasi.mainloop()
