def main():

    file_path = 'books/frankenstein.txt'
    words = get_words(file_path)
    total = count_words(words)
    char_counts = count_characters(words)
    report = gen_report(file_path, total, char_counts)
    print(f"{total} words foound in this document")
    print(char_counts)
    print(report)

def get_words(file_path: str) -> str:
    with open(file_path, 'r') as file:
        file_contents = file.read()
        return file_contents

def count_words(string: str) -> int:
    words = string.split()
    count = len(words)
    return count

def count_characters(string: str) -> dict[str, int]:
    words = string.lower().strip()
    word_counts = {}
    for char in words:
        if char not in word_counts:
            word_counts[char] = 1
        else:
            word_counts[char] += 1
    return word_counts

def gen_report(
        title: str,
        word_count: int,
        char_count: dict[str, int]
) -> str:
    sorted_chars = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    report = f"--- Begin report of {title} ---\n{word_count} words found in document\n\n"
    for key, value in sorted_chars.items():
        if key.isalpha():
            report = report + f"The '{key}' character was found {value} times\n"
    report = report + "--- End report ---"
    return report


main()
