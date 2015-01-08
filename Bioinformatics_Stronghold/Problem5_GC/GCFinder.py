class GCFinder:
    gcContent = {}
    def __init__(self, dataset):
        self.data = dataset

    def store(self):
        name = ""
        for line in self.data:
            if line.find("Rosalind_") > 0:
                name = line
                self.gcContent[name] = ""
            else:
                self.gcContent[name] = self.gcContent[name] + line.rstrip()

    def find(self):
        label = ""
        topGC = 0.0

        for content in self.gcContent:
            strand = self.gcContent[content]
            count = 0.0
            for character in strand:
                if character == "C" or character == "G":
                    count = count + 1
            gc = count / len(strand)
            if gc > topGC:
                topGC = gc
                label = content
        return label, topGC
