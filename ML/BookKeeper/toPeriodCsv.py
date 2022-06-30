import sys;

if (len (sys.argv) != 2):
    print("Usage: " + sys.argv[0] + " <filepath>")
    exit(1)

filename = sys.argv[1]

f = open(filename, "rt")
data = f.read()

data = data.replace(",", ".")
data = data.replace("NaN", "0")
f.close()

fout = open(filename, "wt")
fout.write(data)
fout.close()