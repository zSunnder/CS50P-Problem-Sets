import csv

name = input("wat ur name ")
home = input("wat ur home ")

with open("students.csv", "a") as file:
    write = csv.DictWriter(file, fieldnames=["name", "home"])
    write.writerow({"name": name, "home": home})
