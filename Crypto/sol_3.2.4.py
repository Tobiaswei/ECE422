import pbp
from fractions import gcd
from Crypto.PublicKey import RSA


# Function Source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def modular_multiplicative_inverse(input_1, input_2):
    b = input_1
    a = input_2
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0 % input_2


with open("./moduli.hex") as moduli_file, open("./3.2.4_ciphertext.enc.asc") as cipher_file,\
 open("./sol_3.2.4.txt", 'w') as out_file:

    moduli_list = []
    for i in moduli_file.readlines():
        moduli_list.append(int(i.strip(), 16))

    print("Product Tree starts!")
    product_tree = [moduli_list]
    while len(product_tree[-1]) > 1:
        product_tree_last = product_tree[-1]
        product_tree.append([])

        for i in range(len(product_tree_last) / 2):
            product_tree[-1].append(product_tree_last[i * 2] * product_tree_last[i * 2 + 1])
        if len(product_tree_last) % 2:
            product_tree[-1].append(product_tree_last[len(product_tree_last) - 1])
    product_all = product_tree[-1][0]
    print("Product Tree finishes!\n")

    print("Squared Product Tree starts!")
    product_tree_squared = []
    for i in range(len(product_tree)):
        product_tree_squared.append([])
        for j in range(len(product_tree[i])):
            product_tree_squared[-1].append(product_tree[i][j]**2)
    print("Squared Product Tree finishes!\n")

    print("Remainder Tree starts!")
    remainder_tree = [product_all]
    for product_tree_squared_node in product_tree_squared[::-1]:
        remainder_tree_copy = remainder_tree[:]
        remainder_tree = []
        for i in range(len(product_tree_squared_node)):
            remainder_tree.append(remainder_tree_copy[i // 2] % product_tree_squared_node[i])
    print("Remainder Tree finishes!")

    print("GCD starts!")
    moduli_candidates = []
    for remainder, N in zip(remainder_tree, moduli_list):
        gcd_value = gcd(remainder / N, N)
        if gcd_value != 1 and gcd_value != N:
            moduli_candidates.append((N, gcd_value))
    print("GCD finishes!")

    print("Search for Private Keys starts!")
    private_keys = []
    e = 65537
    for i in range(len(moduli_candidates)):
        N = moduli_candidates[i][0]
        p = moduli_candidates[i][1]
        q = N / p
        d = modular_multiplicative_inverse(e, (p - 1) * (q - 1))
        private_keys.append(RSA.construct((long(N), long(e), long(d))))
    print("Search for Private Keys finishes!")

    cipher_text = cipher_file.read()
    for key in private_keys:
        try:
            plaintext = pbp.decrypt(key, cipher_text)
            print(plaintext)
            out_file.write(plaintext)
        except ValueError:
            pass
