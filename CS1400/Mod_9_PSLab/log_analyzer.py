with open("server_logs.txt", "r") as logs, open("log_summary.txt", "w") as file_out:
    types = {}
    longest_mes = ""
    for line in logs:
        '''counts the number of times each message type is present in the logs'''
        new_line = line.split("|")
        if new_line[0] not in types:
            types[new_line[0]] = 1
        else:
            types[new_line[0]] += 1

        if len(new_line[1]) > len(longest_mes):
            '''compares message length while iterating through the lines'''
            longest_mes = new_line[1]
    file_out.write("Log Summary\n")

    for item in types:
        file_out.write(f"{item}: {types[item]}\n") #I was trying to access the dictionary like a list and the output was wrong obviously. It took me a little debugging to remember you access elements of a dict by calling dict[key]
    
    file_out.write(f"Longest message: {longest_mes}")