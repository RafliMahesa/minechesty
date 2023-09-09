1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment (lingkungan virtual) adalah cara untuk membuat suatu "ruang kerja" yang terisolasi di komputer kita pada proyek perangkat lunak yang kita kerjakan. Setiap "ruang kerja" mungkin memiliki versi Python berbeda dengan yang diperlukan untuk masing-masing proyek. Selain itu karena berbagai proyek memiliki package dan dependencies yang berbeda-beda, maka dengan penggunaan virtual environment akan ada sekat yang dapat mencegahnya bertabrakan/bentrok.

Meskipun kita tetap bisa membuat aplikasi web berbasis Django tanpa virtual environment, namun penggunaan virtual environment akan lebih baik dan efektif. Dengan virtual environment, kita seperti memiliki "ruang kerja" yang terisolasi satu sama lain untuk mencegah bentroknya package serta dependencies yang berbeda versi dengan yang sudah ada di perangkat kita. Dengan demikian maka dalam pengembangan web berbasis Django lebih efektif jika menggunakan virtual environment.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
