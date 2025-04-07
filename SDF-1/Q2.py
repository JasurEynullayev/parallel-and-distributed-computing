# 2. print() funksiyası və scope

# 2.1 print() funksiyası
# Bu funksiya konsola məlumat çıxarmaq üçün istifadə olunur.
# Sadə istifadə
print("Salam Dünya")

# Birdən çox dəyişən çıxarmaq
ad = "Ali"
yas = 20
print("Ad:", ad, "Yaş:", yas)

# f-string ilə formatlı çıxış
print(f"{ad} adlı şəxsin yaşı {yas}-dır.")


# 2.2 Scope (Görünürlük sahəsi)
# Scope dəyişənin harada yaradıldığına görə onun əlçatan olub-olmamasıdır.


# Global və Local Scope
x = 100  # Global dəyişən

def func():
    y = 10  # Local dəyişən
    print("x =", x)  # Global görünür
    print("y =", y)  # Local görünür

func()
# print(y)  # Xəta: 'y' funksiyadan kənarda yoxdur


# Local dəyişən global-a mane olmur
x = 50

def func():
    x = 10  # Local dəyişən, global-a təsir etmir
    print("Local x:", x)

func()
print("Global x:", x)


# global açarı ilə dəyişiklik etmək
x = 5

def change_global():
    global x
    x = 100

change_global()
print(x)  # 100




