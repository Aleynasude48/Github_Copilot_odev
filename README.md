# Mystery Module

Basit bir ikinci dereceden denklem kök hesaplayıcısı.

## Açıklama

`mystery_module` yalnızca tek bir fonksiyon içerir: `fn_x(a, b, c)`.
Bu fonksiyon, $ax^2 + bx + c = 0$ denkleminin gerçek köklerini çözer.

## Fonksiyon: fn_x(a, b, c)

### Parametreler:

- **a:** katsayı a
- **b:** katsayı b
- **c:** katsayı c

### Davranış:

1.  Diskriminant hesaplanır: $\Delta = b^2 - 4ac$
2.  Eğer $\Delta < 0$ ise gerçek kök yoktur; fonksiyon `None` döner.
3.  Eğer $\Delta \geq 0$ ise gerçek kökler hesaplanır ve bir **tuple** (demet) olarak döner.

## Kullanım

### Gereksinimler

- Python standard kütüphanesi
- `math` modülü kullanılır, ek bağımlılık yok.

## Notlar

- **a** katsayısı sıfır olmamalıdır.a = 0 durumu birinci dereceden denklem anlamına gelir ve bu fonksiyon için uygun değildir
- Fonksiyon yalnızca **gerçek kökleri** döndürür; karmaşık kökleri ele almaz.
