import numpy as np

# Longest common subsequence
def lcs_bf(A, B):
    """Run in exponential time"""
    def lcs_bf_recursive(A, B, m, n):
        if m == 0 or n == 0:
            return 0
        elif A[m-1] == B[n-1]:
            result = 1 + lcs_bf_recursive(A,B,m-1,n-1)
        else:
            result = max(lcs_bf_recursive(A,B,m-1,n), lcs_bf_recursive(A,B,m,n-1))
        return result
    return lcs_bf_recursive(A, B, len(A), len(B))

def lcs_memo(A, B):
    """Run in O(mn) time"""
    memo = {}
    def lcs_memo_recursive(A, B, m, n, memo):
        if (m,n) in memo:
            return memo[m,n]
        if m == 0 or n == 0:
            result = 0
        elif A[m-1] == B[n-1]:
            result = 1 + lcs_memo_recursive(A,B,m-1,n-1,memo)
        else:
            result = max(lcs_memo_recursive(A,B,m-1,n,memo), lcs_memo_recursive(A,B,m,n-1,memo))
        memo[m,n] = result
        return result
    return lcs_memo_recursive(A, B, len(A), len(B), memo)

def lcs_table(A, B):
    m = len(A)
    n = len(B)
    T = np.zeros((m+1,n+1), dtype=int)

    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    print(np.matrix(T).T)
    return T[-1][-1]

def main():
    seq1 = "snowflake"
    seq2 = "horseback"
    print(lcs_bf(seq1, seq2))
    print(lcs_memo(seq1, seq2))
    print(lcs_table(seq1, seq2))

if __name__ == "__main__":
    main()