# 3. if, elif, else, nested if
# Python-da şərtli operatorlar ilə qərar vermə strukturunu qururuq.

# Əsas struktur
yas = 20

if yas < 18:
    print("Uşaqsan")
elif yas == 18:
    print("Tam yetkin")
else:
    print("Böyüksən")

# Nested if (iç-içə if)
x = 10
y = 20

if x < 15:
    if y < 25:
        print("Hər ikisi doğrudur")
