import glob, os, csv

file_path = './ids.txt'

def get_all_files_in_subfolders(folder):
    return glob.glob(f'{folder}/**/*', recursive=True)

numbers = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()  # Remove any leading/trailing whitespace characters
        if line:  # Ensure the line is not empty
            number = int(line)
            numbers.append(number)
            # print(number)



folder_path = './bmvc2024_upload'
all_files = get_all_files_in_subfolders(folder_path)

with open("files.csv", 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Number', 'File Name'])  # Write the header row

    for number in numbers:
        print(f'Files for number {number}:')
        file_info = []
        for file in all_files:
            paper_number = 'Paper_'+str(number)
            if paper_number in file:
                file_name = os.path.basename(file)
                # print(file)
                if 'Paper_' not in file_name:
                    print(file_name)
                    file_info.append(f"{file_name}; ")
        
        csvwriter.writerow([number, ''.join(file_info)])