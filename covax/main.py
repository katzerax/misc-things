#function findMatches which can be called with parameters query and values
def findMatches(query, values):
    #function findDifference which uses the query and values parameters from findMatches
    def findDifference(query, values):
        #variable n to store length of array
        n = len(values)
        #firstMatchIndex calls on function first to find first location of query in array
        firstMatchIndex = first(values, 0, n-1, query, n)
        #lastMatchIndex calls on function last to find last location of query in array
        lastMatchIndex = last(values, firstMatchIndex, n-1, query, n);
        #numberOfMatches calculates the total number of indexes with query's value by finding the difference of first and last
        numberOfMatches = lastMatchIndex-firstMatchIndex+1;
        #checks to see numberOfMatches has a valid number
        if numberOfMatches !=-1:
            #if number is valid, returns numberOfMatches, firstMatchIndex as prompt intends.
            return (numberOfMatches, firstMatchIndex)
        #if number is invalid, returns -1
        else:
            return(-1)
    #function first uses a binary search to find the first instance of query in the array
    def first(values, low, high, query, n):
            #checks if length of array is greater than or equal to 0
            if high >= low:
                #finds the middle index and sets that value to mid
                mid = (low + high)//2
            #checks if mid value is 0 or if query value is higher than the number to the left index that it checked and that the current mid value is equal to the query
            if (mid == 0 or query > values[mid-1]) and values[mid] == query:
                #if above is true then mid is the first instance of the query in the array, returns that
                return mid
            #checks if the query is higher than the currently checked index
            elif query > values[mid]:
                #checks the value to the right of current index
                return first(values, (mid + 1), high, query, n)
            #if above if and elif statements don't work, checks the value to the left of current index
            else:
                return first(values, low, (mid -1), query, n)
            #if all else fails, returns -1
            return -1;
    #function last uses a binary search to find the last instance of query in the array
    def last(values, low, high, query, n):
            #checks if length of array is greater than or equal to 0
            if high >= low:
                #finds the middle index and sets that value to mid
                mid = (low + high)//2;
            #checks if mid value is 1 less than length of array or if query value is less than the number to the right index that it checked and that the current mid value is equal to the query
            if(mid == n-1 or query < values[mid+1]) and values[mid] == query :
                #if above is true then mid is the last instance of the query in the array, returns that
                return mid
            #checks if the query is lower than the currently checked index
            elif query < values[mid]:
                #checks the value to the left of current index
                return last(values, low, (mid -1), query, n)
            #if above if and elif statements don't work, checks the value to the right of current index
            else:
                return last(values, (mid + 1), high, query, n)
            #if all else fails, returns -1
            return -1
    #calls findDifference for findMatches, allows all of the above functions to be confined within findMatches
    return findDifference(query, values)
#example array that can be replaced
values = [1, 2, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 9]
#prints to console the result of query 7 and the array list above marked as values, console is formatted as (numberOfMatches, firstMatchIndex)
print(findMatches(5, values))
