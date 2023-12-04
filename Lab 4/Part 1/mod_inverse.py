from sympy import mod_inverse


def key_gen(a, d, p):
    return pow(a, d, p)

def sign(x, a, d, p, k_e):
    r = pow(a, k_e, p)
    k_inv = mod_inverse(k_e, p - 1)
    s = ((x - d*r) * k_inv) % (p - 1)
    return (r, s)

def verify(x, r, s, B, a, p):
    t = (pow(B, r, p)*pow(r, s, p)) % p
    test = pow(a, x, p)
    return t == test

print(sign(435774528075745568404129942557, 476219007220973994303455600579, 113087485233248996526571115482, 669379343040372993112682310767, 291905782067546206475817580403))