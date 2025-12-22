from Crypto.Util.number import long_to_bytes
import gmpy2

ct = int(
    "756b45c7f89ef9544e4fa53bce87946c0b17df562cec738e89562e01a9bda791"
    "6785b16a3eee9d3b53c060bfa051851d6c4c9d85ee0a2be1e624d632569e7ec"
    "65fd48e632e25b71a44f08f8d9f7fa4e7f5833bec9f865",
    16
)

m, exact = gmpy2.iroot(ct, 3) 
#iroot(ct, 3) computes integer k-th root of ct
assert exact

print(long_to_bytes(m))