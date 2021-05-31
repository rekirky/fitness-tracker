import csv

def main():
  print("Welcome to Azentro - MVM Activity Conversion Chart")

  data = load_data()
  activity = input("Enter Activity: ")
  time = float(input("Enter Time/KM worked: "))
  for i in data:
    if activity == i[0]:
      output = float((i[2] * (time/10)) + (i[1]*(time%10)))
  print(f"For doing {activity} for {time} min/km you earn {output} ")
    
def load_data():
    data = []
    file_in = open("data.csv", 'r', newline='')
    csv_reader = csv.reader(file_in)
    for row in csv_reader:
      row[1] = float(row[1])
      row[2] = float(row[2])
      data.append(row)
    file_in.close()
    file_loaded = True
    return data

main()
