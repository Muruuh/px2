class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def orolt(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def garalt(self):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        return total_seconds

with open("input.txt", "r") as file:
    hours1, minutes1, seconds1 = map(int, file.readline().split())
    hours2, minutes2, seconds2 = map(int, file.readline().split())

time1 = Time(hours1, minutes1, seconds1)
time2 = Time(hours2, minutes2, seconds2)

total_time_seconds = abs(time1.garalt() - time2.garalt())


total_hours = total_time_seconds // 3600
total_minutes = (total_time_seconds % 3600) // 60
total_seconds = total_time_seconds % 60

with open("output.txt", "w") as file:
    file.write(f"Нийт цагийн зөрүү: {total_hours} цаг, {total_minutes} минут, {total_seconds} секунд\n")
    file.write(f"Time 1: {time1.orolt()}\n")
    file.write(f"Time 2: {time2.orolt()}\n")
