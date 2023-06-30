import sqlite3

# Veritabanı bağlantısını oluştur
connection = sqlite3.connect('veritabani.db')

# İşaretçiyi al
cursor = connection.cursor()

# Tabloyu oluştur
cursor.execute('''CREATE TABLE kullanıcılar
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  number TEXT NOT NULL UNIQUE,
                  message TEXT NOT NULL);''')

# Örnek verileri ekle
kullanıcılar = [
    ('John', '+9056566654', 'merhaba'),
    ('Jane', '+9056566655', 'merhaba'),
    ('Alice', '+9056566656', 'merhaba')
]

cursor.executemany('INSERT INTO kullanıcılar (name, number, message) VALUES (?, ?, ?)', kullanıcılar)

# Değişiklikleri kaydet
connection.commit()

# Bağlantıyı kapat
connection.close()