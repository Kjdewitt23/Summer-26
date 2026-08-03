'''make sure presidents.txt and BLS_private.csv are in the same folder as fact_check.py and run this module in the terminal to see the results'''

def main():
    start_line = 13
    republican = 0
    democrat = 0
    presidents = {}

    # Read txt file and create dictionary with key of year and value of president's party. Encoding removes starting characters found in .txt files
    with open("presidents.txt", "r", encoding="utf-8-sig") as pres:
        for line in pres:
            year, party = line.strip().split()
            presidents[int(year)] = party

    # Read BLS data and create list of jobs created then update republican or democrat totals
    with open("BLS_private.csv", "r") as jobs:
        for line_num, line in enumerate(jobs):
            if line_num >= start_line:
                row = line.strip().split(",")

                year = int(row[0])
                # checks if bls data has an empty month or any that can't be inherently converted into an int
                total_jobs = sum(int(x) if x else 0 for x in row[1:])

                if presidents[year] == "Republican":
                    republican += total_jobs
                else:
                    democrat += total_jobs
        print(f"Total jobs for Republicans: {republican}")
        print(f"Total jobs for Democrats: {democrat}")

        if republican > democrat:
            print("Clinton was wrong")
        else:
            print("Clinton was correct")

if __name__ == "__main__":
    main()
