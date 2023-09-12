1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [x] Membuat sebuah proyek Django baru.
      * Membuat direktori
      * Di dalam direktori tersebut, buka command prompt (Windows) atau terminal shell (Unix) lalu buat virtual environment dengan perintah "python -m venv env"
      * Mengaktifkan virtual environment dengan perintah "env\Scripts\activate.bat"
      * Pada direktori yang sama buat requirements.txt dan tambahkan beberapa dependencies
      * Pasang dependencies dengan perintah "pip install -r requirements.txt"
      * Buat proyek Django bernama minechesty dengan perintah "django-admin startproject minechesty ."
      * Tambahkan * pada ALLOWED_HOSTS di settings.py untuk keperluan deployment
        ...
        ALLOWED_HOSTS = ["*"]
        ...
      * Menguji apakah proyek minechesty berhasil dibuat dengan perintah "python manage.py runserver"
      * Buka http://localhost:8000 pada web yang biasa dipakai untuk melihat animasi roket sebagai tanda aplikasi Django berhasil dibuat.
      * Untuk menghentikan server tekan Ctrl+C (Windows/Linux)
      * Tambahkan Berkas .gitignore yang berisi sesuai pada tutorial sehingga Repositori Git tau mana berkas-berkas atau direktori-direktori yang diabaikan
- [x] Membuat aplikasi dengan nama "main" pada proyek minechesty.
      * Membuat aplikasi "main" dengan perintah "python manage.py startapp main"
      * Memasukkan aplikasi main ke dalam proyek dengan cara membuat settings.py pada direktori proyek minechesty lalu memasukkan "main" ke dalam variable INSTALLED_APPS
      INSTALLED_APPS = [
          ...,
          'main',
          ...
      ]
      




2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment (lingkungan virtual) adalah cara untuk membuat suatu "ruang kerja" yang terisolasi di komputer kita pada proyek perangkat lunak yang kita kerjakan. Setiap "ruang kerja" mungkin memiliki versi Python berbeda dengan yang diperlukan untuk masing-masing proyek. Selain itu karena berbagai proyek memiliki package dan dependencies yang berbeda-beda, maka dengan penggunaan virtual environment akan ada sekat yang dapat mencegahnya bertabrakan/bentrok.

Meskipun kita tetap bisa membuat aplikasi web berbasis Django tanpa virtual environment, namun penggunaan virtual environment akan lebih baik dan efektif. Dengan virtual environment, kita seperti memiliki "ruang kerja" yang terisolasi satu sama lain untuk mencegah bentroknya package serta dependencies yang berbeda versi dengan yang sudah ada di perangkat kita. Dengan demikian maka dalam pengembangan web berbasis Django lebih efektif jika menggunakan virtual environment.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

Model-View-Controller (MVC), Model-View-ViewModel (MVVM), dan Model-View-Template (MVT) merupakan pola desain arsitektur yang memisahkan aplikasi menjadi tiga komponen utama yang saling berhubungan, yaitu model, view, dan controller atau viewModel atau template. 

a. MVC (Model-View-Controller)
MVC adalah pola desain arsitektur yang membagi aplikasi menjadi 3 bagian yaitu: model, view, dan controller.
- Model bertanggung jawab untuk mengatur dan mengelola data dari aplikasi.
- View merupakan komponen yang menangani logika presentasi dalam konsep MVT. View bertanggung jawab untuk mengatur tampilan dan mengambil data dari model untuk disajikan kepada pengguna
- Controller berperan dalam menerima masukan dari pengguna, mengatur komunikasi antara Model (data dan logika bisnis) dengan View (antarmuka pengguna), serta melakukan pemrosesan masukan tersebut untuk menentukan tindakan yang perlu diambil terkait data Model dan tampilan View.

b. MVT (Model-View-Template)
MVT adalah pola yang mirip dengan MVC, tetapi controller digantikan dengan Template. MVT biasanya digunakan dalam pengembangan web dengan Django web framework.
- Model bertanggung jawab untuk mengatur dan mengelola data dari aplikasi.
- View merupakan komponen yang menangani logika presentasi dalam konsep MVT. View bertanggung jawab untuk mengatur tampilan dan mengambil data dari model untuk disajikan kepada pengguna
- Template adalah komponen yang berfungsi untuk mengatur tampilan atau antarmuka pengguna. Template digunakan untuk merancang tampilan HTML dan menampilkan data dari model melalui view.

c. MVVM (Model-View-ViewModel)
MVVM adalah varian modern dari MVC yang biasa digunakan untuk mengembangkan aplikasi web yang dapat digunakan kembali dan mudah diuji.
- Model bertanggung jawab untuk mengatur dan mengelola data dari aplikasi.
- View: bertanggung jawab untuk tampilan
- ViewModel: Bertugas untuk menghubungkan Model dan View. ViewModel tidak memiliki referensi ke View dan View tidak perlu menunggu proses pada ViewModel. ViewModel melakukan observe terhadap Model, sehingga jika ada perubahan di Model, ViewModel akan tahu

Perbedaan utama antara ketiga pola ini terletak pada bagaimana mereka mengelola komunikasi antara Model dan View. 
* Dalam MVC, Controller bertanggung jawab untuk mengelola komunikasi antara Model dan View menggunakan peristiwa. 
* Dalam MVVM, kerangka kerja melakukan semua pengangkatan berat menggunakan fitur yang disebut data pengikatan data. ViewModel di MVVM membantu menjaga tampilan terpisah dari model, dan pada saat yang sama, bertindak sebagai pengontrol untuk memfasilitasi komunikasi antara tampilan dan komponen model. 
* Dalam MVT, Template bertugas untuk mengurus bagaimana halaman/halaman web ditampilkan di browser.
