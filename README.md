# py-cat

`py-cat` is a Python script that mimics the behavior of the Unix `cat` command with additional options for numbering lines.

## Features

- Read from multiple files or standard input.
- Number all lines with the `-n` option.
- Number non-blank lines with the `-b` option.

## Usage

```bash
python main.py [options] [file ...]
```

### Options

- `-n`: Number all lines.
- `-b`: Number non-blank lines.

### Examples

#### Number all lines in a file

```bash
python main.py -n file.txt
```

#### Number non-blank lines in a file

```bash
python main.py -b file.txt
```

#### Read from standard input and number all lines

```bash
echo "Hello\nWorld" | python main.py -n
```

#### Read from multiple files

```bash
python main.py file1.txt file2.txt
```

## Code Explanation

The script processes command-line arguments to determine the options and files to read. If no files are provided, it reads from standard input. It then processes the lines according to the specified options and prints them.

### Argument Parsing

The [`parse_args`](command:_github.copilot.openSymbolFromReferences?%5B%22parse_args%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fnordin%2Fdev%2Fpy-cat%2Fmain.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fnordin%2Fdev%2Fpy-cat%2Fmain.py%22%2C%22path%22%3A%22%2Fhome%2Fnordin%2Fdev%2Fpy-cat%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A18%7D%7D%5D%5D "Go to definition") function from [`utils.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fnordin%2Fdev%2Fpy-cat%2Futils.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/nordin/dev/py-cat/utils.py") is used to parse command-line arguments and set the appropriate options.

### Line Processing

Lines are processed to add line numbers based on the specified options (`-n` for numbering all lines, `-b` for numbering non-blank lines).

### Main Function

The main function reads from stdin if no files are provided, otherwise reads from the specified files and processes the lines accordingly.

## License

This project is licensed under the MIT License.

---

Feel free to modify this README to better fit your project's needs.
