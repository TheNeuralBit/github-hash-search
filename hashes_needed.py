def hash_count(hash):
    bits = len(hash)*4
    return 1 << (160 - bits)

if __name__ == "__main__":
    import sys

    print(int((1 << 160)/ sum(hash_count(line.strip()) for line in sys.stdin.readlines())))
