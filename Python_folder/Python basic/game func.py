def game():
    return 221


score = game()
with open ("highscore") as f:
    highscore = int(f.read())

if highscore<score:
    with open("highscore", "w") as f:
        f.write(str(score))