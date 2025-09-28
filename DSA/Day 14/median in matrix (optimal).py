def upperBound(arr, x, n):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def countSmallEqual(matrix, N, M, x):
    cnt = 0
    for i in range(N):
        cnt += upperBound(matrix[i], x, M)
    return cnt


def median(matrix, N, M):
    low = float('inf')
    high = float('-inf')


    for i in range(N):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][M - 1])


    req = (N * M) // 2


    while low <= high:
        mid = (low + high) // 2
        smallEqual = countSmallEqual(matrix, N, M, mid)

        if smallEqual <= req:
            low = mid + 1
        else:
            high = mid - 1

    return low


if __name__ == "__main__":

    matrix = [
        [1],
        [2],
        [3],
        [4],
        [5]
    ]

    N = 5
    M = 1
    result = median(matrix, N, M)
    print(f"Median of the matrix is: {result}")