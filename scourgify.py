import sys, csv

def line_arguments(arguments):
    if len(arguments) < 3:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 3:
        sys.exit("Too many command-line arguments")

def check_filename(argument, check = True):
    if argument.split(".")[1] != "csv":
        sys.exit("Not a CSV file")

    if check:
        try:
            open(argument, "r")
        except:
            sys.exit(f"Could not read {argument}")
    
    return argument

def main(arguments):
    line_arguments(arguments)

    try:
        with open(sys.argv[1], 'r', newline='') as input_file, \
            open(sys.argv[2], 'w', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)
            writer.writerow(['first', 'last', 'house'])
            for row in reader:
                name, house = row
                first, last = name.split(', ')
                writer.writerow([first, last, house])
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')                