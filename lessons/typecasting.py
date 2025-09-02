# Typecasting
# Typecasting - change a given variable type

def main():
    name = "Dom"
    age = 18
    gpa = 5.0
    is_student = True

    print(type(name))
    print(name)

    # Integer typecasting
    gpa = int(gpa) # 5 -> Truncates the decimal
    print(gpa)

    # Float typecasting
    age = float(age) # 18.0 -> Addition of decimal/floating point value
    print(age)

    # String typecasting
    age = str(age) 
    print(type(age))
    print(age)

    # String concatenation
    age = str(age)
    age += "1"
    print(age)

    # Boolean typecasting
    empty = ""
    name = bool(name)
    print(name)
    name = bool(empty) # If " " = True; if "" = False
    print(name)


if __name__ == "__main__":
    main()
