#https://docs.python.org/2/library/argparse.html

import argparse
def arg_parsing():
    parser = argparse.ArgumentParser(description='Test ArgumentParser')
    parser.add_argument("--input", required=True,
                        help='Input directory')
    args = parser.parse_args()
    args = vars(args)
    #args['input'] = os.path.abspath(args['input'])
    return args
    
def arg_parsing_v2(params):
    parser = argparse.ArgumentParser(description='Test ArgumentParser')
    for param in params:
        param='-'+str(param)
        parser.add_argument(param, required=True,
                            help='Input parammeter')
    args = parser.parse_args()
    args = vars(args)
    return args

#ARGS = arg_parsing()
#pathresultTVDI = ARGS['input']
#print(pathresultTVDI)

#python2 argu.py --txtinput "hello" --hallo "xin chao"
#python2 argu.py --input "/opt/lampp/htdocs/python/upload/0901201993905am_h1.tif" --hallo "xin chao"


params=['input','hallo','xinchao']
ARGS = arg_parsing_v2(params)

# python argu.py -input "input" -hallo "hallo" -xinchao "xinchao"

txtinput = ARGS['input']
print(txtinput)

hallo = ARGS['hallo']
print(hallo)

xinchao = ARGS['xinchao']
print(xinchao)