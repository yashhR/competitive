# t = int(input())
# for _ in range(t):
#     n, a, b = map(int, input().split())
#     sequence = list(map(int, input().split()))
#     both = set()
#     bob_only = set()
#     alice_only = set()
#     for i in range(len(sequence)):
#         if sequence[i] % a == 0 and sequence[i] % b == 0:
#             both.add(sequence[i])
#         elif sequence[i] % a == 0:
#             bob_only.add(sequence[i])
#         elif sequence[i] % b == 0:
#             alice_only.add(sequence[i])
#     Bob = True
#     Alice = False
#     for i in range(len(sequence)):
#         if Bob:
#             if len(both) == 0 and len(bob_only) == 0:
#                 print("ALICE")
#                 break
#             elif sequence[i] in both:
#                 both.remove(sequence[i])
#             elif sequence[i] in bob_only:
#                 bob_only.remove(sequence[i])
#         if Alice:
#             if len(both) == 0 and len(alice_only) == 0:
#                 print("BOB")
#                 break
#             elif sequence[i] in both:
#                 both.remove(sequence[i])
#             elif sequence[i] in alice_only:
#                 alice_only.remove(sequence[i])
#         Bob = not Bob
#         Alice = not Alice

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    sequence = list(map(int, input().split()))
    if a == b:
        print("BOB")
    else:
        both = set()
        bob_only = set()
        alice_only = set()
        for i in range(len(sequence)):
            if sequence[i] % a == 0 and sequence[i] % b == 0:
                both.add(sequence[i])
            elif sequence[i] % a == 0:
                bob_only.add(sequence[i])
            elif sequence[i] % b == 0:
                alice_only.add(sequence[i])
        if len(bob_only) >= len(alice_only):
            print("BOB")
        else:
            print("ALICE")