import os

def generate_file_list(user_input, files, migrations_abs_path):
    return_files_list = []
    for file in files:
        with open(os.path.join(migrations_abs_path, file), 'rt') as f:
            data = f.read()
            if user_input.lower() in data.lower():
                return_files_list.append(file)

    return return_files_list, len(return_files_list)

def main():
    migrations = 'Migrations'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    migrations_abs_path = os.path.join(current_dir, migrations)
    files = [f for f in os.listdir(migrations_abs_path) if f.endswith('.sql')]
    files_list = []

    while True:
        user_input = input('Введите искомую строку: ')
        return_object = generate_file_list(user_input, files, migrations_abs_path)
        files, quantity = return_object
        for file in files:
            print(file)
        print('Всего: {0}'.format(quantity))

main()