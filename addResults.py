import re
# this script will add our results for fire maze
def take_results():
    f = open("test.txt", "r")
    results = [0,0,0]
    for lines in f:
        a = re.split(',|\[|\]|\n',lines)
        a = list(filter(None, a))


        for i in range(len(a)):
            a[i] = int(a[i])
            results[i] = results[i] + a[i]
    print(results)
    f.close()
    return results

def main():
    take_results()

if __name__ == "__main__":
    main()