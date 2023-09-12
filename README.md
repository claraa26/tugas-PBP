# tugas2-PBP 
Nama  : Clara Sista Widhiastuti <br/>
NPM   : 2206825782 <br/>
Kelas : PBP-E <br/>

## Proses pembuatan app django
1. Membuat Direktori Repository<br/>
   Membuat direktori baru yaitu **tugas_PBP**, kemudian pada github membuat repository baru yang judulnya sama dengan direktori
   
2. Mengaktifkan virtual evironment<br/>
   Pengaktifan virtual evironment dilakukan agar package yang digunakan tetap terisolasi sehingga bertabarakan dengan pengaturan lainnya. <br/> Kita perlu membuat virtual         environment dengan menjalankan perintah ```python -m venv env```,<br/>kemudian diaktifkan dengan menjalankan perintah ```env\Scripts\activate.bat```. Menambahkan modul yang yang diperlukan pada file ```requirenments.txt```<br/> kemudian menjalankan perintah ```pip install -r requirements.txt```

3. Membuat proyek django<br/>
   buat proyek djago dengan menjalankan perintah ```django-admin startproject tugas_PBP .```<br/> Tambahkan ```*``` pada ```ALLOWED_HOST``` di ```settings.py``` digunakan agar semua host dapat mengakses sehingga aplikasi dapat diakses luas.<br/> Pada windows untuk menjalankan server django dapat menggunakan python ```manage.py runserver```<br/>

4. Mengunggah proyek ke github<br/>
   membuat direktori menjadi repositori git, dengan cara menjalankan perintah ```git init```, kemudian ```git branch -M main```, dan ```git remote add origin https://github.com/claraa26/tugas-PBP.git```<br/>
   menambahkan file ```.gitignore```<br/>
   jangan lupa melakukan ```add```, ```commit```, dan ```push```

5. Membuat aplikasi (main) <br/>
   untuk membuat aplikasi maka perlu menjalankan perintah ```python manage.py startapp main```<br/>
   mendaftarkan aplikasi (main) pada proyek, dengan menambahkan aplikasi pada bagian ```INSTALLED_APPS``` di file ```settings.py```<br/>

6. Membuat templates dasar <br/>
   Membuat file main.html pada direktori templates yang berada di dalam direktori aplikasi (main) yang berisi
   ```
   <h1>Bimble-Online Page</h1>
   
   <h5>Name: </h5>
   <p>{{ name }}</p>
   <h5>Class: </h5>
   <p>{{ class }}</p>
   <h5>Slot Available: </h5>
   <p>{{ slot available }}</p>
   <h5>Description: </h5>
   <p>{{ description }}</p>
   ```
   Membuat ```models.py``` kemudian melakukan migrasi. Hal tersebut merupakan cara django melacak perubahan pada model basis data. 
   untuk dapat membuat migrasi model perlu dijalankan perintah ```python manage.py makemigrations```<br/>
   Kemudian menerapkan migrasi model dengan perintah ```python manage.py migrate```

7. Membuat fungsi view (show_main)<br/>
   Dilakukan perintah ```from django.shortcuts import render``` agar yang berada pada file template ```main.html``` dapat terhubuh pada view.<br/>
   Menambahkan fungsi show main dengan context yang ingin ditampilkan
```
from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Clara',
        'class': 'math',
        'slot available': '15',
        'description': 'math class available for 15 person'

    }

    return render(request, "main.html", context)
```

8. Konfigurasi routing urls<br/>
   file urls.py pada main berisi
   ```
   from django.urls import path
   from main.views import show_main

   app_name = 'main'

   urlpatterns = [
      path('', show_main, name='show_main'),
   ]
   ```
   show main diambil dari modul main.views yang mana merupakan tampilan ketika urls diakses<br/>
   menghubungkan urls.py proyek dengan main dengan menambahkan
```
   urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
  jalankan proyek django dengan perintah ```python manage.py runserver```

## Bagan Request Client
![BAGAN](https://github.com/claraa26/tugas-PBP/blob/master/bagan_request_client%20(1).png)

## Penggunaan Virtual Environment Pada Django
Pada djanggo penggunaan virtual environment sangatlah berguna, karena pengguna dapat menggunakan django dengan dependencies tertentu secara lokal tanpa mempengaruhi instalasi globalnya. Selain itu, dalam jangka panjang penggunaan virtual environment dapat mepermudah pengembangan apliaksi web django. Tentu saja kita dapat menggunkan django tanpa virtual environment, namun hal tersebut tidak dianjurkan karena dapat menyebabkan masalah pada package dan dependencies

## Perbedaan MVC, MVT, MVVM
### MVC (Model-View-Controller)
  Model berisikan data serta logika (database)<br/>
  View berguna untuk menangani tampilan <br/>
  Controler menghubungkan antara model dan view <br/>
### MVT (Model-View-Template)
  Model merupakan komponen yang bertanggungjawab dalam mengatur dan mengola data aplikasi<br/>
  View komponen yang menangani logika presentasi dalam konsep MVT<br/>
  Template merupakan komponen yang berfungsi untuk mengatur tampilan pengguna<br/>
## MVVM (Model-View-ViewModel)
  Model berisi data dan logika bisnis<br/>
  View menangani tampilan<br/>
  ViewModel merupakan penghubung antara model dan view<br/>
Perbedaan dari ketinganya adalah bagaimana cara menghubungkan antar komponen. Pada MVC, controller berperan sebagai penghubung model dan view. Pada MVT, template berperan sebagai penghubung model dan view. Sedangkan pada MVVM, ViewModel yang berperan sebagai penghubung antara model dan view.
   
>>>>>>> master
