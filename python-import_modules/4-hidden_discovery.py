#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    def find():
        names = dir(hidden_4)
        for i in names:
            if not i.startswith('__'):
                print('{}'.format(i))
find()
