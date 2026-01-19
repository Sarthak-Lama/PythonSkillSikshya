marks = {
    "savita":67,
    "Imtiz":88,
    "Laxman":91,
}

print("Marks doctionary before update : \n",marks)
marks1 = {"sharad":51,
          "Mushtaq":61,
          "Laxman":89
          }

newmarks ={**marks , **marks1}
print("Marks dictionary after update : \n",newmarks)