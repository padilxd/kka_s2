Fadhil Hilmi M.P 11
dan 
Ahmad Adly Maulana 02
tugas kelompok [KELOMPOK](./kelompok.py)


Hasil Praktikum 1-6 [OUTPUT](./output latihan)


Tugas Analisis 1:
• Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris
hero1 = Hero...? Coba lakukan print(hero1.hp).

JAWAB

Mengubah atribut melalui objek (misalnya hero1.hp = 500) langsung mengubah data objek tersebut.
Perubahan hanya berlaku untuk objek itu saja, tidak memengaruhi objek lain.

Tugas Analisis 2:
• Perhatikan parameter lawan pada method serang. Parameter tersebut
menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini
penting?

JAWAB

Parameter lawan harus berupa objek, bukan string, agar bisa:
Mengakses atribut (lawan.name)
Memanggil method (lawan.diserang())

Ini adalah dasar interaksi antar objek dalam OOP.

Tugas Analisis 3:
• Eksperimen Fungsi super(): Pada class Mage, coba hapus (atau jadikan
komentar #) baris kode super().__init__(name, hp, attack_power). Kemudian
jalankan programnya.
• Pertanyaan: Error apa yang muncul saat kamu mencoba melihat info Eudora
(eudora.info())? Mengapa error tersebut mengatakan Mage object has no
attribute 'name', padahal kita sudah mengirim nama "Eudora" saat
pembuatan objek?
• Jelaskan peran fungsi super() dalam menghubungkan data dari class Anak ke
class Induk!

JAWAB

a. Error yang muncul:
Muncul error: Mage object has no attribute 'name'

b. Penjelasan error:
Walaupun nama “Eudora” dikirim saat membuat objek, data tersebut tidak disimpan
Karena super().__init__() dihapus, constructor parent tidak dijalankan

c. Peran super()
super() menghubungkan data dari class anak ke class induk
Memastikan atribut seperti name, hp, dan attack_power dibuat dengan benar

Tugas Analisis 4:
1. Percobaan Hacking: Coba tambahkan baris kode berikut di bagian paling
bawah (luar class):
print(f"Mencoba akses paksa: {hero1._Hero__hp}")
Pertanyaan: Apakah nilai HP muncul atau Error? Jika muncul, diskusikan dengan
temanmy mengapa Python masih mengizinkan akses ini (konsep Name Mangling)
dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman
yang baik.
2. Uji Validasi: Hapus logika if dan elif di dalam method set_hp, sehingga isinya
hanya self.__hp = nilai_baru.
Pertanyaan: Kemudian lakukan hero1.set_hp(-100).
Apa yang terjadi pada data HP Hero? Jelaskan mengapa keberadaan method
Setter sangat penting untuk menjaga integritas data dalam game!

JAWAB

1. Percobaan Hacking
Jawaban:
Nilai HP muncul, tidak error
Ini karena Name Mangling, Python hanya menyamarkan nama atribut (__hp)
Tetap tidak boleh dilakukan karena:
Melanggar enkapsulasi
Membuat kode sulit dirawat dan berisiko bug

2. Uji Validasi
Jawaban:
Setelah hero1.set_hp(-100), HP menjadi -100
Ini tidak logis untuk game
Setter penting untuk:
Menjaga data tetap valid
Mencegah nilai tidak masuk akal (HP minus / terlalu besar)

Tugas Analisis 5:
1. Melanggar Kontrak: Pada class Hero, hapus (atau jadikan komentar #) seluruh
blok method def serang(self, target):. Jalankan programnya.
Pertanyaan: Error apa yang muncul? Jelaskan dengan bahasamu sendiri, apa arti
pesan error Can't instantiate abstract class Hero with abstract
method...?
Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di
Interface?
2. Mencetak Cetakan: Coba aktifkan baris kode unit = GameUnit().
Pertanyaan: Mengapa class GameUnit dilarang untuk dibuat menjadi objek?
Apa gunanya ada class GameUnit jika tidak bisa dibuat menjadi objek nyata?

JAWAB

1. Melanggar Kontrak
a. Error yang muncul:
Error: Can't instantiate abstract class Hero with abstract method serang

b. Artinya:
Class Hero punya method abstrak yang wajib dibuat
Jika lupa dibuat, class tidak boleh dijadikan objek

c. Konsekuensi:
Program tidak bisa dijalankan
Kontrak interface tidak terpenuhi

2. Mencetak Cetakan
Jawaban:
GameUnit tidak bisa dijadikan objek karena bersifat abstract
Gunanya:
Sebagai kerangka aturan
Memaksa semua turunan punya method penting

Tugas Analisis 6:
1. Uji Skalabilitas (Kemudahan Menambah Fitur): Tanpa mengubah satu huruf
pun pada kode Looping (for pahlawan in pasukan:), buatlah satu class
baru bernama Healer(Hero).
Isi method serang milik Healer dengan: print(f"{self.name} tidak
menyerang, tapi menyembuhkan teman!").
Masukkan objek Healer ke dalam list pasukan.
o Pertanyaan: Apakah program berjalan lancar?
o Kesimpulannya, apa keuntungan Polimorfisme bagi seorang programmer
ketika harus mengupdate game dengan karakter baru di masa depan?
2. Konsistensi Penamaan: Ubah nama method serang pada class Archer
menjadi tembak_panah. Jalankan program.
Pertanyaan: Apa yang terjadi?
Mengapa dalam konsep Polimorfisme, nama method antara Parent Class dan
berbagai Child Class harus persis sama?

JAWAB

1. Uji Skalabilitas
a. Apakah program berjalan?
Ya, berjalan lancar

b. Kesimpulan:
Polimorfisme memungkinkan:
Menambah karakter baru tanpa mengubah kode lama
Kode lebih fleksibel dan mudah dikembangkan

2. Konsistensi Penamaan
a. Apa yang terjadi?
Method serang tidak dipanggil
Program error atau perilaku Archer tidak dijalankan

b. Alasannya:
Polimorfisme bergantung pada nama method yang sama
Jika beda nama, loop tidak mengenali method tersebut


