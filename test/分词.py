file=open('D:\各种数据集\专利数据\city文本.txt',mode='r',encoding='UTF-8')
admin=[]
contents = file.readlines()
print(contents)
for msg in contents:
    msg = msg.strip('\n')
    adm = msg.split('~')
    admin.append(adm)
file.close()
print(admin)