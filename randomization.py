import random
import csv

if __name__ == '__main__':
    with open("names.txt") as f:
        giver = f.readlines()
        for i, val in enumerate(giver):
            giver[i] = val.strip()

    receiver = list(giver)
    repetition = True
    while repetition:
        repetition = False
        random.shuffle(receiver)
        print(giver, "\n", receiver, "\n---------")
        for i in range(len(giver)):
            if giver[i] == receiver[i]:
                repetition = True
                break

    with open("connections.csv", "w", newline='') as f:
        csvwriter = csv.writer(f)
        for i in range(len(giver)):
            csvwriter.writerow([giver[i], receiver[i]])

