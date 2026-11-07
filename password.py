from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt

def pw_strength(password):
    checks = zxcvbn(password)
    score = checks["score"]
    if score ==4 :
        opinion = "Very Strong Password"
    elif score == 3 :
        opinion = "Password is Ok"
    else:
        opinion = "Weak Password"
    return opinion

def hashed_pw(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_pw(pw_attempt,hashed):
    if bcrypt.checkpw(pw_attempt.encode(), hashed):
        return "Correct Password, Access Granted.."
    return "Incorrect Password, Access Denied..."

if __name__ == "__main__":
    password = getpass("Enter Password : ")
    print(pw_strength(password))
    print("____________________________________________________________")
    pw_attempt = getpass("Re-enter the password : ")
    print(verify_pw(pw_attempt,hashed_pw(password)))