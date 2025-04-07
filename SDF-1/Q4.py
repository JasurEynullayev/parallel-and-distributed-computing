# 4. List funksiyaları: append(), len(), insert(), remove(), extend()
# Python-da list dəyişkən, indekslənə bilən və istənilən tip element saxlayan obyektlərdir.
my_list = [1, 2, 3]

# append - sonuna əlavə et
my_list.append(4)  # [1, 2, 3, 4]

# insert - istənilən yerə əlavə et
my_list.insert(1, 99)  # [1, 99, 2, 3, 4]

# remove - ilk uyğun elementi sil
my_list.remove(2)  # [1, 99, 3, 4]

# extend - bir neçə elementi əlavə et
my_list.extend([5, 6])  # [1, 99, 3, 4, 5, 6]

# len - uzunluğu
print(len(my_list))  # 6
