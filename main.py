import osa

def convert_fahrenheit_to_celsius(value):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    return client.service.ConvertTemp(value, 'degreeFahrenheit', 'degreeCelsius')

def convert_value_to_rubles(value, currency_code):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    exchange_rate = float(client.service.RateStr('', currency_code, 'RUB', 'true', '', '', ''))
    return float(value) * exchange_rate

def convert_miles_to_kilometers(value):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    return client.service.ChangeLengthUnit(value, 'Miles', 'Kilometers')

def calculate_average_temp(file_path):
    with open(file_path, 'rt') as f:
        data = f.read()
        source_values_array = data.split('\n')
        celsius_value_list = []
        for element in source_values_array:
            element = element.replace(' F', '')
            celsius_value_list.append(convert_fahrenheit_to_celsius(element))
        average_temp = round(float(sum(celsius_value_list) / float(len(celsius_value_list))), 1)
        print('Средняя температура за неделю: {0} C'.format(average_temp))

def calculate_expencies_for_flights(file_path):
    with open(file_path, 'rt') as f:
        data = f.read()
        source_values_array = data.split('\n')
        flights_costs_list = []
        for element in source_values_array:
            cost = element.split(' ')[1]
            currency_code = element.split(' ')[2]
            flights_costs_list.append(convert_value_to_rubles(cost, currency_code))
        print('Суммарная стоимость перелетов в рублях: {0}'.format(round(sum(flights_costs_list))))

def calculate_trip_length(file_path):
    with open(file_path, 'rt') as f:
        data = f.read()
        source_values_array = data.split('\n')
        trip_length_list = []
        for element in source_values_array:
            miles_length_string = element.split(' ')[1]
            miles_length = float(miles_length_string.replace(',', ''))
            trip_length_list.append(convert_miles_to_kilometers(miles_length))
        print('Cуммарное расстояние пути в километрах с точностью до сотых: {0}'.format(round(sum(trip_length_list), 2)))

# calculate_average_temp('D:\\__Netology\\3.5_soap\\temps.txt')
# calculate_expencies_for_flights('D:\\__Netology\\3.5_soap\\currencies.txt')
# calculate_trip_length('D:\\__Netology\\3.5_soap\\travel.txt')