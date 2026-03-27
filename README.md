mystery_module
Basit bir ikinci dereceden denklem kök hesaplayıcısı.

Açıklama
mystery_module yalnızca tek bir fonksiyon içerir:

fn_x(a, b, c)
Bu fonksiyon, ax^2 + bx + c = 0 denkleminin gerçek köklerini çözer.

Fonksiyon
fn_x(a, b, c)
Parametreler:
a: katsayı a
b: katsayı b
c: katsayı c
Davranış:
d = b**2 - 4*a*c hesaplanır.
d < 0 ise gerçek kök yok; fonksiyon None döner.
d >= 0 ise gerçek kökler:
(-b + sqrt(d)) / (2*a)
(-b - sqrt(d)) / (2*a)
Bu iki kök bir demet (tuple) olarak döner.
Kullanım
Gereksinimler
Python standard kütüphanesi
math modülü kullanılır, ek bağımlılık yok
Notlar
a sıfır olmamalıdır; a = 0 durumu birinci dereceden denklem anlamına gelir ve bu fonksiyon için uygun değildir.
Fonksiyon yalnızca gerçek kökleri döndürür; karmaşık kökleri ele almaz.
