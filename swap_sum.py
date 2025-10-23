def swap_sum(A, B):
    """
    Given two sorted integer arrays, return a pair of indices that makes the
    sum of array B exactly 10 greater than the sum of array A
    
    Input: 
        - A (List): A sorted list of integers
        - B (List): A sorted list of integers

    Return:
        - indices (tuple): The indices that swap
    """
    sumA = sum(A)
    sumB = sum(B)

    diff_sum = sumB - sumA - 10
    # sumB = sumA + 10
    # sumB - B[j] + A[i] = sumA - A[i] + B[j] - 10
    # sumB - sumA - 10 = 2 * (B[j] - A[i])
    # (sumB - sumA - 10) / 2 = B[j] - A[i]
    if diff_sum % 2 != 0:
        return None  # no integer solution possible

    target_diff = diff_sum // 2

    i, j = 0, 0

    while i < len(A) and j < len(B):
        diff = B[j] - A[i]
        if diff == target_diff:
            return (i, j)
        # B[j] is much greater than A[i]
        elif diff > target_diff:
            i += 1
        else:
            j += 1
    return None