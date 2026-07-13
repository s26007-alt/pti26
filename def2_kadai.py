def postTaxPrice(price):
    ans = price * 1.08
    return ans

print(int(postTaxPrice(120)),"円")
print(int(postTaxPrice(128)),"円")
print(int(postTaxPrice(980)),"円")
