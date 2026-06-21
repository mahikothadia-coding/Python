import random

secret = random.randint(1, 50)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Enter your guess (1-50): "))

    if guess == secret:
        print("🎉 You won!")
        break

    diff = abs(secret - guess)

    if diff >= 20:
        print("🧊 Ice Cold")
    elif diff >= 10:
        print("🥶 Cold")
    elif diff >= 5:
        print("🌡️ Warm")
    else:
        print("🔥 Hot")

    attempts += 1

    print("Remaining hearts: ", end="")
    for i in range(max_attempts - attempts):
        print("❤️", end=" ")
    print()

if attempts == max_attempts and guess != secret:
    print("❌ You lost!")
    print("Secret number was:", secret)
