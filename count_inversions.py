'''
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum [n*(n-1)/2, where n is the number of elements in the array. ---Courtesy of a Quora Answer!

Split inversions are a great heuristic for measuring how optimum a sorting algorithm is.
More the number of split inversions a sorting algorithm removes in a single iteration of the array, the lower its complexity, and the higher its efficiency.
Learning Divide and Conquer Approach
'''

def count_inversions(arr):
  l = len(arr)
  mid = l//2
  inversions = 0

  if l == 1:
    return inversions, arr
  else:
    leftInversions, left = count_inversions(arr[:mid])
    rightInversions, right = count_inversions(arr[mid:])
    inversions+= (leftInversions+rightInversions)

    lLeft = len(left)
    lRight = len(right)
    k=j=0
    mergedArr = []

    for i in range(l):
      if j!= lLeft and k!= lRight:
        if left[j] <= right[k]:
          mergedArr.append(left[j])
          j+=1
        else:
          mergedArr.append(right[k])
          k+=1
          if j!= lLeft:
            inversions+=lLeft-j
      elif j == lLeft:
        mergedArr.append(right[k])
        k+=1
      elif k == lRight:
        mergedArr.append(left[j])
        j+=1
      
  return inversions, mergedArr

if __name__ == "__main__":
  main()
  
arr = [1, 5, 3, 2, 4, 6]
print(count_inversions(arr))
