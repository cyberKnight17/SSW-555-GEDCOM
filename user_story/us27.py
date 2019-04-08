from datetime import datetime

def age_cal(birthday): # calculate individual's age
    birthdate = datetime.strptime(birthday, '%d%b%Y')
    current = datetime.today()
    return current.year - birthdate.year - ((current.month, current.day) < (birthdate.month, birthdate.day))