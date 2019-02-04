import requests

sim = open("SimLex-999.txt", "r")
dict = open("eestiinglise.txt", encoding="utf8")
dictionary = {}

for i, line in enumerate(dict):
    try:
        words = line.split("\t")
        est = words[0].replace("-", "")
        ing = words[1].replace("-", "").split(",")
        for i in ing:
            dictionary[i] = est
    except Exception:
        print("viga " + i)


with open('output.txt', 'w') as output:
    for line in sim:
        words = line.split("\t")
        word1 = words[0]
        word2 = words[1]

        translated1 = dictionary.get(word1)
        translated2 = dictionary.get(word2)

        if translated2 is None:
            req = requests.post(
                "https://translation.googleapis.com/language/translate/v2?q=" + word2 + "&target=et&key"
                                                                                        "")
            json = req.json()
            try:
                d = json.get('data').get('translations')[0].get('translatedText')
                translated2 = d
            except Exception:
                print(word2)
                translated2 = "???"
        if translated1 is None:
            req = requests.post(
                "https://translation.googleapis.com/language/translate/v2?q=" + word1 + "&target=et&key"
                                                                                        "")
            json = req.json()
            try:
                d = json.get('data').get('translations')[0].get('translatedText')
                translated1 = d
            except Exception:
                print(word2)
                translated1 = "???"

        POS = words[2]
        SimLex999 = words[3]
        concw1 = words[4]
        concw2 = words[5]
        concQ = words[6]
        AssocUSF = words[7]
        SimAssoc333 = words[8]
        SD = words[9]
        output.write(
            word1 + "\t" + "" + word2 + "\t" + translated1 + "\t" + translated2 + "\t" + POS + "\t" + SimLex999 + "\t" + concw1 + "\t" + concw2 + "\t" + concQ + "\t" + AssocUSF + "\t" + SimAssoc333 + "\t" + SD)
        output.flush()

sim.close()
dict.close()

