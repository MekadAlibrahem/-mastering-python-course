# # التكليف 01

#     قم بإنشاء List تحتوي على الأرقام التالية 1, 2, 3, 3, 4, 5, 1
#     قم بعمل متغير باسم unique_list ثم قم بتخزين القيم المميزة فقط من ال List السابقة.
#     في السطر الأول قم بطباعة محتوى unique_list وتأكد أنها تحتوي على الأرقام المميزة فقط
#     في السطر الثاني قم بطباعة نوع unique_list وتأكد أن نوع البيانات هو list
#     في السطر الثالث قم بطباعة ال unique_list بدون العنصر الأخير

# my_list = [1, 2, 3, 3, 4, 5, 1]
# # Needed Output

# # 1, 2, 3, 4, 5
# # <class 'list'>
# # 1, 2, 3, 4
# ===============================


my_list = [1, 2, 3, 3, 4, 5, 1]

unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
print(unique_list[:-1])