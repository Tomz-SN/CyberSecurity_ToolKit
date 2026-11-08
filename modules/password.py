from zxcvbn import zxcvbn

# Checks strength of the password by using zxcvbn library, recieve password as argument...

def pw_strength(password):
    checks = zxcvbn(password)

# score is one of the keys in zxcvbn function output, which is a dictionary...
    score = checks["score"]

    if score ==4 :
        opinion = "Entered Password is very STRONG and safe "
    elif score == 3 :
        opinion = "Entered password is pretty DECENT"
    else:
        opinion = "Entered password is very WEAK and easy to crack : DO BETTER"
    return opinion