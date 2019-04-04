import json

def main():
    with open("test.json","w") as file:
        for i in reversed(range(1,133)):
            file.write("\"{}\": [\"3\",\"2\",\"1\"],".format(i))

if __name__ == "__main__":
    main()
