from zxcvbn import zxcvbn

def pw_strength(password):
    checks = zxcvbn(password)
    score = checks["score"]
    if score ==4 :
        opinion = "Entered Password is very STRONG and safe "
    elif score == 3 :
        opinion = "Entered password is pretty DECENT"
    else:
        opinion = "Entered password is very WEAK and easy to crack : DO BETTER"
    return opinion