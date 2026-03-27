# Mystery Module

Basit bir ikinci dereceden denklem kök hesaplayıcısı.

## Açıklama

`mystery_module` yalnızca tek bir fonksiyon içerir: `fn_x(a, b, c)`.
Bu fonksiyon, $ax^2 + bx + c = 0$ denkleminin gerçek köklerini çözer.

## Fonksiyon: fn_x(a, b, c)

### Parametreler:

- **a:** Katsayı a
- **b:** Katsayı b
- **c:** Katsayı c

### Davranış:

1.  Diskriminant hesaplanır: $d = b^2 - 4ac$
2.  Eğer $d < 0$ ise gerçek kök yoktur; fonksiyon `None` döner.
3.  Eğer $d \geq 0$ ise gerçek kökler şu formülle hesaplanır:
    - $x_1 = (-b + \sqrt{d}) / (2a)$
    - $x_2 = (-b - \sqrt{d}) / (2a)$
4.  Bu iki kök bir demet (**tuple**) olarak döner.

## Kullanım

### Gereksinimler

- Python standart kütüphanesi.
- `math` modülü kullanılır, ek bağımlılık yoktur.

## Notlar

- **a** sıfır olmamalıdır; $a = 0$ durumu birinci dereceden denklem anlamına gelir ve bu fonksiyon için uygun değildir.
- Fonksiyon yalnızca gerçek kökleri döndürür; karmaşık (complex) kökleri ele almaz.
