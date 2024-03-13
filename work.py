from datetime import datetime
   
def get_days_from_today():
    user_input = input('Введіть дату PPPP-MM-ДД: ')
    user_date = datetime.strptime(user_input, '%Y-%m-%d')

    print(user_date)
