import spockbots.robot as robot


while True:
    line = input("spockbots >>> ")
    try:
        eval(line)
    except Exception as e:
        print()
        print(e)
        print()