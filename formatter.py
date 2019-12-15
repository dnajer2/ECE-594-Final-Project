def main():
    r1=["q", "w", "e", "r", "t", "y", "u", "i","o", "p"]
    r2=["a", "s", "d", "f", "g", "h", "j", "k","l"]
    r3=["z", "x", "c", "v", "b", "n", "m"]

    fname=input("Keyboard name: ")


    f=open(fname +".txt","w+")
    cs=open("Character Spikes", "r")

    c1=cs.readlines()
    for x in c1:
        temp=(x.split())
        if temp[0] in r1:
            index=r1.index(temp[0])
            r1[index]=temp[0] + ": " + str("%.2f" % float(temp[3]))


        elif temp[0] in r2:
            index=r2.index(temp[0])
            r2[index]=temp[0] + ": " +str("%.2f" % float(temp[3]))

        elif temp[0] in r3:
            index=r3.index(temp[0])
            r3[index]=temp[0] + ": " +str("%.2f" % float(temp[3]))

    f.write(str(r1))
    f.write("\n")
    f.write(str(r2))
    f.write("\n")
    f.write(str(r3))

    f.close()
    cs.close()






if __name__ == "__main__":
    main()