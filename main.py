import subprocess
import os
from multiprocessing import Process

def create_directory_if_missing(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print('Directory {0} was created'.format(folder_path))

def convert_images(current_dir, path_to_source, files):
    path_to_converter = os.path.join(current_dir, 'convert.exe')
    path_to_result = os.path.join(current_dir, 'Result')
    create_directory_if_missing(path_to_result)
    for file in files:
        subprocess.run(path_to_converter + ' "' + os.path.join(path_to_source, file) + '" -resize 200 "' + os.path.join(path_to_result, file) + '"')

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_source = os.path.join(current_dir, 'Source')
    files = os.listdir(path_to_source)
    first_process_files = files[0::4]
    second_process_files = files[1::4]
    third_process_files = files[2::4]
    fourth_process_files = files[3::4]
    process_1 = Process(target=convert_images, args=(current_dir, path_to_source, first_process_files))
    process_2 = Process(target=convert_images, args=(current_dir, path_to_source, second_process_files))
    process_3 = Process(target=convert_images, args=(current_dir, path_to_source, third_process_files))
    process_4 = Process(target=convert_images, args=(current_dir, path_to_source, fourth_process_files))
    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()
    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()