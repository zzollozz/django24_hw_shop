import secrets

def sec_key():
    return secrets.token_hex()



if __name__ == '__main__':
    print(sec_key())