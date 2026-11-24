usernames = ["Harshita", "Basit", "Khushi", "Shanu"]
followers = [500, 1200, 800, 2000]

instagram = {}

for i in range(len(usernames)):
    instagram[usernames[i]] = followers[i]

print(instagram)
