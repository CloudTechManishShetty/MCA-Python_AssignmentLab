import random
import datetime
import math

participants = ["Manish", "Ganesh", "Deepak", "Kaushik", "Rohan", "Kaushal", "Shrinivas", "Maithili", "Rutuja"]
total_prize_pool = 50000

print("--- Lucky Draw Contest ---")
num_winners = 5
winners = random.sample(participants, num_winners)
print("The ",num_winners," Winners are: ",winners)

now = datetime.datetime.now()
print("Draw Date & Time: ",now.strftime('%Y-%m-%d %H:%M:%S'))

base_prize = total_prize_pool / num_winners
bonus_percentages = [0.40, 0.30, 0.10, 0.10, 0.10]
prizes = []

print("\n--- Prize Distribution ---")
for i, winner in enumerate(winners):
    bonus_amount = base_prize * bonus_percentages[i]
    total_prize = math.ceil(base_prize + bonus_amount)
    prizes.append(total_prize)
    
    print(winner," (Bonus: ",bonus_percentages[i]*100,"%): Base", base_prize + bonus_amount," = Total ",total_prize)

print("\nTotal Prize Pool: ",total_prize_pool)
print("Total Distributed (Rounded): ",sum(prizes))