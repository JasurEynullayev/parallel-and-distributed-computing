# PYTHON FUNKSİYALARI VƏ MƏLUMAT TİPLƏRİ

# Python-da iki növ funksiya var:
# - Built-in funksiyalar (hazır funksiyalar)
# - İstifadəçi tərəfindən yaradılmış funksiyalar

# Built-in funksiyalar sətir əməliyyatları, tarix və vaxt əməliyyatları, siyahı manipulyasiyaları və s. üçün istifadə olunur.
# İstifadəçi funksiyaları isə istifadəçinin özü tərəfindən yazılır.

# ------------------------------------------------------------------------

# FUNKSİYA YARATMAQ

def send_data():
    print("successful!")

send_data()
send_data()

# Funksiyalar istənilən qədər çağırıla bilər.

# ------------------------------------------------------------------------

# FUNKSİYAYA ARQUMENT VERİLMƏSİ

def hi(name):
    print("Hello " + name)

hi("Someone")

# Parametrli funksiya: Parametrlərlə məlumat ötürə bilərik.

# ------------------------------------------------------------------------

# İKİ ARQUMENTLİ FUNKSİYA

def sum(x, y):
    print(f"Sum of numbers: {x + y}")

sum(4, 7)

# f-string formatlaması istifadə olunur.

# ------------------------------------------------------------------------

# ORTALAMA HESABLAMA FUNKSİYASI

def meanOfTheNumbers(lst):
    mean = sum(lst) / len(lst)
    print("The mean of the numbers is: {}".format(mean))

meanOfTheNumbers([1, 2, 3, 4])

# ------------------------------------------------------------------------

# STR DƏYƏRLƏRİN BÖYÜK HƏRFƏ ÇEVRİLMƏSİ

def upperCase(metn):
    metn = metn.upper()
    print(metn)

upperCase("salam")

# ------------------------------------------------------------------------

# DEFAULT ARQUMENTLİ FUNKSİYA

def hi(mesaj, name="anonim"):
    print(f"{mesaj} {name}")

hi("Salam")

# Default dəyər verildiyi üçün bir arqumentlə də işləyir.

# ------------------------------------------------------------------------

# VOID (return etməyən) FUNKSİYA

def sumOfNumbers(x, y):
    print(x + y)

result = sumOfNumbers(3, 8)
print(result)  # None

# ------------------------------------------------------------------------

# RETURN İLƏ FUNKSİYA

def sumOfNumbers(x, y):
    return x + y

result = sumOfNumbers(3, 8)
print(result)  # 11

# ------------------------------------------------------------------------

# LİST FUNKSİYAYA VERİLDİKDƏ

def add_element(lst):
    lst.append(4)

my_list = [1, 2, 3]
add_element(my_list)
print(my_list)  # [1, 2, 3, 4]

# ------------------------------------------------------------------------

# LİSTLƏR (Lists)
colors = ["black", "white", "green", "grey", "blue"]
print(type(colors))
print(colors)
print(len(colors))            # uzunluğu
print(colors[2:4])            # 3-cü və 4-cü element

# Əlavə və dəyişikliklər:
colors.append("yellow")       # sona əlavə
colors.insert(0, "grey")      # 0-cı indexə əlavə
colors.remove("black")        # elementi silmək

colors2 = ["white1"]
colors.append(colors2)       # nested list
colors.extend(colors2)       # ayrı-ayrı element kimi əlavə

# Silmək və sıralamaq:
col = ["yellow", "pink", "black", "green"]
col.pop(2)                   # index 2-ni silmək
print(col)

colo = ["a", "b", "c", "d"]
print(sorted(colo))         # sıralanmış nəticə

# Ən kiçik və ən böyük:
numbers = [1, 2, 4, 5, 7, 342]
print(min(numbers))
print(max(numbers))

# Toplama:
print(sum(numbers))

# Siyahı içində dövr:
for i in numbers:
    print(i)

# Join metodu:
string = " ".join(colors)
print(string)

# ------------------------------------------------------------------------

# TUPLES
cl = ("Sari", "Qirmizi", "Boz")
for i in cl:
    print(i)

print(min(cl))

# Tuple-lar dəyişdirilə bilməz.
# append(), remove() və insert() işləmir.

# ------------------------------------------------------------------------

# SET-lər
mySet = {"sari", "qara"}
mySet.add("Ag")
print(mySet)

# Element silmək:
mySet.discard("boz")  # təhlükəsiz silmə (error atmır)

# Set əməliyyatları:
set1 = {"a", "b", "c"}
set2 = {"d", "e"}
print(set2.intersection(set1))   # kəsişmə
print(set2.union(set1))          # birləşmə
print(set2.difference(set1))     # fərq

# ------------------------------------------------------------------------

# DICTIONARY
person = {"ad": "Someone", "yas": 25}
print(person["ad"])

person.update({"ad": "human", "yas": 19})
person["id"] = 12345
print(person)

del person["ad"]
print(person)

print(person.values())
print(person.get("yas"))
