from faker import Faker

fake = Faker(locale='zh_CN')
name = fake.name()
print(name)
sfz = fake.ssn(min_age=18, max_age=90)
print(sfz)
phone = fake.phone_number()
print(phone)




