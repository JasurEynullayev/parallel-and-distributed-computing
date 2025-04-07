# ------------------------------
# 1. Şərhlər (Comments) Python-da
# ------------------------------

# Tək sətirlik şərh:
# Bu bir tək sətirlik şərhdir.

"""
Bu isə
çox sətirli
bir şərhdir (docstring şəklində).
"""

# Eyni zamanda bir neçə sətirlik şərhləri ardıcıl '#' işarələri ilə də yaza bilərik:
# Bu da
# çox sətirli
# bir şərhdir.

# Qeyd: '#' şərhlər üçün, docstring-lər isə funksiyalar, siniflər və modullar üçün izah yazmaqda istifadə olunur.

# ------------------------------
# 2. Giriş (Indentation) qaydaları
# ------------------------------

# Doğru yazım:
if 5 > 2:
    print("Five is greater than two!")

# Səhv yazım (indentation yoxdur):
# if 5 > 2:
# print("Five is greater than two!")

# Qeyd: Python boşluqlardan istifadə edərək blokları müəyyən edir.

# ------------------------------
# 3. Dəyişənlər (Variables)
# ------------------------------

x = 5
y = "John"
print(x)
print(y)

x = 4           # int tipində
print(type(x))
x = "Sally"     # str tipinə çevrildi
print(type(x))
print(x)

# Qeyri-qanuni dəyişən adları:
# 2myvar = "John"      # rəqəmlə başlaya bilməz
# my-var = "John"      # tire istifadə edilə bilməz
# my var = "John"      # boşluq ola bilməz

# ------------------------------
# 4. Birdən çox dəyəri birdən çox dəyişənə mənimsətmək
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# ------------------------------
# 5. Eyni dəyəri bir neçə dəyişənə mənimsətmək
x = y = z = "Orange"
print(x)
print(y)
print(z)

# ------------------------------
# 6. Unpacking (paket açmaq)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# ------------------------------
# 7. print() funksiyası
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)          # Boşluqla ayırır
print(x + y + z)        # Birləşdirir (concatenation)

# ------------------------------
# 8. Dəyişən növlərinin uyğun olmaması (TypeError)
# x = 5
# y = "John"
# print(x + y)  # səhvdir, çünki int və str birləşdirilə bilməz

# ------------------------------
# 9. Qlobal və lokal dəyişənlər
x = "awesome"

def myfunc():
    x = "fantastic"  # lokal dəyişən
    print("Python is " + x)

myfunc()
print("Python is " + x)

# Global dəyişəni funksiya içində dəyişmək:
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)

# ------------------------------
# 10. Tip yoxlama (type()) və çevirmə (casting)

x = 1       # int
y = 2.8     # float
z = 1j      # complex
print(type(x))
print(type(y))
print(type(z))

# Tip çevirmə:
x = float("3")
y = int(2.0)
z = str(3)
print(type(x))
print(type(y))
print(type(z))

# ------------------------------
# 11. Sətirlərlə işləmək

# İndeksləmə:
a = "Hello, World!"
print(a[1])  # 'e'

# Çoxsətirli string:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Uzunluq:
print(len(a))

# Alt stringin mövcudluğunu yoxlamaq:
txt = "The best things in life are free!"
print("free" in txt)
print("free" not in txt)

# Dilimləmə:
b = "Hello, World!"
print(b[2:5])  # 'llo'

# ------------------------------
# 12. if, elif, else

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Qısa sintaksis:
if a > b: print("a is greater than b")
print("A") if a > b else print("B")

# not operatoru:
if not a < b:
    print("a is NOT less than b")

# nested if:
x = 11
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# pass ifadəsi:
if b > a:
    pass

# ------------------------------
# 13. Üzv olub-olmama yoxlaması
list = [1, 2, 3, 4, 5, 6, 7]
a = 4
if a in list:
    print("yes")
else:
    print("no")

# ------------------------------
# 14. while dövrü

# Sadə dövr:
i = 1
while i < 6:
    print(i)
    i += 1

# break:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# continue:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# else ilə while:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# ------------------------------
# 15. for dövrü

for x in "banana":
    print(x)

for x in range(6):
    print(x)

# Dilimləmə nümunəsi:
a = "salam necesen"
print(a[2:4])  # 'la'
