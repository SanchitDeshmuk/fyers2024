import pyotp as tp

totp_key = 'RU376TSN3LAENIQZT3PNB2HWWYORMSNF'
k = tp.TOTP(totp_key).now()

print(k)