days = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday')

days_list= list(days)
days_list.remove('Sunday')
days_list.append('Domingo')
days_tuple= tuple(days_list)
print(days_tuple)