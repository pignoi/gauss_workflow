def checkFile(infile):
    with open(infile) as f:
        lines = f.readlines()
        for line in lines[-1:-5:-1]:
            if "Normal termination" in line:
                return 1
        
    return 0

if __name__ == "__main__":
    a = checkFile("/Users/cxmac/Desktop/78_data.log")
    print(a)
