DAYS = 7
def main():
    total_rocks = 0
    rocks = 0
    count = 0
    for count in range(1, DAYS):
        print("How many rocks did you collect on day # ", count, ": ")
        rocks = input()
        total_rocks += int(rocks)
    print("You collected ", total_rocks, " this week!")
main()