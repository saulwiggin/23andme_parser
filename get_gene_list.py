from flask import Flask,json
from genome import Genome

app = Flask(__name__)

@app.route("/getGeneList")
def getgeneList():

    try:

        # Initialize a gene list
        geneList = []

        #upload genomes
        f = open('genomes/Genome_test.txt', 'r')
        f.read()
        my_genome = loadtxt('genomes/Genome_test.txt')
        print(my_genome)

        # create a instances for filling up gene list
        for i in range(0,610526):
            gene = gene(my_genome.rsid,my_genome.chromosome,my_genome.position,my_genome.genotype)
            geneList.append(gene)



    # convert to json data
        jsonStr = json.dumps([e.toJSON() for e in geneList])

    except:
        print "error ", sys.exc_info()[0]

    return jsonStr

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6666)
