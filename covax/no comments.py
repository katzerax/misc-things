def findMatches(query, values):
    def findDifference(query, values):
        n = len(values)
        firstMatchIndex = first(values, 0, n-1, query, n)
        lastMatchIndex = last(values, firstMatchIndex, n-1, query, n);
        numberOfMatches = lastMatchIndex-firstMatchIndex+1;
        if numberOfMatches !=-1:
            return (numberOfMatches, firstMatchIndex)
        else:
            return(-1)

    def first(values, low, high, query, n):
            if high >= low:
                mid = (low + high)//2
            if (mid == 0 or query > values[mid-1]) and values[mid] == query:
                return mid
            elif query > values[mid]:
                return first(values, (mid + 1), high, query, n)
            else:
                return first(values, low, (mid -1), query, n)
            return -1;

    def last(values, low, high, query, n):
            if high >= low:
                mid = (low + high)//2;
            if(mid == n-1 or query < values[mid+1]) and values[mid] == query :
                return mid
            elif query < values[mid]:
                return last(values, low, (mid -1), query, n)
            else:
                return last(values, (mid + 1), high, query, n)
            return -1
    return findDifference(query, values)

#example array that can be replaced
values = [1, 2, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 9]
print(findMatches(5, values))
