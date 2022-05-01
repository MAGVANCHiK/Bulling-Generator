#Bulling generator
import random
import os
directory_folder = r"%USERPROFILE%%\bullinglogs\log.txt"+".txt"
folder_path = os.path.dirname(r"%%USERPROFILE%%\bullinglogs\log.txt"+".txt") # Путь к папке с файлом
if not os.path.exists(folder_path): #Если пути не существует создаем его
 os.makedirs(folder_path)
file = open(r"%%USERPROFILE%%\bullinglogs\log.txt", 'w')
with open(r"%USERPROFILE%\bullinglogs\log.txt", 'w'):
    file.write("")
kol = input("Количество фраз(Желательно 5-30): ")
kol = int(kol) - 1
isp = 0
while int(kol) >= int(isp):
    RAN = random.randint(0, 51)
    if int(RAN) == 1:
        with open(directory_folder, 'a') as file:
                file.write("Таких, как ты, надо держать в клетке, еблан безмамный. ")
    if int(RAN) == 2:
        with open(directory_folder, 'a') as file:
            file.write("У тебя мозгов нет хуила обоссаный. ")
    if int(RAN) == 3:
        with open(directory_folder, 'a') as file:
            file.write("Мир стал бы лучше без тебя, ты - ЧМО! ")
    if int(RAN) == 4:
        with open(directory_folder, 'a') as file:
            file.write("Блудилище с " + str(random.randint(2, 30))  + " отчимами, а не пойти ли тебе нахуй?! ")
    if int(RAN) == 5:
        with open(directory_folder, 'a') as file:
            file.write("Говномес безмозглый, адекватно говорить умеешь? ")
    if int(RAN) == 6:
        with open(directory_folder, 'a') as file:
            file.write("Гнида подзалупная, мондавошка безмамная, ты что кроме кибербуллинга умеешь? ")
    if int(RAN) == 7:
        with open(directory_folder, 'a') as file:
            file.write("Закрой свой рот ебучий, ублюдок сын ты сучий. ")
    if int(RAN) == 8:
        with open(directory_folder, 'a') as file:
            file.write("Дрочила обоссаный, а может это твоя мать здохла в канаве годик тому назад?! ")
    if int(RAN) == 9:
        with open(directory_folder, 'a') as file:
            file.write("Кретин ты ж обоссаный, губозакаточную машину не хочешь? ")
    if int(RAN) == 10:
        with open(directory_folder, 'a') as file:
            file.write("Мудацкая хуетень обоссаная, ты по фактам отвечать умешь? ")
    if int(RAN) == 11:
        with open(directory_folder, 'a') as file:
            file.write("Ты говоришь слова которые тебе твоя мамаша шалава,написала на бумажке и тебе в ебало засунула! ")
    if int(RAN) == 12:
        with open(directory_folder, 'a') as file:
            file.write("Не забывай что у тебя матери-то нету. ")
    if int(RAN) == 13:
        with open(directory_folder, 'a') as file:
            file.write("Ты только стрелки типичного первоклассника и используешь. ")
    if int(RAN) == 14:
        with open(directory_folder, 'a') as file:
            file.write("Ты-ж ебалай с мусорки выбежал и написал. ")
    if int(RAN) == 15:
        with open(directory_folder, 'a') as file:
            file.write("Походу отчимы отстропонить хотят бедного ((. ")
    if int(RAN) == 16:
        with open(directory_folder, 'a') as file:
            file.write("Ты даун с " + str(random.randint(47, 50)) + " хромосомами, заткнуться сможешь? ")
    if int(RAN) == 17:
        with open(directory_folder, 'a') as file:
            file.write("Как ты не поймёшь что твою мамашу, шалава между прочем,насиловали каждое утро, и что тебе остаётся только сосать огромный чёрный хуй отца! ")
    if int(RAN) == 18:
        with open(directory_folder, 'a') as file:
            file.write("Нет, ну я уже сплю без мамы, ну кроме твоей). ")
    if int(RAN) == 19:
        with open(directory_folder, 'a') as file:
            file.write("Так если я к тебе не лезу, завали свой грёбаный ебальник! ")
    if int(RAN) == 21:
        with open(directory_folder, 'a') as file:
            file.write("Так и хочется тебя пристрелить… ")
    if int(RAN) == 22:
        with open(directory_folder, 'a') as file:
            file.write("А у тебя наверное член короткий, раз язык такой длинный! ")
    if int(RAN) == 23:
        with open(directory_folder, 'a') as file:
            file.write("Если бы ты не был таким тупым, я бы мог и обидеться. ")
    if int(RAN) == 24:
        with open(directory_folder, 'a') as file:
            file.write("Не волнуйся, когда-нибудь ты скажешь что-нибуть смешное. ")
    if int(RAN) == 25:
        with open(directory_folder, 'a') as file:
            file.write("О, вы, кажется, задумались? Это что-то новенькое. ")
    if int(RAN) == 26:
        with open(directory_folder, 'a') as file:
            file.write("Твоим голосом только в толчке и кричать, что занято! ")
    if int(RAN) == 27:
        with open(directory_folder, 'a') as file:
            file.write("Я твою мать в пизду без смазки трахал! ")
    if int(RAN) == 28:
        with open(directory_folder, 'a') as file:
            file.write("Вот ты ПОДОНОК! ")
    if int(RAN) == 29:
        with open(directory_folder, 'a') as file:
            file.write("Вообще советую съебать. Сын Фермера! ")
    if int(RAN) == 30:
        with open(directory_folder, 'a') as file:
            file.write("Ебало завали сын шлюхи, я её в пизду трахал! ")
    if int(RAN) == 31:
        with open(directory_folder, 'a') as file:
            file.write("Тебя в жопу страпонили или как? ")
    if int(RAN) == 32:
        with open(directory_folder, 'a') as file:
            file.write("Пошёл бы ты нахуй хуила безмамный! ")
    if int(RAN) == 33:
        with open(directory_folder, 'a') as file:
            file.write("Съеби в пизду безмамный сын шлюхи! ")
    if int(RAN) == 34:
        with open(directory_folder, 'a') as file:
            file.write("Твою мамку в пизду " + str(random.randint(3, 20)) + " трахали! ")
    if int(RAN) == 35:
        with open(directory_folder, 'a') as file:
            file.write("Соси член сын шлюхи! ")
    if int(RAN) == 36:
        with open(directory_folder, 'a') as file:
            file.write("За себя не стыдно? ")
    if int(RAN) == 37:
        with open(directory_folder, 'a') as file:
            file.write("Ебанутый сбезманый хуила! ")
    if int(RAN) == 38:
        with open(directory_folder, 'a') as file:
            file.write("Твоя мать мой член " + str(random.randint(1, 10)) + " час сосёт! ")
    if int(RAN) == 39:
        with open(directory_folder, 'a') as file:
            file.write("Очко после " + str(random.randint(3, 20)) + "-ого отчима не болит? ")
    if int(RAN) == 40:
        with open(directory_folder, 'a') as file:
            file.write("Попуск ёбаный, съеби пожалуйста! ")
    if int(RAN) == 41:
        with open(directory_folder, 'a') as file:
            file.write("Ноунейм ёбаный счеби нахуй отсюда! ")
    if int(RAN) == 42:
        with open(directory_folder, 'a') as file:
            file.write("Приятно с членом в горле? ")
    if int(RAN) == 43:
        with open(directory_folder, 'a') as file:
            file.write("Отсосать не хочешь? ")
    if int(RAN) == 44:
        with open(directory_folder, 'a') as file:
            file.write("Нахуй пойти не хочешь? ")
    if int(RAN) == 45:
        with open(directory_folder, 'a') as file:
            file.write("Ебало не болит словами раскидываться? ")
    if int(RAN) == 46:
        with open(directory_folder, 'a') as file:
            file.write("Рекорд по количеству членов в жопе побил? ")
    if int(RAN) == 47:
        with open(directory_folder, 'a') as file:
            file.write("У твоей мамки пизда не болит? ")
    if int(RAN) == 48:
        with open(directory_folder, 'a') as file:
            file.write("Ахахахаха, ебать ты попуск! ")
    if int(RAN) == 49:
        with open(directory_folder, 'a') as file:
            file.write("Хуила безмамны! Сын фермера с хуём в жопе! ")
    if int(RAN) == 50:
        with open(directory_folder, 'a') as file:
            file.write("Ахуеть ты еблан! Съеби НАХУЙ! ")
    if int(RAN) == 51:
        with open(directory_folder, 'a') as file:
            file.write("Еблан безмамный! ")
    isp = int(isp) + 1
with open(directory_folder, 'a') as file:
    file.write("Ебать ты попуск!")
    print("by MAGVANCHiK2022, vk: id715385421")
    f = open(directory_folder)
    a = f.read()
    print(a)
print("by MAGVANCHiK2022, vk: id715385421")
