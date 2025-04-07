# 5. Tuple və Set Məntiqi və Funksiyaları

# Tuple — Dəyişməz sıra
# Tuple dəyişdirilə bilməyən (immutable) məlumat strukturudur.
# Sıralıdır, indekslənə bilər və təkrarlana bilər.
# Mötərizə ( ) ilə yaradılır.
my_tuple = (1, 2, 3, 4)

# İndeks üzrə müraciət
print(my_tuple[2])        # 3

# Təkrar istifadə
print(my_tuple * 2)       # (1, 2, 3, 4, 1, 2, 3, 4)

# Uzunluq
print(len(my_tuple))      # 4

# Neçə dəfə təkrarlandığını yoxlamaq
print(my_tuple.count(2))  # 1

# Elementin indeksini tapmaq
print(my_tuple.index(3))  # 2

# Əsas üstünlüyü: Tuple dəyişməzdir → yaddaş baxımından daha effektivdir. Məsələn: koordinatlar (x, y) saxlanması üçün idealdır.


# Set — Unikal elementlər toplusu
# Set dəyişkəndir (mutable), lakin sıralı deyil.
# Təkrarlanan elementlər saxlamaz.
# Mötərizə { } ilə və ya set() ilə yaradılır.
my_set = {1, 2, 3, 4}

# Yeni element əlavə etmək
my_set.add(5)
my_set.add(2)  # 2 artıq var, dəyişməyəcək

# Element silmək
my_set.remove(3)         # 3 silinir
my_set.discard(10)       # 10 yoxdursa belə, xəta vermir

# Başqa list və ya set-lə birləşdirmək
my_set.update([6, 7, 8])

# Uzunluq
print(len(my_set))       # 7

# Element mövcuddurmu?
print(4 in my_set)       # True

# Set Əməliyyatları
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))                 # {1, 2, 3, 4, 5}
print(a.intersection(b))          # {3}
print(a.difference(b))            # {1, 2}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}

# Məntiqi İstifadə Sahəsi: Unikal dəyərlər saxlamaq, məsələn:
# İstifadəçi ID-ləri
# Email ünvanları (təkrarsız)
# İki siyahı arasında kəsişmə tapmaq