from yargy import Parser 
from yargy.morph import MorphAnalyzer
from yargy.tokenizer import MorphTokenizer

def findINN(text):
    import data.inn
    parser = Parser(data.inn.INNORG)
    matches = list(parser.findall(text))
    ret = []
    y = [_.fact for _ in matches]
    for i in y:
        z = {}
        z['num'] = i.num
        ret = ret + [z]
    if ret:
        return ret


def findDATECOAST(text):
    import data.datecoast
    parser = Parser(data.datecoast.DATECOASTCASE)
    matches = list(parser.findall(text))
    ret = []
    y = [_.fact for _ in matches]
    for i in y:
        z = {}
        z['day'] = i.day
        z['month'] = i.month
        z['year'] = i.year
        ret = ret + [z]
    if ret:
        return ret



def findDATECONT(text):
    import data.datecont
    parser = Parser(data.datecont.DATECONT)
    matches = list(parser.findall(text))
    ret = []
    y = [_.fact for _ in matches]
    for i in y:
        z = {}
        z['day'] = i.day
        z['month'] = i.month
        z['year'] = i.year
        ret = ret + [z]
    if ret:
        return ret



def findNCOASTCASE(text):
    import data.ncoast
    parser = Parser(data.ncoast.NCOASTCASE)
    matches = list(parser.findall(text))
    ret = []
    y = [_.fact for _ in matches]
    for i in y:
        z = {}
        z['first'] = i.first
        z['second'] = i.second
        z['third'] = i.third
        ret = ret + [z]
    if ret:
        return ret


def findNCONTRACT(text):
    import data.ncont
    parser = Parser(data.ncont.NCONTRACT)
    matches = list(parser.findall(text))
    ret = []
    y = [_.fact for _ in matches]
    for i in y:
        z = {}
        z['num'] = i.num
        ret = ret + [z]
    if ret:
        return ret 
