array = [-1, -5, -10, -1100, -1101, -1102, -9000]


def is_monotonic(a):
    return (
            all(a[i] <= a[i + 1] for i in range(len(a) - 1)) or
            all(a[i] >= a[i + 1] for i in range(len(a) - 1))
    )


print(is_monotonic(array))
