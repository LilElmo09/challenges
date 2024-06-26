def main():
    category = ''
    height = float(input('Enter your height in meters: '))
    weight = float(input('Enter your weight in kilograms: '))
    bmi = weight / (height**2)
    if bmi < 18.5:
        category = 'underweight'
    elif bmi >= 18.5 and bmi < 25:
        category = 'normal weight'
    elif bmi >= 25 and bmi < 30:
        category = 'overweight'
    elif bmi >= 30:
        category = 'obese'
    else:
        print("Out of range")
        main()
    print(f'Your BMI is {bmi:.2f}, which means you are in the {category} category')

if __name__ == '__main__':
    main()
