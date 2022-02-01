"""
2.  Создать текстовый файл (не программно), сохранить в нём несколько строк,
    выполнить подсчёт строк и слов в каждой строке.
"""
with open("Text1", encoding="utf-8") as file_text:
    num_strings = file_text.readlines()
    print("Строк в файле: ", len(num_strings))
    for num_string, string in enumerate(num_strings, 1):
        print(f"Слов в {num_string} строке:", len(string.split()))
