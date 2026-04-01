def isHappy(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False

        seen.add(n)

        total = 0
        for digit in str(n):
            total += int(digit) ** 2

        n = total

    return True


if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
