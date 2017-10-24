s = "arzobobispobobia"
print(sum(s[i:].startswith("bob") for i in range(len(s))))