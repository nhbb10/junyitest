def count_with_filter(input_number):
    count = 0
    for i in range(1, input_number+1, 1):
        if ((i%3 == 0) and (i% 5 == 0)) or ((i%3 != 0) and (i% 5 != 0)):
            count += 1
    return count

if __name__ == "__main__":
    count_with_filter(15)


