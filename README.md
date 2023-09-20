# tugas3-PBP 
Nama  : Clara Sista Widhiastuti <br/>
NPM   : 2206825782 <br/>
Kelas : PBP-E <br/>

## Perbedaan form POST dan form GET

| **Pembeda** | ```POST``` | ```GET``` |
|:--:|--|--|
|**Fungsi**|Mengirimkan data ke server|Mengambil data dari server|
|**History**|Isi atau nilai dari form tidak ditampilkan di URL|Isi atau nilai dari form dapat dilihat langsung pada URL
|**Kegunaan**|Pengiriman data tertutup dan data bersifat sensitif (*username* dan *password*)|Menampilkan id pada penggunaan database

## Perbedaan XML, JSON, HTML dalam pengiriman data
| ```XML``` | ```JSON``` |```HTML```
|--|--|--|
|Didesain untuk mendeskripsikan serta mentransfer data. Data harus berupa string dan tidak mendukung array|Didesain untuk mendeskripsikan serta mentransfer data menggunakan bahasa yang mudah dimengerti. Dapat mengakses array.|Didesain untuk menampilkan data dan bagaimana penampakan data tersebut.|
|case sensitive|case sensitive|case nsensitive
|Menggunakan tag|Menggunakan pasangan key dan value|Menggunakan tag|

## JSON sering digunakan dalam pertukaran data antara aplikasi web modern
Alasan JSON sering digunakan untuk pertukaran data adalah:
1.  Ukuran file JSON lebih kecil dibanding format lain seperti XML
2. JSON memiliki struktur kode yang sederhana sehingga mudah dibaca serta dimengerti oleh manusia.
3. Dapat digunakan dengan berbagai jenis bahasa, Hal tersebut membuatnya menjadi lebih fleksible. 

## Implementasi data delivery
1. Membuat berkas baru dengan nama ```forms.py``` pada direktori ```main``` kemudian tambahkan kode dibawah ini
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "amount", "description"]
```
2. pada folder ```main``` buka berkas ```views.py``` tambahkan import dan fungsi baru create_ product untuk menerim data seperti berikut
```
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
```
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
3. Agar kita dapat menampilkan/mengembalikan data maka perlu mengubah fungsi ```show_main``` pada berkas ```views.py``` seperti kode dibawah ini
```
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Clara Sista Widhiastuti', 
        'class': 'PBP E', 
        'products': products
    }

    return render(request, "main.html", context)
```
4. Buka direktori ```main/templates```, kemudian buat berkas baru dengan nama ```create_product.html``` isi dengan kode dibawah ini
```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
5. menampilkan ```data``` ke dalam bentuk table dan menambahkan tombol ```Add New Product``` dengan menambahkan kode berikut pada berkas ```main.html```
```
...
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>

{% endblock content %}
```
---
membuat fungsi views JSON dan XML pada berkas ```views.py``` di direktori ```main```
1. menambahkan import ```HttpResponse``` dan ```Serializer```
```
from django.http import HttpResponse
from django.core import serializers
```
2. membuat variabel yang dapat menyimpan hasil query dari semua data dalam masing masing fungsi 
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
3. Untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON maka kita perlu membuat fungsi ```show_xml_id``` dan ```show_json_by_id```
```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
---
Routing URL
1. pada direktori ```main``` buka berkas ```urls.py``` tambahkan import fungsi XML dan JSON
```
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
```
2. Tambahkan path url ke dalam ```urlpatterns```
```
...
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
```
## Screenshot Postman
#### HTML
![HTML](image\html.png)
#### JSON
![JSON](image\json.png)
#### JSON_ID
![JSON_ID](image\json_id.png)
#### XML
![XML](image\xml.png)
#### XML_ID
![XML_ID](image\xml_id.png)

<details>
<summary> <b> Tugas 2 </b> </summary>
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
### MVVM (Model-View-ViewModel)
  Model berisi data dan logika bisnis<br/>
  View menangani tampilan<br/>
  ViewModel merupakan penghubung antara model dan view<br/>
Perbedaan dari ketinganya adalah bagaimana cara menghubungkan antar komponen. Pada MVC, controller berperan sebagai penghubung model dan view. Pada MVT, template berperan sebagai penghubung model dan view. Sedangkan pada MVVM, ViewModel yang berperan sebagai penghubung antara model dan view.

