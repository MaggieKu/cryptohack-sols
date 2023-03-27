# flag ? key1 ? key2 ? key3 = (flag ? key1) ? (key2 ? key3)
# flag ? key1 =  (flag ? key1) ? (key2 ? key3) ? (key2 ? key3)
# flag = flag ? key1 ? key1
# Would have a more elegant answer if I figured out how to import pwn!

xoredflag = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2xorkey3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"

xf = [i for i in bytes.fromhex(xoredflag)]
k1 = [i for i in bytes.fromhex(key1)]
k2k3 = [i for i in bytes.fromhex(key2xorkey3)]

res = ""
for i in range(len(xf)):
    res += (chr((xf[i] ^ k2k3[i]) ^ k1[i]))

print(res)
