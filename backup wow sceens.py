import os
source = ['"D:\\Games\\World of Warcraft\\_classic_\\Screenshots" ']
cpt = sum([len(files) for r, d, files in os.walk("D:\\Games\\World of Warcraft\\_classic_\\Screenshots")])
target_dir = 'C:\\Users\\bobri\\YandexDisk'
target = target_dir + os.sep + 'screens' + '.zip'
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
    print('Было сохранено', cpt, 'скриншотов')
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
input()
