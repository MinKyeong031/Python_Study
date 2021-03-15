def repeat(s, n = 3):
    print(((s + ",") * (n-1)) + s)

def once(s):
    print(s)

if __name__ == '__main__':
    repeat('김성수', 5)
    once('김성수')