print("Введите 0 для выхода")
try:
    while True:
# Минимальная 5$, но это только лишь за подключение к облаку, без виртуального сервера. А с около 50$ за проект / полный узел | CPS cost
        connectivityCost = 25
        tps = int(input("\nТекущая пропускная способность сети, tps: "))
# Если tps = 0, сеть не работает
        if tps == 0: break
# Показатель 100 - 250 tps вполне вероятен на старте
        if tps <= 250:
            f = open('./pioneers.txt')
            print(f.read())
# Показатель, к которому стоит стремиться в 2020 году.
        elif tps < 1000:
                f = open('./kusama-stage.txt')
                print(f.read())
# Как думаете доберёмся свыше 1к в секунду транзакций в парачейн? А если объединить две или три сети?
        elif tps >= 1000:
                f = open('./tokyo-lockers.txt')
                print(f.read())
# График работы и допустимое время ожидания исполнения являются входными параметрами, характеризующими пользовательскую часть сети
        print("Пожалуйста укажите пользовательские требования к сети Робономика.")
        latency = int(input("\nС какой задержкой устройства будут готовы работать, сек: "))
        workHours = int(input("Сколько часов в день устройство будет работать, ч: "))
# Пользователю будет стоить дешевле, а сеть будет получать меньше транзакций, но делать на первой фазе придётся так
        subscription = connectivityCost/24*workHours
        print("\nСтоимость вашего подключения составит: "+ "%.2f" % (subscription), "$")
# Рассчитываем максимальное количество устройств с пониманием, что block time для пользователей это latency
        cpsMax = latency*tps
        print("Максимальное количество устройств в сети Робономика составит: ", (cpsMax))
 # Доходность в прямой зависимости от tps и стоимости connectivity и обратно зависима от требования по задержке исполнения транзакции
        revenue = tps*connectivityCost*latency
        print("Максимальная доходность сети провайдеров составит: ", (revenue), "$ / месяц")
 # Мы можем определять размер пула валидаторов парачейна думая о средней доходности для каждого из них.
 # Например 1к $ в месяц за работу на провайдера мне кажется уже не плохо.
        providersPool = int(tps*connectivityCost*latency/1000)
        print("Рекомендуемое количество провайдеров сети: ",(providersPool))
except:
    print("Не чуди!")
