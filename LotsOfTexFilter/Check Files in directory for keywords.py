import os
directory="C:/Users/AAZ/Desktop/Drive/Tech/Scripting/Python/FirKit/Web Recon/AllRedditCommentHistories/"

wordlist=["twitter","facebook","email","@"]

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file=os.path.join(directory,filename)
        with open(file,"r") as r:
            allLines = r.readlines()
            for counter,line in enumerate(allLines):
                for word in wordlist:
                    if word in line.lower():
                        print("[+] Found "+word+" at line ["+str(counter)+"] in file ["+filename+"]")
                        print("    "+line)
