import datetime

kullanicilar = {}
kitaplar = [
    {'ad': 'Aşk-ı Memnu ', 'yazar': 'Halit Ziya Uşaklıgil'},
    {'ad': 'Araba Sevdası', 'yazar': 'Recaizade Mahmut Ekrem'},
    {'ad': 'Benim Adım Kırmızı', 'yazar': 'Orhan Pamuk'},
    {'ad': 'Beyaz Diş', 'yazar': 'Jack Landon'},
    {'ad': 'Beyaz Gemi ', 'yazar': 'Cengiz Aytmatov'},
    {'ad': 'Acımak', 'yazar': 'Reşat Nuri Güntekin'},
    {'ad': 'Ateşten Gömlek', 'yazar': 'Halide Edip Adıvar'},
    {'ad': 'Suç ve Ceza', 'yazar': 'Fyodor  Mihailoviç Dostoyevski'},
    {'ad': 'Aklından Bir Sayı Tut', 'yazar': 'John Verdon'},
    {'ad': 'Melekler ve Şeytanlar', 'yazar': 'Dan Brown'}
]

def kullanici_kayit():
    ad = input('Adınızı girin: ')
    soyad = input('Soyadınızı girin: ')
    tc = input('TC kimlik numaranızı girin: ')
    
    if tc in kullanicilar:
        print('Bu TC kimlik numarası zaten kayıtlı. Giriş yapabilirsiniz.')
    else:
        kullanicilar[tc] = {'ad': ad, 'soyad': soyad, 'kitaplar': []}
        print('Kaydınız başarıyla tamamlandı.')
        kullanici_islem(tc)

def kullanici_giris():
    tc = input('TC kimlik numaranızı girin: ')
    
    if tc in kullanicilar:
        print('Giriş başarılı.')
        kullanici_islem(tc)
    else:
        print('Kullanıcı bulunamadı. Lütfen kaydolun.')

def kitaplari_goster():
    for i, kitap in enumerate(kitaplar, 1):
        print(f'{i}. Kitap: {kitap["ad"]}, Yazar: {kitap["yazar"]}')

def kullanici_islem(tc):
    while True:
        print('1 - Kütüphaneden kitap al')
        print('2 - Kütüphaneye kitabı teslim et')
        print('3 - Alınan kitapları göster')
        print('4 - Kütüphaneye kitap ekle')
        print('5 - Çıkış yap')
        
        secim = input('Seçiminizi yapın: ')
        
        if secim == '1':
            kitaplari_goster()
            kitap_sec = input('Hangi kitabı almak istersiniz? (Kitap numarasını girin): ')
            kitap_indis = int(kitap_sec) - 1
            
            if kitap_indis >= 0 and kitap_indis < len(kitaplar):
                kitap = kitaplar.pop(kitap_indis)
                kullanicilar[tc]['kitaplar'].append({'kitap': kitap, 'alma_tarihi': datetime.date.today(), 'teslim_tarihi': None})
                print(f'{kitap["ad"]} kitabını aldınız.')
                kullanicilar[tc]['kitaplar'][-1]['teslim_tarihi'] = kullanicilar[tc]['kitaplar'][-1]['alma_tarihi'] + datetime.timedelta(days=15)
                print('Kitabı 15 gün içinde teslim etmelisiniz.')
            else:
                print('Geçersiz kitap numarası.')
        
        elif secim == '2':
            if len(kullanicilar[tc]['kitaplar']) == 0:
                print('Henüz hiç kitap almamışsınız.')
            else:
                print('Aldığınız Kitaplar:')
                for i, kitap_bilgisi in enumerate(kullanicilar[tc]['kitaplar'], 1):
                    kitap = kitap_bilgisi['kitap']
                    print(f'{i}. Kitap: {kitap["ad"]}, Yazar: {kitap["yazar"]}')
                    
                kitap_sec = input('Hangi kitabı iade etmek istersiniz? (Kitap numarasını girin): ')
                kitap_indis = int(kitap_sec) - 1
                
                if kitap_indis >= 0 and kitap_indis < len(kullanicilar[tc]['kitaplar']):
                    verilen_kitap = kullanicilar[tc]['kitaplar'].pop(kitap_indis)
                    kitaplar.append(verilen_kitap['kitap'])
                    print(f'{verilen_kitap["kitap"]["ad"]} kitabını iade ettiniz.')
                else:
                    print('Geçersiz kitap numarası.')
        
        elif secim == '3':
            if len(kullanicilar[tc]['kitaplar']) == 0:
                print('Henüz hiç kitap almamışsınız.')
            else:
                print('Aldığınız Kitaplar:')
                for i, kitap_bilgisi in enumerate(kullanicilar[tc]['kitaplar'], 1):
                    kitap = kitap_bilgisi['kitap']
                    print(f'{i}. Kitap: {kitap["ad"]}, Yazar: {kitap["yazar"]}')
        
        elif secim == '4':
            kitap_adi = input('Kitap adını girin: ')
            yazar_adi = input('Yazar adını girin: ')
            yeni_kitap = {'ad': kitap_adi, 'yazar': yazar_adi}
            kitaplar.append(yeni_kitap)
            print('Kitap başarıyla eklendi.')
        
        elif secim == '5':
            break

def kontrol_et(tc):
    bugun = datetime.date.today()
    for kitap_bilgisi in kullanicilar[tc]['kitaplar']:
        teslim_tarihi = kitap_bilgisi['teslim_tarihi']
        if teslim_tarihi is not None and teslim_tarihi < bugun:
            kitap = kitap_bilgisi['kitap']
            print(f'{kitap["ad"]} kitabını teslim etmeniz gerekiyor!')
            return True
    return False

while True:
    print('KÜTÜPHANEMİZE HOŞGELDİNİZ')
    print('1 - Kaydol')
    print('2 - Giriş yap')
    print('3 - Çıkış yap')
    
    secim = input('Seçiminizi yapın: ')
    
    if secim == '1':
        kullanici_kayit()
        break
    elif secim == '2':
        kullanici_giris()
        while True:
            if kontrol_et(tc):
                kullanici_islem(tc)
            else:
                break
        break
    elif secim == '3':
        break
