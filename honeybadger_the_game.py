import random
import time

print("🐾 Welcome to the game 'Honey Badger vs. The Old Man'!")
print("Your goal: steal 5 jars of jam and survive!")

jars = 0
hp = 3
collected_jars = []

jams = ["strawberry", "blueberry", "raspberry", "pepper"]

def show_status():
    print(f"\n📊 Jars: {jars}/5 | ❤️ Health: {hp}")
    if collected_jars:
        print(f"🫙 Collected Jams: {', '.join(collected_jars)}")
    else:
        print("🫙 No jam collected yet.")

while jars < 5 and hp > 0:
    show_status()
    time.sleep(1)

    action = input("\nWhat will you do? (1 — steal a jar, 2 — look around, 3 — crawl silently): ")

    if action == "1":
        jar = random.choice(jams)
        collected_jars.append(jar)
        jars += 1
        print(f"✅ The honey badger grabbed a jar of {jar} jam!")

        if jar == "raspberry":
            hp = min(hp + 1, 3)
            print("🍯 The raspberry jam was healing! Health +1.")
        elif jar == "pepper":
            print("🔥 It's too spicy! The honey badger made some noise...")
            if random.choice([True, False]):
                print("💥 BANG! The old man heard the noise and fired his gun!")
                hp -= 1

        if random.randint(1, 4) == 1:
            print("👀 The old man spotted the honey badger!")
            print("💥 BANG! The old man shoots!")
            hp -= 1

    elif action == "2":
        print("🔎 The honey badger looks around...")
        time.sleep(2)
        find = random.choice(["a piece of bacon", "an old bone", None])
        if find:
            print(f"🎁 The honey badger found: {find}!")
            if find == "a piece of bacon":
                hp = min(hp + 1, 3)
                print("🧈 The honey badger ate the bacon — health restored!")
        else:
            print("😞 Nothing useful found.")

    elif action == "3":
        print("🐾 The honey badger crawls silently...")
        time.sleep(2)
        if "blueberry" in collected_jars:
            print("👴 After eating blueberry jam, the old man’s eyesight got worse — lower chance to spot you!")
            if random.randint(1, 5) == 1:
                print("💥 Oh no, the old man still noticed you!")
                hp -= 1
        else:
            if random.randint(1, 3) == 1:
                print("💥 BANG! The old man heard something or saw you!")
                hp -= 1
            else:
                print("✅ The honey badger sneaked by unnoticed.")

if jars == 5:
    print("\n🎉 Victory! The honey badger stole 5 jars of jam and escaped!")
elif hp <= 0:
    print("\n☠️ The honey badger died a hero.")
else:
    print("\n🤔 How did you get here? This is a bug!")

print("Game Over.")