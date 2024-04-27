def max_talks_schedule(talks):
    # Sort the talks based on their end times
    sorted_talks = sorted(talks, key=lambda x: x[1])

    # Divide-and-conquer function
    def divide_and_conquer(start, end):
        if start >= end:
            return 0

        middle = (start + end) // 2
        count = 1  # Include the talk that ends at the middle time

        # Find talks that start after the middle
        next_talk = middle + 1
        while next_talk < len(sorted_talks) and sorted_talks[next_talk][0] < sorted_talks[middle][1]:
            next_talk += 1

        # Recursively solve the two subproblems
        count += divide_and_conquer(start, middle)
        count += divide_and_conquer(next_talk, end)

        return count

    # Start the divide-and-conquer process
    return divide_and_conquer(0, len(sorted_talks))

# Example usage:
# talk_proposals = [(1, 3), (2, 5), (5, 7), (4, 8), (6, 9)]
talk_proposals = [(1,4),(2,5),(5,7),(6,8),(7,9),(10,12),(11,20)]
result = max_talks_schedule(talk_proposals)
print("Maximum number of talks without overlaps:", result)
