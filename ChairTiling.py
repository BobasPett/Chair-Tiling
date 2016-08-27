
import math 

class Path(object):
    svgPath=""

def lineTo(x, y):
    return """ L """ + str(x) + """ """ + str(y) + """ """


def moveTo(x, y):
    return """ M """ + str(x) + """ """ + str(y) + """ """


def getPath(coord,color):
    pathStr = """<path d=""" + """ " """
    pathStr += moveTo(coord[0][0], coord[0][1])
    for i in range(len(coord)):
        if i!=0:
            pathStr+=lineTo(coord[i][0], coord[i][1])           
    pathStr+=lineTo(coord[0][0], coord[0][1])
    pathStr+= """  Z" fill=" """+color+"""  "  """ """stroke="black" stroke-width="3"/>"""
    return pathStr

def getPink(x,y,s):
    return ((x,y),(x,y+2*s),(x+s,y+2*s),(x+s,y+s),(x+2*s,y+s),(x+2*s,y))

def chair(path,s,color,deg):
    x=path[0][0]
    y=path[0][1]
    Path.svgPath+=getPath(path,color)
    if deg>0:
        #pink
        if color=="pink":
            #pink
            path=((x,y),(x,y+2*s),(x+s,y+2*s),(x+s,y+s),(x+2*s,y+s),(x+2*s,y))
            chair(path,s/2,"pink",deg-1)

            #blue
            path=((x+4*s,y),(x+2*s,y),(x+2*s,y+s),(x+3*s,y+s),(x+3*s,y+2*s),(x+4*s,y+2*s))
            chair(path,s/2,"blue",deg-1)

            #pink
            path=((x+s,y+s),(x+s,y+3*s),(x+2*s,y+3*s),(x+2*s,y+2*s),(x+3*s,y+2*s),(x+3*s,y+s))
            chair(path,s/2,"pink",deg-1)

            #green
            path=((x,y+4*s),(x,y+2*s),(x+s,y+2*s),(x+s,y+3*s),(x+2*s,y+3*s),(x+2*s,y+4*s))
            chair(path,s/2,"green",deg-1)

        #purple
        if color=="purple":
            #purple
            path=((x,y),(x,y-2*s),(x-s,y-2*s),(x-s,y-s),(x-2*s,y-s),(x-2*s,y))
            chair(path,s/2,"purple",deg-1)

            #purple
            path=((x-s,y-s),(x-s,y-3*s),(x-2*s,y-3*s),(x-2*s,y-2*s),(x-3*s,y-2*s),(x-3*s,y-s))
            chair(path,s/2,"purple",deg-1)

            #green
            path=((x-4*s,y),(x-2*s,y),(x-2*s,y-s),(x-3*s,y-s),(x-3*s,y-2*s),(x-4*s,y-2*s))
            chair(path,s/2,"green",deg-1)

            #blue
            path=((x,y-4*s),(x,y-2*s),(x-s,y-2*s),(x-s,y-3*s),(x-2*s,y-3*s),(x-2*s,y-4*s))
            chair(path,s/2,"blue",deg-1)

        #green
        if color=="green":
            #green
            path=((x,y),(x,y-2*s),(x+s,y-2*s),(x+s,y-s),(x+2*s,y-s),(x+2*s,y))
            chair(path,s/2,"green",deg-1)

            #green
            path=((x+s,y-s),(x+s,y-3*s),(x+2*s,y-3*s),(x+2*s,y-2*s),(x+3*s,y-2*s),(x+3*s,y-s))
            chair(path,s/2,"green",deg-1)

            #purple
            path=((x+4*s,y),(x+2*s,y),(x+2*s,y-s),(x+3*s,y-s),(x+3*s,y-2*s),(x+4*s,y-2*s))
            chair(path,s/2,"purple",deg-1)

            #pink
            path=((x,y-4*s),(x,y-2*s),(x+s,y-2*s),(x+s,y-3*s),(x+2*s,y-3*s),(x+2*s,y-4*s))
            chair(path,s/2,"pink",deg-1)
            
        #blue
        if color=="blue":
            #blue
            path=((x,y),(x,y+2*s),(x-s,y+2*s),(x-s,y+s),(x-2*s,y+s),(x-2*s,y))
            chair(path,s/2,"blue",deg-1)

            #pink
            path=((x-4*s,y),(x-2*s,y),(x-2*s,y+s),(x-3*s,y+s),(x-3*s,y+2*s),(x-4*s,y+2*s))
            chair(path,s/2,"pink",deg-1)

            #blue
            path=((x-s,y+s),(x-s,y+3*s),(x-2*s,y+3*s),(x-2*s,y+2*s),(x-3*s,y+2*s),(x-3*s,y+s),)
            chair(path,s/2,"blue",deg-1)

            #purple
            path=((x,y+4*s),(x,y+2*s),(x-s,y+2*s),(x-s,y+3*s),(x-2*s,y+3*s),(x-2*s,y+4*s))
            chair(path,s/2,"purple",deg-1)


def main():
    width = 500
    height = 500
    stringW = """ width=" """ + str(width) + """ " """  # "w="width" "
    stringH = """ height=" """ + str(height) + """ " """  # "h="height" "
    svgStart = """<svg""" + stringW + """ """ + stringH + """>"""
    svgEnd = """</svg>"""
    svgPathStart= """<path d=""" + """ " """
    svgPathEnd= """Z"/>"""
    
    scale=width/4
    coordinates=getPink(1,1,scale)
    path=svgStart
    chair(coordinates,scale,"pink",5)
    path+=Path.svgPath
    path+=svgEnd
    print (path)


main()
