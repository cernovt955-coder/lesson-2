catalog = []
phone1 = Smartphone("Марка1", "Модель1", "+79000000001")
phone2 = Smartphone("Марка2", "Модель2", "+79000000002")
# ... и так далее для пяти телефонов
catalog.extend([phone1, phone2, phone3, phone4, phone5])

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
