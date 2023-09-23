Application Link: https://minechesty.adaptable.app <br>
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   
- [x] Membuat sebuah proyek Django baru. <br>

+ Membuat direktori minechesty dan menginisialisasi git dengan `git init` serta hubungkan dengan repositori di github dengan `git remote add origin [link]`
+ Di dalam direktori tersebut, buka command prompt (Windows) atau terminal shell (Unix) lalu buat virtual environment dengan perintah `python -m venv env` 
+ Mengaktifkan virtual environment dengan perintah `env\Scripts\activate.bat` 
+ Pada direktori yang sama buat `requirements.txt` dan tambahkan beberapa dependencies
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
``` 
+ Pasang dependencies dengan perintah `pip install -r requirements.txt` 
+ Buat proyek Django bernama minechesty dengan perintah `django-admin startproject minechesty .` 
+ Tambahkan * pada ALLOWED_HOSTS di `settings.py` untuk keperluan deployment 
```
  ... 
  ALLOWED_HOSTS = ["*"] 
  ... 
```
+ Menguji apakah proyek minechesty berhasil dibuat dengan perintah `python manage.py runserver`
+ Buka http://localhost:8000 pada web yang biasa dipakai untuk melihat animasi roket sebagai tanda aplikasi Django berhasil dibuat. 
+ Untuk menghentikan server tekan Ctrl+C (Windows/Linux) 
+ Tambahkan Berkas .gitignore yang berisi code dibawah sehingga Repositori Git tau mana berkas-berkas atau direktori-direktori yang diabaikan
```
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```

- [x] Membuat aplikasi dengan nama `main` pada proyek minechesty.
      
+ Membuat aplikasi "main" dengan perintah `python manage.py startapp main`
+ Memasukkan aplikasi main ke dalam proyek dengan cara membuat settings.py pada direktori proyek minechesty lalu memasukkan `main` ke dalam variable INSTALLED_APPS 
```
      INSTALLED_APPS = [ 
          ..., 
          'main', 
          ... 
      ]
```

- [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.

+ Buka berkas `urls.py` di dalam direktori proyek `minechesty`
+ Impor fungsi `include` dari `django.urls`
```
...
from django.urls import path, include
...
```
+ Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main di dalam variabel urlpatterns
```
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```

- [x] Membuat model pada aplikasi main.
      
+ Membuka `models.py` dan membuat model Item serta beberapa atribut.
```
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    rarity = models.TextField(default='uncommon', editable=False)
```
+ Migrasi model
```
python manage.py makemigrations
```
+ Migrasi ke dalam basis data lokal
```
python manage.py migrate
```

- [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
+ Buka berkas `views.py` pada direktori aplikasi `main`
+ Menambahkan pasangan key-value yang dibutuhkan dalam variabel context pada `views.py`
```
from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Muhammad Rafli Mahesa',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
```
+ Membuat direktori `templates` pada direktori `main` lalu membuat berkas `main.html` di dalamnya.
+ Isilah sesuai dengan nama aplikasi, nama, dan kelas
```
<h1>MineChesty</h1>

<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
```

- [x] Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.
      
+ Buatlah berkas `urls.py` di dalam direktori `main`.
+ Isilah `urls.py` dengan kode
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

- [x] Melakukan deployment ke Adaptable
      
+ Pertama-tama lakukan simpan direktori ke Github dengan cara
```
git add *
```
```
git commit -m "<KOMENTAR>"
```
```
git push -u origin main
```
+ Masuk ke web Adaptable.io lalu login dan tombol `new app`. Pilih `Connect an Existing Repository`
+ Pilihlah repositori proyek minechesty sebagai basis-aplikasi yang akan di deploy. Lalu pilih branch yang akan dijadikan deployment branch
+ Pilihlah `Python App Template` sebagai template deployment
+ Pilih `PostgreSQL` sebagai tipe basis data yang akan digunakan
+ Pilih Python versi 3.11
+ Pada bagian Start Command masukkan perintah python manage.py migrate && gunicorn minechesty.wsgi
+ Masukkan nama aplikasi yang akan dijadikan domain web
+ Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk mulai proses deployment aplikasi

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![bagan](https://cdn.discordapp.com/attachments/1141216017255776401/1151175617052688384/image.png)
+ User adalah pengguna/individu yang mengakses aplikasi web
+ URLConf(`urls.py`) adalah file yang digunakan untuk mendefisikan rute URL pada aplikasi web. Setiap rute URL yang dibuat akan terkait dengan salah satu fungsi view yang menangani permintaan HTTP yang sesuai
+ Model(`models.py`) adalah file yang digunakan untuk membuat struktur data yang akan disimpan di dalam database.
+ Views(`views.py`) adalah file yang berfungsi sebagai tempat penyimpanan fungsi-fungsi yang mengendalikan bagaimana permintaan HTTP dari pengguna diterima, data dari database diakses dan diproses (menggunakan model), lalu tampilan HTML yang dihasilkan dengan template dikembalikan.
+ Template adalah file HTML yang digunakan untuk menghasilkan tampilan yang akan ditampilkan kepada pengguna. Template ini biasanya mengandung kode HTML.
+ Database adalah tempat di mana data aplikasi disimpan secara permanen. Views dapat mengakses dan mengubah data sesuai dengan model data yang sudah dibuat oleh Model.

Pada pengembangan aplikasi web dengan Django, pengguna mengirimkan permintaan HTTP ke alamat web tertentu yang telah ditentukan dalam file `urls.py`. Alamat web ini terhubung dengan fungsi view yang ada dalam file `views.py`. Fungsi view tersebut akan mengambil dan memproses data dari database menggunakan definisi model dalam file `model.py`. Hasilnya akan ditampilkan melalui tampilan HTML yang telah dibuat dengan template, kemudian dikirimkan kembali kepada pengguna sebagai tampilan web.


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment (lingkungan virtual) adalah cara untuk membuat suatu "ruang kerja" yang terisolasi di komputer kita pada proyek perangkat lunak yang kita kerjakan. Setiap "ruang kerja" mungkin memiliki versi Python berbeda dengan yang diperlukan untuk masing-masing proyek. Selain itu karena berbagai proyek memiliki package dan dependencies yang berbeda-beda, maka dengan penggunaan virtual environment akan ada sekat yang dapat mencegahnya bertabrakan/bentrok.

Meskipun kita tetap bisa membuat aplikasi web berbasis Django tanpa virtual environment, namun penggunaan virtual environment akan lebih baik dan efektif. Dengan virtual environment, kita seperti memiliki "ruang kerja" yang terisolasi satu sama lain untuk mencegah bentroknya package serta dependencies yang berbeda versi dengan yang sudah ada di perangkat kita. Dengan demikian maka dalam pengembangan web berbasis Django lebih efektif jika menggunakan virtual environment.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

Model-View-Controller (MVC), Model-View-ViewModel (MVVM), dan Model-View-Template (MVT) merupakan pola desain arsitektur yang memisahkan aplikasi menjadi tiga komponen utama yang saling berhubungan, yaitu model, view, dan controller atau viewModel atau template. 

a. MVC (Model-View-Controller)
MVC adalah pola desain arsitektur yang membagi aplikasi menjadi 3 bagian yaitu: model, view, dan controller.
* Model bertanggung jawab untuk mengatur dan mengelola data dari aplikasi.
* View merupakan komponen yang menangani logika presentasi dalam konsep MVT. View bertanggung jawab untuk mengatur tampilan dan mengambil data dari model untuk disajikan kepada pengguna
* Controller berperan dalam menerima masukan dari pengguna, mengatur komunikasi antara Model (data dan logika bisnis) dengan View (antarmuka pengguna), serta melakukan pemrosesan masukan tersebut untuk menentukan tindakan yang perlu diambil terkait data Model dan tampilan View.

b. MVT (Model-View-Template)
MVT adalah pola yang mirip dengan MVC, tetapi controller digantikan dengan Template. MVT biasanya digunakan dalam pengembangan web dengan Django web framework.
* Model bertanggung jawab untuk mengatur dan mengelola data dari aplikasi.
* View merupakan komponen yang menangani logika presentasi dalam konsep MVT. View bertanggung jawab untuk mengatur tampilan dan mengambil data dari model untuk disajikan kepada pengguna
* Template adalah komponen yang berfungsi untuk mengatur tampilan atau antarmuka pengguna. Template digunakan untuk merancang tampilan HTML dan menampilkan data dari model melalui view.

c. MVVM (Model-View-ViewModel)
MVVM adalah varian modern dari MVC yang biasa digunakan untuk mengembangkan aplikasi web yang dapat digunakan kembali dan mudah diuji.
* Model bertanggung jawab untuk mengatur dan mengelola data dari aplikasi.
* View: bertanggung jawab untuk tampilan
* ViewModel: Bertugas untuk menghubungkan Model dan View. ViewModel tidak memiliki referensi ke View dan View tidak perlu menunggu proses pada ViewModel. ViewModel melakukan observe terhadap Model, sehingga jika ada perubahan di Model, ViewModel akan tahu

Perbedaan utama antara ketiga pola ini terletak pada bagaimana mereka mengelola komunikasi antara Model dan View. 
* Dalam MVC, Controller bertanggung jawab untuk mengelola komunikasi antara Model dan View menggunakan peristiwa. 
* Dalam MVVM, kerangka kerja melakukan semua pengangkatan berat menggunakan fitur yang disebut data pengikatan data. ViewModel di MVVM membantu menjaga tampilan terpisah dari model, dan pada saat yang sama, bertindak sebagai pengontrol untuk memfasilitasi komunikasi antara tampilan dan komponen model. 
* Dalam MVT, Template bertugas untuk mengurus bagaimana halaman/halaman web ditampilkan di browser.

--------------------------__TUGAS 2__--------------------------

1. Apa perbedaan antara form POST dan form GET dalam Django?
Form POST dan form GET memiliki tujuan yang berbeda. Jika terdapat `request` yang bisa merubah keadaan pada system, seperti contoh mengubah sesuatu pada database maka gunakan POST. Jika terdapat `request` yang tidak merubah keadaan pada system maka gunakan GATE. Cara kerja form POST adalah data yang dimasukkan dalam form akan dikirimkan ke server sebagai bagian dari body permintaan HTTP sedangkan form GET data yang dimasukkan ke formulir akan dikirimkan ke server melalui URL sebagai bagian dari query String.

Contoh:
__POST__ 
```
/hasil-pencarian.php HTTP/1.1
```
__GET__
```
/hasil-pencarian.php?kata_kunci=kucing HTTP/1.1
```

Metode GET tidak cocok untuk formulir kata sandi, data besar, atau data biner karena informasinya muncul dalam URL dan meningkatkan risiko keamanan, sementara cocok digunakan dalam formulir pencarian web karena URL hasil pencarian dapat dengan mudah dibookmark atau dibagikan. Sedangkan metode POST lebih aman untuk formulir admin dengan perlindungan tambahan seperti CSRF. Jadi kesimpulannya __GET__ digunakan untuk mengambil data dari server dan __POST__ digunakan untuk mengirim data ke server.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
__Struktur Data__
+ Pada XML data disimpan dengan struktur pohon dengan namespace untuk kategori data yang berbeda. Pada XML sudah memiliki tag yang telah ditentukan, namun user tetap dapat membuat atau menambah tag mereka sendiri.
+ Pada JSON data disimpan dengan struktur seperti dictionary pada python yaitu dengan pasangan `key`-`value` sehingga JSON lebih sederhana dan memiliki syntaks yang lebih ringkas dibanding XML.
+ HTML digunakan untuk membangun struktur dan tampilan halaman web. Pada HTML tag telah ditentukan sebelumnya dan user tidak memiliki fleksibilitas untuk membuat tag mereka sendiri seperti pada XML dan JSON dalam hal menyimpan data.

__Penggunaan dan Penerapan__
+ Pada XML mendukung berbagai jenis data seperti string, integer, boolean, date, image, namespace, dan custom types sesuai kebutuhan
+ Pada JSON data dikirim melalui internet dalam format yang lebih ringkas dan mudah ditulis. JSON lebih umum digunakan dalam pengembangan aplikasi web dan API karena dukungan yang kuat dari JavaScript
+ HTML digunakan untuk membangun tampilan web dan tidak secara khusus dirancang untuk pengiriman data. HTML lebih cocok untuk menampilkan data secara visual kepada user

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
+ JSON mudah ditulis dan dipahami karena format `key`-`value` dan array yang mudah dibaca oleh manusia.
+ Fleksibel karena JSON dapat menyimpan beragam struktur data seperti objek, array, string, dan tipe data lainnya yang sering dipakai.
+ Memiliki native format JavaScript dan mudah diparse oleh broswer.
+ Compatible dengan banyak bahasa pemrograman seperti JavaScript, Python, Java, C#, Ruby, PHP, C++.


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [x] Membuat input `form` untuk menambahkan objek model pada app sebelumnya. <br>
+ Pada direktori `main` buat berkas baru `forms.py`. Lalu isilah dengan kode dibawah ini
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```
+ Buka berkas `views.py` pada direktori `main` dan tambahkan beberapa import
```
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
```
+ Lalu pada file yang sama, buatlah fungsi baru bernama `create_product` dengan parameter `request` seperti dibawah ini
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
+ Ubah fungsi `show_main` yang sudah ada pada berkas `views.py` menjadi seperti berikut 
```
def show_main(request):
    item = Item.objects.all()

    context = {
        'app_name' : 'MineChesty',
        'name' : 'Muhammad Rafli Mahesa',
        'class': 'PBP E',
        'item' : item
    }

    return render(request, "main.html", context)
```
+ Buka `urls.py` pada direktori `main` dan import fungsi `create_product`
```
from main.views import show_main, create_product
```
+ Tambahkan path url ke dalam `urlpatterns` pada `urls.py` di `main`
```
path('create-product', create_product, name='create_product'),
```
- [x] Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID. <br>

__Fungsi `views` untuk formal HTML__
+ Lalu pada `views.py` lengkapi fungsi `show_main` untuk melihat dalam format HTML dengan menambahkan beberapa kode menjadi seperti dibawah ini 
```
def show_main(request):
    item = Item.objects.all()
    total_item = 0
    for i in item:
        total_item += 1

    context = {
        'app_name' : 'MineChesty',
        'name' : 'Muhammad Rafli Mahesa',
        'class': 'PBP E',
        'item' : item,
        'total' : total_item
    }

    return render(request, "main.html", context)
```

__Fungsi `views` untuk format XML__
+ Buka `views.py` pada direktori `main` dan tambahkan import `HttpResponse` dan `Serializer`.
```
from django.http import HttpResponse
from django.core import serializers
```
+ Buat fungsi `show_xml` yang menerima parameter request dan buat sebuah variable untuk menyimpan hasil query dari seluruh data yang ada pada Items serta tambahkan return function berupa `HttpResponse` yang berisi parameter data hasil `query` yang sudah diserialisasi menjadi format XML dan parameter `content_type="application/xml"`.
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
__Fungsi `views` untuk format JSON__
+ Pada berkas `views.py` pada direktori `main`, buat fungsi `show_json` yang menerima parameter request dan buat sebuah variable untuk menyimpan hasil query dari seluruh data yang ada pada Items serta tambahkan return function berupa `HttpResponse` yang berisi parameter data hasil `query` yang sudah diserialisasi menjadi format JSON dan parameter `content_type="application/json"`.
```
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
__Fungsi `views` untuk format XML by ID dan JSON by ID__
+ Buka berkas `views.py` pada direktori `main` dan buatlah fungsi baru yang menerima parameter request dan id dengan nama `show_xml_by_id` dan `show_json_by_id`. Lalu buat sebuah variable untuk menyimpan hasil query dari seluruh data yang ada pada Items. Tambahkan return function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter `content_type` dengan value `"application/xml"` (untuk format XML) atau `"application/json"` (untuk format JSON).
+ XML
```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
+ JSON
```
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

- [x] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2. <br>
+ Buka berkas `urls.py` pada direktori `main` dan import fungsi yang sudah dibuat
```
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
```
+ Tambahkan beberapa path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimport

```
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
```


- [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.

__Dokumentasi Akses URL HTML__
![HTML](https://media.discordapp.net/attachments/1141216017255776401/1153686627059761202/image.png?width=1073&height=633)
__Dokumentasi Akses URL XML__
![XML](https://media.discordapp.net/attachments/1141216017255776401/1152987450168311849/image.png?width=1187&height=542)
__Dokumentasi Akses URL JSON__
![JSON](https://media.discordapp.net/attachments/1141216017255776401/1152987210723885167/image.png?width=1048&height=633)
__Dokumentasi Akses URL XML by ID__
![XML by ID](https://media.discordapp.net/attachments/1141216017255776401/1152987565578801305/image.png?width=1187&height=357)
__Dokumentasi Akses URL JSON by ID__
![JSON by ID](https://media.discordapp.net/attachments/1141216017255776401/1152987653298475058/image.png?width=1187&height=454)

--------------------------__TUGAS 3__--------------------------

1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
Django `UserCreationForm` adalah sebuah `import` untuk formulir bawaan dari `django.contrib.auth.forms` yang memudahkan kita untuk membuat formulir register untuk user dalam aplikasi web. Dengan Django `UserCreationForm`, user baru bisa register dengan mudah di web tanpa harus menulis kode lagi dari awal.
__Kelebihan:__
+ Dengan menggunakan form ini untuk registrasi user baru kita tidak perlu menulis lagi dari awal.
+ UserCreationForm sudah terintegrasi dengan sistem otentikasi Django sehingga ketika form berhasil disimpan maka UserCreationForm akan membuat pengguna baru dan menyimpannya ke database.
+ UserCreationForm sudah mempunyai sistem validasi otomatis untuk mengecek apakah data user sesuai dengan aturan yang ditentukan, misal apakah username unik serta kecocokan antara password1 dan password2. Selain itu juga mengecek apakah password terlalu mudah ditebak atau tidak.
__Kekurangan:__
+ Terbatasnya field untuk data karena hanya terdapat 3 field bawaan yaitu username, password1, dan password2. Jika kita butuh field tambahan seperti email, alamat, atau informasi lain yang biasa dipakai dalam registrasi maka kita harus menambahkannya lagi sendiri. 
+ Terbatas desain bawaan sehingga jika ingin kita ubah, maka kita bisa sesuaikan dengan kemauan kita.
2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting? <br>

__Autentikasi:__
+ Autentikasi adalah proses verifikasi user yang masuk ke dalam system.
+ Autentikasi dapat dilakukan dengan berbagai metode, namun pada Django autentikasinya berupa form. <br>

__Otorisasi:__
+ Otorisasi adalah proses penentuan hak akses yang diberikan kepada user setelah melewati tahap autentikasi.
+ Otorisasi bertujuan agar user dapat memiliki akses ke system sesuai dengan peran mereka dan tidak melewati batas izin dari peran mereka sendiri.
+ Otorisasi dalam Django adalah cara mengontrol siapa yang dapat melakukan apa di dalam aplikasi web Anda dengan menggunakan sistem izin serta autentikasi pengguna.

Jadi, kedua aspek yaitu autentikasi dan otorisasi saling melengkapi dan sangat penting dalam pengembangan web karena: <br>
+ Autentikasi memverifikasi identitas pengguna dan memastikan bahwa hanya mereka yang memiliki hak akses yang sah dapat masuk ke sistem.
+ Otorisasi mengatur apa yang dapat dilakukan oleh pengguna yang sudah terautentikasi, sehingga melindungi data dan sumber daya dari akses yang tidak sah atau tidak diizinkan, berdasarkan peran atau izin yang dimilikinya.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies dalam konteks aplikasi web adalah sebuah file teks kecil yang dikirim oleh server web ke browser user dan disimpan pada perangkat user. File tersebut berisi informasi seperti ID sesi, preferensi pengguna, dan data lain yang relevan dengan interaksi pengguna dengan situs web. 

Django menggunakan cookies dalam mengelola data sesi pengguna dengan menyimpan ID sesi user. Jadi ketika User tersebut mengakses suatu web maka akan dibuat ID sesi unik untuk User tersebut yang dimana ID ini akan dipakai untuk mengidentifikasi sesi si User tersebut. Akan tetapi untuk data sesi User tidak disimpan di cookies tersebut melainkan disimpan di server Django. Django mengaksesnya dengan mengaitkan data ini sesuai dengan ID sesi yang sesuai.

Django secara default menyimpan ID user dalam cookie yang disebut `sessionid`. Cookie dari user ini akan dikirim ke server untuk membuat permintaan dan dipakai untuk mengidentifikasi sesi dari user agar Django dapat mengembalikan data sesi sesuai dari ID user tersebut. Jadi Django menyediakan alat berupa `request` dan `response`.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? <br>
Penggunaan cookies dalam pengembangan web dapat menjadi aman apabila kita bisa mengelolanya dengan baik dan tetap mematuhi aturan keamanan yang tepat. Namun, walaupun begitu tetap ada potensi risiko keamanan terkait dengan cookies yang harus diwaspadai seperti pelacakan oleh pihak ketiga, pelanggaran privacy, dan serangan cross-site scripting (penyerang menyisipkan kode berbahaya ke dalam cookies). Jadi kita harus tetap waspada dan mencegah risiko walaupun seminimal mungkin, misal dengan membuat enkripsi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar. <br>
<br>

__REGISTER__ <br>
+ Buka berkas `views.py` pada direktori `main` dan tambahkan beberapa import dibawah ini.
```
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```
+ Tambahkan juga fungsi baru bernama `register` seperti kode dibawah ini.
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
+ Selanjutnya pada direktori `templates` yang berada pada direktori `main` buatlah berkas HTML `register.html` dan isi dengan potongan kode berikut.
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
<br>

__LOGIN__ <br>
+ Buka berkas views.py pada direktori `main` dan buatlah fungsi `login_user` seperti kode berikut.
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
+ Tambahkan import `authenticate` dan `login` pada bagian atas.
```
from django.contrib.auth import authenticate, login
```

+ Buatlah berkas baru bernama `login.html` pada direktori `templates` yang ada pada direktori `main` lalu isi dengan kode berikut.
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
<br>

__LOGOUT__ <br>
+ Buka berkas `views.py` pada direktori main dan buatlah fungsi `logout_user` seperti kode dibawah ini
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
+ Tambahkan juga import pada bagian atas
```
from django.contrib.auth import logout
```
+ Buka berkas `main.html` pada direktori `templates` yang ada pada direktori `main` lalu tambahkan kode berikut setelah hyperlink tag untuk Add New Product.
```
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```
+ Setelah selesai membuat beberapa fungsi dan file HTML diatas maka bukalah berkas urls.py pada direktori main dan tambahkan import berikut.
```
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user
```
+ Tambahkanlah juga beberapa potongan kode berikut pada `urlpatterns`
```
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
```
+ Selanjutnya tambahkan restriksi pada halaman main agar sesuai dengan user yang sedang login. Pertama-tama buka berkas `views.py` yang ada pada direktori `main` dan tambahkan import `login_required` pada bagian atas
```
from django.contrib.auth.decorators import login_required
```
+ Tambahkan juga kode `@login_required(login_url='/login')` di atas fungsi `show_main`.
```
...
@login_required(login_url='/login')
def show_main(request):
...
```
- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal. <br>
+ Pertama membuka http://127.0.0.1:8000/ pada browser.
+ Lalu tekan tombol `Register Here!!` untuk membuat 2 akun baru
+ Setelah selesai membuat 2 akun baru lalu, login dengan username dan password sesuai dengan yang sudah dibuat pada form register
+ Lalu tekan tombol `add new product` untuk membuat dummy data, dan buatlah masing-masing 3 dummy data per akun.
+ Dua akun pengguna dengan masing-masing 3 dummy data berhasil dibuat!

- [x] Menghubungkan model Item dengan User. <br>
+ Buka berkas `models.py` pada direktori `main` dan tambahkan kode berikut.
```
...
from django.contrib.auth.models import User
...
```
+ Tambahkan juga pada model `Item` yang sudah dibuat potongan kode berikut.
```
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
+ Buka `views.py` pada direktori `main` dan ubah potongan kode pada `create_product` menjadi seperti dibawah ini.
```
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
```
+ Pada fungsi `show_main` juga ubah menjadi seperti berikut.
```
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        ...
        'name': request.user.username,
    ...
    }
```
+ Simpan semua perubahan dengan melakukan `python manage.py makemigrations` pada cmd
+ Seharusnya akan muncul error saat melakukan migrasi model. Pilih 1 untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data.
+ Ketik angka 1 kembali untuk menetapkan dengan user ID 1
+ Lakukan `python manage.py migrate` kembali untuk mengaplikasikan yang dilakukan pada sebelumnya
<br>

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi. <br>
Untuk menampilkan username nama yang sedang logged in sudah terdapat pada step menghubungkan Item dengan User sebelumnya yaitu persisnya saat tahap mengganti context di dalam `show_main` yaitu  
```
'name': request.user.username,
```
+ Untuk menerapkan cookies seperti last login, pertama-tama kita harus menghubungan data dari cookies terlebih dahulu. Buka berkas `views.py` pada direktori `main` dan tambahkan beberapa import dibawah ini.
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
+ Pada fungsi `login_user`, tambahkan fungsi untuk menambahkan cookie yang bernama `last_login` untuk melihat kapan kali suatu user melakukan login. Caranya adalah dengan mengganti kode yang ada pada blok `if user is not None` menjadi potongan kode dibawah ini.
```
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
+ Pada fungsi `show_main` tambahkan potongan kode `last_login': request.COOKIES['last_login']` ke dalam variable context.
```
context = {
    ...
    'last_login': request.COOKIES['last_login'],
    ...
}
```
+ Ubah fungsi `logout_user` menjadi potongan berikut.
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
+ Buka berkas `main.html` dan tambahkan potongan kode berikut di bawah tombol logout.
```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```



