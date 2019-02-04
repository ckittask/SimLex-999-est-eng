sim = open("output.txt", "r")
with open("SimLex-999-eng-est.txt", "w") as output:
    for line in sim:
        words = line.split("\t")
        feng1 = words[0]
        feng2 = words[2]
        first = words[1]
        second = words[3]
        POS = words[4]
        SimLex999 = words[5]
        concw1 = words[6]
        concw2 = words[7]
        concQ = words[8]
        AssocUSF = words[9]
        SimAssoc333 = words[10]
        SD = words[11]
        output.write(
            feng1 + "\t" + feng2 + "\t" + first + "\t" + second + "\t" + POS + "\t" + SimLex999 + "\t" + concw1 +
            "\t" + concw2 + "\t" + concQ + "\t" + AssocUSF + "\t" + SimAssoc333 + "\t" + SD)
        output.flush()
sim.close()
output.close()
