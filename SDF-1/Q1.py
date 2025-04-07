# 1. Python-da şərhlər, indentation və məlumat tipləri

# 1.1 Şərhlər (Comments)
# Şərhlər proqram kodunda izah yazmaq, digər proqramçılara məlumat ötürmək və ya kodun bəzi hissələrini deaktiv etmək üçün istifadə olunur. Python-da # işarəsi ilə yazılır.
# Bir sətrlik şərh
# Bu bir sadə şərhdir
print("Salam")  # Bu da bir şərhdir

# Çoxsətrli şərh (comment bloqu)
# Python-da formal çoxsətrli şərh yoxdur, lakin üç dırnaqla (''' və ya """) yazılmış mətnlər dokumentasiya və qeyri-rəsmi çoxsətrli şərh kimi istifadə edilə bilər.
"""
Bu funksiyanın məqsədi istifadəçini salamlamaqdır.
Parametr: ad
"""
def salamla(ad):
    print(f"Salam {ad}")


# 1.2 Indentation (Boşluqla düzmə qaydası)
# Python digər dillərdən fərqli olaraq {} istifadə etmir. Bloklar 4 boşluq (və ya tab) ilə müəyyən olunur. Boşluq səhvləri sintaksis xətası verir.
# Düzgün boşluq
if True:
    print("Bu doğrudur")
    print("Bu da həmin blokda")

# Səhv boşluq
# if True:
# print("Xəta")  
# SyntaxError: expected an indented block
# Python standartı: 4 boşluq istifadə olunur. Bu, oxunaqlılığı artırır və kod səhvlərinin qarşısını alır.


# 1.3 Məlumat Tipləri (Data Types)
# Python-da dynamic typing var. Yəni dəyişənin tipini əvvəlcədən təyin etməyə ehtiyac yoxdur.

# Integer
a = 10

# Float
b = 3.14

# String
c = "Salam dünya"

# Boolean
d = True  # və ya False

# List
e = [1, 2, 3]

# Tuple
f = (4, 5, 6)

# Dictionary
g = {"ad": "Ali", "yas": 25}

# Set
h = {1, 2, 3}

print(type(a))  
# <class 'int'>