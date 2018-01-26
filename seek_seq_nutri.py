from seqseek import Chromosome
from difflib import SequenceMatcher
from numpy import loadtxt
import json

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

#import Levenshtein
#Levenshtein.ratio('hello world', 'hello')

#upload genome text
with open("genomes/Genome_test.txt") as textFile:
    lines = [line.split() for line in textFile]

    print(lines[1])
    print(len(lines))
#search for the right gene

#create dictionary for data
data = {}
data['genes'] = []


#print gene next to these reference variaties
your_gene = lines[5518-1];
rs4654748 = { 'CC' : {'desc':'2.90 ng/mL lower Vitamin B6 blood concentration'},
              'CT' : {'desc':'1.45 ng/mL lower Vitamin B6 blood concentration'},
                'TT' : {'desc':'normal Vitamin B6 blood concentration'},
              }
if your_gene[3] == 'CC':
    result = rs10741657['CC']['desc']
elif your_gene[3] == 'CT':
    result = rs10741657['CT']['desc']
elif your_gene[3] == 'TT':
    result = rs10741657['TT']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs429358',
    'genotype': your_gene,
    'Chromosome': Chromosome(1).sequence(21786068,21786118),
    'result': result
})

print('Vitamin D: rs12794714, rs2060793')
your_gene = lines[369599-1];
print(your_gene)
rs10741657 = {'AA' : {'desc':'tend to have higher vitamin D levels'},
              'GG' : {'desc':'tend to have lower vitamin D levels'},
              }
if your_gene[3] == 'AA':
    result = rs10741657['AA']['desc']
elif your_gene[3] == 'GG':
    result = rs10741657['GG']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs12794714',
    'genotype': your_gene,
    'Chromosome': Chromosome(11).sequence(14913575,14913625),
    'result': result
})

your_gene = lines[269601-1];
rs10741657 = {'AA' : {'desc':'Lower serum levels of vitamin D'},
              'GG' : {'desc':'Higher serum levels of vitamin D'},
              }
if your_gene[3] == 'AA':
    result = rs10741657['AA']['desc']
elif your_gene[3] == 'GG':
    result = rs10741657['GG']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs2060793',
    'genotype': your_gene,
    'Chromosome': Chromosome(11).sequence(14915260,14915360),
    'result': result
})

print('B9: rs1801133, rs1801131, rs1801394')
your_gene = lines[2744-1];
rs12794714 = {'AA' : {'desc':'no data'},
              'AC' : {'desc':'Possibly impaired folate metabolism'},
              'CC' : {'desc':'Number of risks. Complex.'},
              }
if your_gene[3] == 'AA':
    result = rs12794714['AA']['desc']
elif your_gene[3] == 'AC':
    result = rs12794714['AC']['desc']
elif your_gene[3] == 'CC':
    result =rs12794714['CC']['desc']
else:
    result = 'no match found'
data['genes'].append({
    'name': 'rs12794714',
    'genotype': your_gene,
    'Chromosome': Chromosome(1).sequence(11856328, 11856428),
    'result': result
})

print('rs1801131')
print(Chromosome(1).sequence(11854426, 11854526))
your_gene = lines[2721];
rs1801131 = {'AA' : {'desc':'no data'},
              'AC' : {'desc':'Possibly impaired folate metabolism'},
              'CC' : {'desc':'Number of risks. Complex.'},
              }
if your_gene[3] == 'AA':
    result = rs1801131['AA']['desc']
elif your_gene[3] == 'AC':
    result = rs1801131['AC']['desc']
elif your_gene[3] == 'CC':
    result = rs1801131['CC']['desc']
else:
    print 'no match found'
data['genes'].append({
    'name': 'rs1801131',
    'genotype': your_gene,
    'Chromosome': Chromosome(1).sequence(11854426, 11854526),
    'result': result
})


print('rs1801394')
print(Chromosome(1).sequence(237048450, 237048550))
your_gene = lines[170410-1];
rs1801131 = {'AA' : {'desc':'normal'},
              'AC' : {'desc':'normal'},
              'CC' : {'desc':'1.4x higher risk for meningiomas'},
              }
if your_gene[3] == 'AA':
    print(rs1801131['AA']['desc'])
elif your_gene[3] == 'AC':
    result = rs1801131['AC']['desc']
elif your_gene[3] == 'CC':
    result = rs1801131['CC']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs1801394',
    'genotype': your_gene,
    'Chromosome': Chromosome(1).sequence(237048450, 237048550),
    'result': result
})

print('#Retinol conversion: rs7501331, rs12934922')
your_gene = lines[499502-1];
rs7501331 = {'CC' : {'desc':'normal'},
              'CT' : {'desc':'Reduced conversion of beta-carotene to retinol'},
              'TT' : {'desc':'Reduced conversion of beta-carotene to retinol'},
              }
if your_gene[3] == 'CC':
    result = rs7501331['CC']['desc']
elif your_gene[3] == 'CT':
    result = rs7501331['CT']['desc']
elif your_gene[3] == 'TT':
    result = rs7501331['TT']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs7501331',
    'genotype': your_gene,
    'Chromosome': Chromosome(16).sequence(81314446, 81314546),
    'result': result
})

print('rs12934922')
your_gene = lines[499498-1];
print(your_gene)
print(Chromosome(16).sequence(81301644, 81301744))
rs12934922 = {'CC' : {'desc':'normal'},
              'CT' : {'desc':'Reduced conversion of beta-carotene to retinol'},
              'TT' : {'desc':'Reduced conversion of beta-carotene to retinol'},
              }
if your_gene[3] == 'CC':
    result = rs12934922['CC']['desc']
elif your_gene[3] == 'CT':
    result = rs12934922['CT']['desc']
elif your_gene[3] == 'TT':
    result = rs12934922['TT']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs12934922',
    'genotype': your_gene,
    'Chromosome': Chromosome(16).sequence(81301644, 81301744),
    'result': result
})


print('#B12: rs602662, rs492602')
print('rs602662')
print(Chromosome(19).sequence(49206935, 49207035))
your_gene = lines[549869-1];
print(your_gene)
rs602662 = {'AA' : {'desc':'Higher vitamin B12 levels'},
              'GG' : {'desc':'Lower vitamin B12 levels'},
              }
if your_gene[3] == 'AA':
    result = rs602662['AA']['desc']
elif your_gene[3] == 'GG':
    result = rs602662['AC']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs602662',
    'genotype': your_gene,
    'Chromosome': Chromosome(19).sequence(49206935, 49207035),
    'result': result
})

print('rs492602')
print(Chromosome(19).sequence(49206367, 49206467))
your_gene = lines[549859-1];
print(your_gene)
rs602662 = {'CC' : {'desc':'Higher B12 levels in women'},
              'CT' : {'desc':'Normal B12 levels'},
                'TT' : {'desc':'Lower vitamin B12 levels'},
              }
if your_gene[3] == 'CC':
    result = rs602662['CC']['desc']
elif your_gene[3] == 'CT':
    result = rs602662['CT']['desc']
elif your_gene[3] == 'TT':
    result = rs602662['TT']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs492602',
    'genotype': your_gene,
    'Chromosome': Chromosome(19).sequence(49206367, 49206467),
    'result': result
})

print('#Choline/PEMT: rs4646406, rs7946, rs12325817')
print('rs4646406')
print(Chromosome(17).sequence(17417119, 17417219))
your_gene = lines[549869];
data['genes'].append({
    'name': 'rs4646406',
    'genotype': your_gene[3],
    'Chromosome': Chromosome(17).sequence(17417119, 17417219),
    'result': 'no data'
})
your_gene = lines[555782];
print(your_gene)
data['genes'].append({
    'name': 'rs7946',
    'genotype': your_gene[3],
    'Chromosome': Chromosome(17).sequence(17417119, 17417219),
    'result': 'no data'
})

your_gene = lines[555782];
print(your_gene)
data['genes'].append({
    'name': 'rs12325817',
    'genotype': 'not found',
    'Chromosome': Chromosome(17).sequence(17486469, 17486569),
    'result': 'no data'
})


print('#Zinc: rs13266634')
your_gene = lines[555782];
print(your_gene)
data['genes'].append({
    'name': 'rs12325817',
    'genotype': 'not found',
    'Chromosome': Chromosome(1).sequence(118184733, 118184833),
    'result': 'no data'
})


print('#Glutathione: rs1695')#Glutathione: rs1695
your_gene = lines[379343];
rs1695 = {'AA' : {'desc':'normal asthma risk in certain populations'},
              'GA' : {'desc':'No data'},
                'GG' : {'desc':'3.5x asthma risk in certain populations'},
              }
if your_gene[3] == 'AA':
    result = rs1695['AA']['desc']
elif your_gene[3] == 'CT':
    result = rs1695['GA']['desc']
elif your_gene[3] == 'TT':
    result = rs1695['GG']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs1695',
    'genotype': your_gene,
    'Chromosome': Chromosome(11).sequence(67352639, 67352739),
    'result': result
})


print('#Monounsaturated fats: rs17300539')
your_gene = lines[131233];
rs17300539 = {'AA' : {'desc':'higher adiponectin levels'},
              'AG' : {'desc':'if obese, dieting more effective'},
                'GG' : {'desc':'increased risk of insulin resistance'},
              }
if your_gene[3] == 'AA':
    result = rs17300539['AA']['desc']
elif your_gene[3] == 'AG':
    result = rs17300539['AG']['desc']
elif your_gene[3] == 'GG':
    result = rs17300539['GG']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs17300539',
    'genotype': your_gene,
    'Chromosome': Chromosome(3).sequence(186559410, 186559510),
    'result': result
})

print('#PUFAs: rs1535, rs3135506, rs662799')
your_gene = lines[378210-1];
rs1535 = {'AA' : {'desc':'no data'},
              'AG' : {'desc':'4+ IQ points for breastfeeding'},
                'GG' : {'desc':'no data'},
              }
if your_gene[3] == 'AA':
    result = rs1535['AA']['desc']
elif your_gene[3] == 'AG':
    result = rs1535['AG']['desc']
elif your_gene[3] == 'GG':
    result = rs1535['GG']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs1535',
    'genotype': your_gene,
    'Chromosome': Chromosome(11).sequence(61597922, 61598022),
    'result': result
})

your_gene = lines[389869-1];

data['genes'].append({
    'name': 'rs3135506',
    'genotype': your_gene,
    'Chromosome': Chromosome(11).sequence(116662357, 116662457),
    'result': 'no data'
})

your_gene = lines[389874-1];
rs662799 = {'AA' : {'desc':'normal'},
              'AG' : {'desc':'1.4x higher early heart attack risk; less weight gain on high fat diets'},
                'GG' : {'desc':'2x higher early heart attack risk; less weight gain on high fat diets'},
              }
if your_gene[3] == 'AA':
    result = rs662799['AA']['desc']
elif your_gene[3] == 'AG':
    result = rs662799['AG']['desc']
elif your_gene[3] == 'GG':
    result = rs662799['GG']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs662799',
    'genotype': your_gene,
    'Chromosome': Chromosome(11).sequence(116663657, 116663757),
    'result': result
})

print('#Saturated fats: rs5082, rs3135506, rs1137101')
your_gene = lines[14180-1];
rs5082 = {'AA' : {'desc':'saturated fat contributes to obesity, but 0.57 % lower risk for coronary artery disease'},
              'AG' : {'desc':'normal risk'},
                'GG' : {'desc':'normal risk'},
              }
if your_gene[3] == 'AA':
    result = rs5082['AA']['desc']
elif your_gene[3] == 'AG':
    result = rs5082['AG']['desc']
elif your_gene[3] == 'GG':
    result = rs5082['GG']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs5082',
    'genotype': your_gene,
    'Chromosome': Chromosome(1).sequence(161193633, 161193733),
    'result': result
})

your_gene = lines[389869-1];

data['genes'].append({
    'name': 'rs3135506',
    'genotype': your_gene,
    'Chromosome': Chromosome(1).sequence(116662357, 116662457),
    'result': 'NO DATA'
})

your_gene = lines[14180-1];
rs1137101 = {'AA' : {'desc':'common in clinvar'},
              'AG' : {'desc':'Slight increase in obesity and T2DM risk'},
                'GG' : {'desc':'Slight increase in obesity and T2DM risk'},
              }
if your_gene[3] == 'AA':
    result = rs1137101['AA']['desc']
elif your_gene[3] == 'AG':
    result = rs1137101['AG']['desc']
elif your_gene[3] == 'GG':
    result = rs1137101['GG']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs1137101',
    'genotype': your_gene,
    'Chromosome': Chromosome(1).sequence(66058463, 66058563),
    'result': result
})

print('#APOE4: rs429358')
your_gene = lines[548954-1];
rs429358 = {'CC' : {'desc':'one of 2 snps relevant to classifying APOE genotype'},
              'CT' : {'desc':'>3x increased risk for Alzheimers; 1.4x increased risk for heart disease'},
                'TT' : {'desc':'Slight increase in obesity and T2DM risk'},
              }
if your_gene[3] == 'CC':
    result = rs429358['CC']['desc']
elif your_gene[3] == 'CT':
    result = rs429358['CT']['desc']
elif your_gene[3] == 'TT':
    result = rs429358['TT']['desc']
else:
    result = 'no match found'

data['genes'].append({
    'name': 'rs429358',
    'genotype': your_gene,
    'Chromosome': Chromosome(19).sequence(45411891, 45411991),
    'result': result
})

print(json.dumps(data))

# chart absorption ability for each
