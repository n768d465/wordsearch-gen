from wordsearch_generator import WordSearchGenerator
import argparse


def run_wordsearch(dim, fill, length):
    ws = WordSearchGenerator(dim=dim, fill=fill, max_word_length=length)
    ws.make_wordsearch()

    print()
    for row in ws.grid:
        print(" ".join(row))

    print("\nWord bank")
    print("---------")
    for word in ws.bank:
        print(word, end=" ")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Random wordsearch generator.")
    parser.add_argument("--dim", type=int, default=10)
    parser.add_argument("--no-fill", action="store_false")
    parser.add_argument("--max-word-length", type=int, default=10)

    args = parser.parse_args()

    run_wordsearch(args.dim, args.no_fill, args.max_word_length)
