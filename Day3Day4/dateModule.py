import datetime

def theDate():
    
    x = datetime.datetime.now()
    day = x.strftime("%A")
    month = x.strftime("%B")
    day_number = x.strftime("%d")
    year = str(x.year)

    x = datetime.datetime.now()
    print("Hello, it is " + day + " " + month + " " + day_number + ", " + year)


