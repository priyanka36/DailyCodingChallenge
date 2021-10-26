def numbers(num_lst):
    for i in range(len(num_lst)):
        for j in range(i+1,len(num_lst)):
            if j+1<len(num_lst):
                if num_lst[i] == num_lst[j]+ num_lst[j+1]:
                    print("There is a number")
                else:
                    print("There aren't any numbers")

if __name__ == "__main__":
    numbers([12,13,1,3,18])