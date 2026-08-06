# This function is to find the missing element in a given array from 1 to N


# Pseudo code:
"""
arr = [1,2,4,5]

find_missing_element(arr):
    for(i=1;i<=n;i++)
    {   
        flag = 0
        for (j=0,j<n;j++)
        {
            if(arr[j]==i)
            {
            flag = 1
            break
            }
        }
        if flag == 1;
            return i
    }

"""

def missing_element(arr):
    n = len(arr)
    for i in range(1,n+1):
        flag = 0
        for j in range(0,n):
            if arr[j] == i:
                flag = 1
                break
        if flag == 0:
            return i

arr = [1,2,4,5]
missing_elem = missing_element(arr)
print(f"missing element in array is : {missing_elem}")


# T.C = o(n^2)
# S.C = o(1)