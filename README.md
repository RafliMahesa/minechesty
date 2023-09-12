1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   
- [x] Membuat sebuah proyek Django baru. <br>

+ Membuat direktori minechesty
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
