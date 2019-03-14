def people_information():
    current_year = 2019
    name = str(input("Hai , Enter your name"))
    age = int(input("Enter your age"))
    remaining_years = 100 - age
    your_age = current_year + remaining_years
    print("your name is " + name)
    print("your current age is ", age)
    print("when 100 years  :", your_age)


people_information()
