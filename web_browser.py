from flask import Flask
from seqseek import Chromosome

app = Flask(__name__)

@app.route('/')
def hello_world():

    string = 'Vitamin B6: rs4654748: '+Chromosome(1).sequence(21786068,21786118)+
    '/n Vitamin C: rs33972313:' + Chromosome(5).sequence(138715502,138715552)+
    '/n Vitamin D: rs12794714:'+Chromosome(11).sequence(14913575,14913625)+
    '/n Vitamin D: rs10741657:'+Chromosome(11).sequence(14914828,14914928)+
    '/n Vitamin D: rs2060793:'+Chromosome(11).sequence(14915260,14915360)+
    '/n Vitamin B9: rs1801133:'+Chromosome(11).sequence(14913575,14913625)+
    '/n Vitamin B9: rs1801131:'+Chromosome(1).sequence(11856328, 11856428)+
    '/n Vitamin B9: rs1805087:'+Chromosome(1).sequence(11854426, 11854526)+
    '/n Vitamin B9: rs1801394:'+Chromosome(1).sequence(237048450, 237048550)+
    '/n Vitamin D: rs12794714:'+Chromosome(11).sequence(14913575,14913625)+
    '/n Vitamin D: rs12794714:'+Chromosome(11).sequence(14913575,14913625)+
    '/n Vitamin D: rs12794714:'+Chromosome(11).sequence(14913575,14913625)+
    '/n Vitamin D: rs12794714:'+Chromosome(11).sequence(14913575,14913625)


    # print(': , , , ')
    # print()
    # print(X)
    # print()
    #
    # print('#Retinol conversion: rs7501331, rs12934922')
    # print(Chromosome(16).sequence(81314446, 81314546))
    # print(Chromosome(16).sequence(81301644, 81301744))
    #
    # print('#B12: rs602662, rs492602')
    # print(Chromosome(19).sequence(49206935, 49207035))
    # print(Chromosome(19).sequence(49206367, 49206467))
    #
    # print('#Choline/PEMT: rs4646406, rs7946, rs12325817')
    # print(Chromosome(17).sequence(17417119, 17417219))
    # print(Chromosome(17).sequence(17409510, 17409610))
    # print(Chromosome(17).sequence(17486469, 17486569))
    #
    # print('#B6: rs4654748')
    # print(Chromosome(1).sequence(21786018, 21786118))
    #
    # print('#Zinc: rs13266634')
    # print(Chromosome(1).sequence(118184733, 118184833))
    #
    # print('#Glutathione: rs1695')#Glutathione: rs1695
    # print(Chromosome(11).sequence(67352639, 67352739))
    #
    # print('#Monounsaturated fats: rs17300539')
    # print(Chromosome(3).sequence(186559410, 186559510))
    #
    # print('#PUFAs: rs1535, rs3135506, rs662799')
    # print(Chromosome(11).sequence(61597922, 61598022))
    # print(Chromosome(11).sequence(116662357, 116662457))
    # print(Chromosome(11).sequence(116663657, 116663757))
    #
    # print('#Saturated fats: rs5082, rs3135506, rs1137101')
    # print(Chromosome(1).sequence(161193633, 161193733))
    # print(Chromosome(1).sequence(116662357, 116662457))
    # print(Chromosome(1).sequence(66058463, 66058563))
    #
    # print('#APOE4: rs429358')
    # print(Chromosome(19).sequence(45411891, 45411991))

    return string
