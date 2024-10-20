print("Pick up a sock")
sock1 = input("What color is the sock? ")
sock2 = input("Pick up another sock. What color is it? ")
while sock1 != sock2:
  print("Your socks do not match.")
  sock2 = input("Pick up another sock. What color is it? ")
print("Your socks match! Now put them on.")
