from telebot import types
import telebot

bot = telebot.TeleBot("1805766159:AAGEpPxX54DAj2Nhe-fHNpKLLaW6cr9vy0A")


@bot.message_handler(commands=['start', 'back'])
def send_echo(message):
    markup = types.ReplyKeyboardMarkup(True, True)
    button = types.KeyboardButton("Что такое Namba One?")
    button2 = types.KeyboardButton("Часто задаваемые вопросы")
    markup.add(button, button2)
    b = open("12.png", 'rb')
    bot.send_photo(message.chat.id, b)
    bot.send_message(message.chat.id, "Выберите кнопку:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def weather(message):
    if message.text == 'Что такое Namba One?':
        instruction = open("N1.png", 'rb')
        bot.send_photo(message.chat.id, instruction)
    elif message.text == 'Часто задаваемые вопросы':
        markup = types.ReplyKeyboardMarkup(True, row_width=3)
        btn4 = types.KeyboardButton("Функционал Namba One")
        btn5 = types.KeyboardButton("Пополнение/Вывод денег")
        btn6 = types.KeyboardButton("Как привязать карту")
        btn7 = types.KeyboardButton("QR-код")
        btn8 = types.KeyboardButton("Идентификация")
        btn12 = types.KeyboardButton("Лимиты")
        btn10 = types.KeyboardButton("Кэшбэк")
        btn11 = types.KeyboardButton("Сервисы")
        btn12 = types.KeyboardButton("/back")
        btn9 = types.KeyboardButton("Безопасность")
        markup.add(btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
        bot.send_message(message.from_user.id, 'Выберите кнопку', reply_markup=markup)
        bot.register_next_step_handler(message, WorldNews)
        bot.register_next_step_handler(message, WorldNews2)
        bot.register_next_step_handler(message, WorldNews3)
        bot.register_next_step_handler(message, WorldNews4)
        bot.register_next_step_handler(message, WorldNews5)
        bot.register_next_step_handler(message, WorldNews6)
        bot.register_next_step_handler(message, WorldNews7)
        bot.register_next_step_handler(message, WorldNews8)
        bot.register_next_step_handler(message, WorldNews9)


@bot.message_handler(content_types=['text'])
def WorldNews(message):
    if message.text == 'Функционал Namba One':
        bot.send_message(message.from_user.id, 'Электронный кошелек Namba One\n\nС помощью счета Namba One можно оплачивать за все товары и услуги в приложении Namba One и переводить деньги. Счет встроен в мобильное приложение Namba One.')
        bot.send_message(message.from_user.id, 'Какие способы оплаты есть в Namba One?\n\n1. Оплата с помощью счета Namba One \n\n2. Оплата с помощью банковских карт VISA, Mastercard и Элкарт. Принимаются карты любых банков. При переводах,'
                                               'оплате, пополнении или вывода денег вы можете использовать любой из способов переводов.')
        bot.send_message(message.from_user.id, 'Что означают статусы Начальный, Продвинутый и Профи?'
                                               '\n\nЭти статусы используются для определения вашего уровня идентификации.'
                                               '\nЕсли у вас Начальный статус - значит вы просто зарегистрированный пользователь.'
                                               '\nЕсли у вас Продвинутый статус - значит вы прошли онлайн идентификацию.'
                                               '\nЕсли у вас Профи статус - значит вы прошли полную идентификацию в Банке.')
        bot.register_next_step_handler(message, WorldNews2)
        bot.register_next_step_handler(message, WorldNews3)
        bot.register_next_step_handler(message, WorldNews4)
        bot.register_next_step_handler(message, WorldNews5)
        bot.register_next_step_handler(message, WorldNews6)
        bot.register_next_step_handler(message, WorldNews7)
        bot.register_next_step_handler(message, WorldNews8)
        bot.register_next_step_handler(message, WorldNews9)


@bot.message_handler(content_types=['text'])
def WorldNews2(message):
    if message.text == "Пополнение/Вывод денег":
        bot.send_message(message.from_user.id, 'Пополнение денег Namba One\n\n1. Через банковскую карту Visa, MasterCard, Элкарт в '
                                               'приложении Namba One. Для этого вам необходимо перейти по функции \n“Пополнить” '
                                               'и перевести на счет Namba One.\n\n2. Пополнить счет в электронных кошельках Элсом, Баланс '
                                               'и Мбанк.Для этого вам необходимо войти в один из кошельков и перейти в раздел “Электронные кошельки”. '
                                               'Далее ввести номер телефона и сумму перевода.\n\n3. Пополнить счет в терминалах QuickPay, '
                                               'Касса24, Pay24, Оной, О!Деньги, Megapay, Умай. Для этого вам необходимо перейти в раздел \n“Электронные кошельки” '
                                               'в одном из терминалов. Далее ввести номер телефона и сумму перевода.\n\n4. Пополнить счет в '
                                               'филиалах Коммерческого Банка Кыргызстан. Подойдите к специалистам по обслуживанию клиентов, вам подскажут '
                                               'как пополнить счет в банке.')
        bot.send_message(message.from_user.id, 'Вывод денег Namba One?\n\n1. Вывод денег в филиалах Коммерческого Банка Кыргызстан.'
                                               'Подойдите к специалистам по обслуживанию клиентов, вам подскажут как пополнить '
                                               'кошелек в банке.\n\n2. Вывод на электронные кошельки Элсом, Баланс и Мбанк. '
                                               'Вы можете вывести деньги на электронные кошельки Элсом, МБанк или Баланс с помощью '
                                               'функции “Оплатить услуги”, далее перейдите в раздел \n“Электронные кошельки”, введите номер телефона получателя и сумму перевода.'
                                               '\n\n3. Вывод денег на банковские карты Visa, MasterCard, Элкарт в приложении Namba One.'
                                               '\nЕсли вы хотите совершить вывод на банковскую карту, то вам необходимо перейти по функции \n“Вывод” на главной '
                                               'странице и выбрать карту на который будет осуществляться перевод и введите сумму перевода.')
        bot.register_next_step_handler(message, WorldNews)
        bot.register_next_step_handler(message, WorldNews3)
        bot.register_next_step_handler(message, WorldNews4)
        bot.register_next_step_handler(message, WorldNews5)
        bot.register_next_step_handler(message, WorldNews6)
        bot.register_next_step_handler(message, WorldNews7)
        bot.register_next_step_handler(message, WorldNews8)
        bot.register_next_step_handler(message, WorldNews9)

@bot.message_handler(content_types=['text'])
def WorldNews3(message):
    if message.text == "Как привязать карту":
        bot.send_message(message.from_user.id, 'Для привязки банковской карты, вам необходимо:'
                                               '\n\n1. Перейти в раздел “Кошелек”'
                                               '\n2. В данном разделе вы увидите функцию “Добавить карту”, \nнажмите на нее.'
                                               '\n3. Выберите платежную систему своей банковской карты: \nVisa, MasterCard, Элкарт'
                                               '\n4. Заполните все поля с карты, которую вы хотите привязать'
                                               '\n5. Дождитесь ответа.')
        bot.send_message(message.from_user.id, 'Как перевести деньги?'
                                               '\n\nПервый способ: '
                                               '\n\nНажмите на кнопку “Перевести” на главном экране, укажите реквизиты получателя и сумму.'
                                               '\n\nВторой способ: \n\nВыберите “Оплатить” в нижнем меню, нажмите через кнопку “Перевести”, '
                                               'отсканируйте QR-код получателя и введите сумму.')
        bot.register_next_step_handler(message, WorldNews)
        bot.register_next_step_handler(message, WorldNews2)
        bot.register_next_step_handler(message, WorldNews4)
        bot.register_next_step_handler(message, WorldNews5)
        bot.register_next_step_handler(message, WorldNews6)
        bot.register_next_step_handler(message, WorldNews7)
        bot.register_next_step_handler(message, WorldNews8)
        bot.register_next_step_handler(message, WorldNews9)

@bot.message_handler(content_types=['text'])
def WorldNews4(message):
    if message.text == "Сервисы":
        bot.send_message(message.from_user.id, 'Что такое сервисы?'
                                               '\n\nСервисы - это быстрый доступ к услугам доставки, такси, '
                                               'маркетплейса, а также к государственным и коммунальным услугам.'
                                               '\n\nКак оплатить за сервис?'
                                               '\n\nДля этого необходимо выбрать в главном меню нужный сервис и '
                                               'выбрать услугу. Возможность оплаты уже встроена в каждый сервис. '
                                               'Вам необходимо просто выбрать способ оплаты и подтвердить платеж.')
        bot.send_message(message.from_user.id, 'Как возвратить платеж?'
                                               '\n\nВозврат платежа у партнера: '
                                               '\nВам необходимо обратиться к партнеру, '
                                               'у которого приобретали товар или услугу. '
                                               '\nПартнер должен у себя в приложении оформить возврат платежа.'
                                               '\n\nВозврат платежа за неправильное пополнение или оплату за коммунальные услуги, сотового оператора и т.д.: '
                                               '\nК сожалению, деньги за неправильное пополнение или оплату не возвращаются. '
                                               'Необходимо обратиться напрямую в компанию, в пользу которой вы пополнили.')
        bot.send_message(message.from_user.id, 'Что делать, если партнер не хочет возвращать деньги?\n\n"Если партнер не хочет возвращать деньги, пользователю необходимо оформить жалобу через колл-центр. '
                                               '\nВ течении 10 дней мы рассмотрим жалобу.'
                                               '\nК сожалению, Namba One не несет ответственность за взаимоотношения между партнерами и клиентами. '
                                               'Тем не менее мы постараемся приложить все усилия, чтобы уладить конфликт.')
        bot.register_next_step_handler(message, WorldNews)
        bot.register_next_step_handler(message, WorldNews2)
        bot.register_next_step_handler(message, WorldNews3)
        bot.register_next_step_handler(message, WorldNews5)
        bot.register_next_step_handler(message, WorldNews6)
        bot.register_next_step_handler(message, WorldNews7)
        bot.register_next_step_handler(message, WorldNews8)
        bot.register_next_step_handler(message, WorldNews9)

@bot.message_handler(content_types=['text'])
def WorldNews5(message):
    if message.text == "Идентификация":
        bot.send_message(message.from_user.id, 'Что такое идентификация?'
                                               '\n\nИдентификация - это установление и подтверждение личности клиента, '
                                               'посредством использования паспорта и других персональных данных клиента.'
                                               '\n\nЗачем нужна идентификация?'
                                               '\n\nИдентификация в электронном кошельке необходима для того, '
                                               'чтобы пополнять кошелек наличными, увеличить лимиты на проведение платежей, '
                                               'оплачивать и переводить деньги.'
                                               '\n\nСогласно требованиям Национального Банка КР, все пользователи электронного '
                                               'кошелька должны быть идентифицированы онлайн посредством фотографии и предоставлении '
                                               'персональных данных или пройти полную идентификацию в филиалах Коммерческого Банка Кыргызстан.'
                                               '\n\nКак пройти Онлайн идентификацию?'
                                               '\n\nОнлайн идентификацию можно пройти сразу же при регистрации в Namba One или в разделе Профиль.'
                                               '\n\nДля прохождения онлайн идентификации необходимо заполнить персональные данные в анкете, сделать '
                                               'фотографию паспорта с обеих сторон и сделать фотографию себя с паспортом согласно инструкции.'
                                               '\n\nКак пройти полную идентификацию?'
                                               '\n\nПолную идентификацию можно пройти в филиалах Коммерческого Банка Кыргызстан, которая позволит '
                                               'увеличить лимиты для полноценного использования возможностей приложения. При себе необходимо иметь '
                                               'паспорт и мобильный телефон, на котором вы используете Namba One.'
                                               '\nМестоположения филиалов можете посмотреть на официальном сайте Банка - www.cbk.kg'
                                               '\n\nВ чем разница между онлайн и полной идентификацией?'
                                               '\n\nРазница между онлайн и полной идентификацией в лимитах на операции.')
        bot.send_message(message.from_user.id, 'Не удается пройти идентификацию?'
                                               '\n\nУбедитесь что вы заполнили все запрашиваемые данные для прохождения '
                                               'идентификации и проверьте аккуратность их заполнения.'
                                               'Если все заполнено верно, то нужно связать клиента с операционным менеджером Namba One.')
        bot.register_next_step_handler(message, WorldNews)
        bot.register_next_step_handler(message, WorldNews2)
        bot.register_next_step_handler(message, WorldNews3)
        bot.register_next_step_handler(message, WorldNews4)
        bot.register_next_step_handler(message, WorldNews6)
        bot.register_next_step_handler(message, WorldNews7)
        bot.register_next_step_handler(message, WorldNews8)
        bot.register_next_step_handler(message, WorldNews9)

@bot.message_handler(content_types=['text'])
def WorldNews6(message):
    if message.text == "Лимиты":
        bot.send_message(message.from_user.id, 'Лимиты на операции Онлайн идентификация:'
                                               '\n\nДоступный баланс:'
                                               '\n30 000 сом'
                                               '\n\nПополнение'
                                               '\nМаксимальная сумма пополнения:'
                                               '\n30 000 сом'
                                               '\nМаксимальная сумма оплаты в течении месяца:'
                                               '\n60 000 сом'
                                               '\n\n Переводы'
                                               '\nМаксимальная сумма перевода за одну транзакцию:'
                                               '\n15 000 сом'
                                               '\nМаксимальная сумма переводов в течении месяца:'
                                               '\n30 000 сом'
                                               '\n\nВывод'
                                               '\nМаксимальная сумма вывода за одну транзакцию:'
                                               '\n15 000 сом'
                                               '\nМаксимальная сумма вывода в течении месяца:'
                                               '\n30 000 сом'
                                               '\n\nЛимиты на операции Полная идентификация:'
                                               '\n\nДоступный баланс:'
                                               '\n1 000 000 сом'
                                               '\n\nПополнение'
                                               '\nМаксимальная сумма пополнения за одну транзакцию:'
                                               '\n400 000 сом'
                                               '\nМаксимальная сумма пополнения в течении месяца:'
                                               '\n2 000 000 сом'
                                               '\n\nОплата'
                                               '\nМаксимальная сумма оплаты за одну транзакцию:'
                                               '\n500 000 сом'
                                               '\nМаксимальная сумма оплаты в течении месяца:'
                                               '\n10 000 000 сом'
                                               '\n\nПереводы'
                                               '\nМаксимальная сумма перевода за одну транзакцию:'
                                               '\n500 000 сом'
                                               '\nМаксимальная сумма переводов в течении месяца:'
                                               '\n500 000 сом')
        bot.register_next_step_handler(message, WorldNews)
        bot.register_next_step_handler(message, WorldNews2)
        bot.register_next_step_handler(message, WorldNews3)
        bot.register_next_step_handler(message, WorldNews4)
        bot.register_next_step_handler(message, WorldNews5)
        bot.register_next_step_handler(message, WorldNews7)
        bot.register_next_step_handler(message, WorldNews8)
        bot.register_next_step_handler(message, WorldNews9)

@bot.message_handler(content_types=['text'])
def WorldNews7(message):
    if message.text == "Кэшбэк":
        bot.send_message(message.from_user.id, 'Что такое Кэшбэк?'
                                               '\n\nКэшбэк - это возврат части денег от потраченной суммы в заведениях '
                                               'и магазинах партнерах в зависимости от условий предоставляющей стороны. '
                                               'Сумма возврата зависит от размера кэшбэка у партнера.Кэшбэк в NambaOne это реальные деньги.'
                                               '\n\nКак потратить Кэшбек?'
                                               '\n\nКэшбэк - является реальной денежной суммой на вашем личном кошельке, которую \nВы можете '
                                               'использовать для оплаты любых товаров, услуг или сервисов, выводить деньги или же переводить.'
                                               '\n\nКак начисляется Кэшбэк?'
                                               '\n\nПри оплате товаров и услуг у наших партнеров включенных в программу кэшбэка вы моментально '
                                               'получаете обратно часть денег от потраченной суммы к себе на кошелек NambaOne.')
        bot.register_next_step_handler(message, WorldNews)
        bot.register_next_step_handler(message, WorldNews2)
        bot.register_next_step_handler(message, WorldNews3)
        bot.register_next_step_handler(message, WorldNews4)
        bot.register_next_step_handler(message, WorldNews5)
        bot.register_next_step_handler(message, WorldNews6)
        bot.register_next_step_handler(message, WorldNews8)
        bot.register_next_step_handler(message, WorldNews9)

@bot.message_handler(content_types=['text'])
def WorldNews8(message):
    if message.text == "QR-код":
        bot.send_message(message.from_user.id, 'Что такое QR-код и QR-сканер?'
                                               '\n\nQR в Namba One - это быстрый инструмент для оплаты и переводов. '
                                               '\nQR-сканер находится в быстром доступе в Namba One в разделе  \n“Оплатить”. '
                                               'Вы можете отсканировать QR-код получателя и оплатить или перевести деньги. '
                                               'QR-код используется для приема оплаты или перевода от отправителя. '
                                               'Эта функция расположена в разделе “Оплатить” в правом верхнем углу.'
                                               '\n\nОплата через QR'
                                               '\n\nДля совершения оплаты через QR, вам необходимо:'
                                               '\n1. Нажать на кнопку “Оплатить” в нижнем меню приложения.'
                                               '\n2. Отсканировать QR-код получателя или показать свой QR-код. Показать свой QR-код можно нажав на кнопку “Мой QR”.')
        bot.register_next_step_handler(message, WorldNews)
        bot.register_next_step_handler(message, WorldNews2)
        bot.register_next_step_handler(message, WorldNews3)
        bot.register_next_step_handler(message, WorldNews4)
        bot.register_next_step_handler(message, WorldNews5)
        bot.register_next_step_handler(message, WorldNews6)
        bot.register_next_step_handler(message, WorldNews7)
        bot.register_next_step_handler(message, WorldNews9)

@bot.message_handler(content_types=['text'])
def WorldNews9(message):
    if message.text == 'Безопасность':
        bot.send_message(message.from_user.id, 'Вы защищены надежной системой безопасности с нашей стороны, а также личным паролем, '
                                               'который знаете только вы. Все операции по банковским картам защищены платежными системами Visa,'
                                               ' Mastercard и Элкарт. Мы следим, чтобы злоумышленники не имели доступ в систему и к вашим данным')
        bot.register_next_step_handler(message, WorldNews)
        bot.register_next_step_handler(message, WorldNews2)
        bot.register_next_step_handler(message, WorldNews3)
        bot.register_next_step_handler(message, WorldNews4)
        bot.register_next_step_handler(message, WorldNews5)
        bot.register_next_step_handler(message, WorldNews6)
        bot.register_next_step_handler(message, WorldNews7)
        bot.register_next_step_handler(message, WorldNews8)
        
bot.polling(none_stop=True)        

    def main():
    bot.polling(none_stop=True)

