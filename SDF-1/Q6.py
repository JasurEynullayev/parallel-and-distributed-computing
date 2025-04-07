# 6. Dictionary Məntiqi və update, delete Funksiyaları

# Dictionary — Açarlı dəyərlər toplusu
# Hər bir element: açar: dəyər (key: value) formatındadır.
# {} istifadə olunur.
# Sıralı və dəyişkəndir.
student = {
    "ad": "Zaur",
    "yas": 22,
    "universitet": "BDU"
}

print(student["ad"])         # Zaur
print(student.get("yas"))    # 22


# update() — Dəyəri dəyişmək və ya əlavə etmək
student.update({"yas": 23})  # Mövcud açar varsa, dəyişir
student.update({"fakulte": "Kompüter elmləri"})  # Yeni açar əlavə edir

# Nəticə:
# {'ad': 'Zaur', 'yas': 23, 'universitet': 'BDU', 'fakulte': 'Kompüter elmləri'}


# delete — Element silmək
del student["universitet"]  # Açarı və dəyəri silir

# pop — açara uyğun dəyəri silib qaytarır
yas = student.pop("yas")   # 23


# Əlavə funksiyalar
# keys, values, items
print(student.keys())      # dict_keys(['ad', 'fakulte'])
print(student.values())    # dict_values(['Zaur', 'Kompüter elmləri'])
print(student.items())     # dict_items([('ad', 'Zaur'), ('fakulte', 'Kompüter elmləri')])
