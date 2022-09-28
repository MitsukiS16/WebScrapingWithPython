def sort_file_content(in_path, out_path):
    lines = []

    with open(in_path) as in_f:
        for line in in_f:
            lines.append(line)

    lines.sort()

    with open(out_path, 'w') as out_f:
        for line in lines:
            out_f.writelines(line)

if __name__ == "__main__":
    input_file = "urlDB.txt"
    output_file = "output.txt"
    sort_file_content(input_file, output_file)