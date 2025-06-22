#lab Exception ( wasan alqahtani)
def additoin(x, y):
    #handle the exception in try and catch 
    try:
        x = 10
        y = 20
        print("Addition:", x + b)
        print("the operation is successful")
    # type of exception is raised
    except NameError as error:
        print(f"There is a variable not defined type of error :{error.__class__}")
    except Exception as e:
        print(f"Error occur : {e.__class__}")

additoin(10, 20)