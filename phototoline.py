from turtle import back


DENSITY = 2
PXSIZE = 10


def preamble(file, rows, cols):
    width = cols*PXSIZE
    height = rows*PXSIZE
    file.write("%!PS-Adobe-3.0 EPSF-3.0\n%%BoundingBox: " + str(0) + " " +str(0) + " " + str(width+PXSIZE*2) + " " + str(height+PXSIZE*2) + "                                         \n/maxlines " + str(DENSITY) + " def\n" + str(PXSIZE) + " " + str(PXSIZE) + " translate\n")
    print()

def genericPixel(file, pixel, x, y):
    pixel = pixel/256
    file.write(" "+ str(PXSIZE)+ " " + str(pixel)+ " " + str(y*PXSIZE- PXSIZE) + " " + str(x*PXSIZE) + " " + "pixel\n")


def rightRowEndPixel(file, pixel, x, y):
    pixel = pixel/256
    file.write(" "+ str(PXSIZE)+ " " + str(pixel)+ " " + str(y*PXSIZE- PXSIZE) + " " + str(x*PXSIZE) + " " + "rightRowEndPixel\n")

def rightRowBeginPixel(file, pixel, x, y):
    pixel = pixel/256
    file.write(" "+ str(PXSIZE)+ " " + str(pixel)+ " " + str(y*PXSIZE- PXSIZE) + " " + str(x*PXSIZE) + " " + "rightRowBeginPixel\n")

def leftRowEndPixel(file, pixel, x, y):
    pixel = pixel/256
    file.write(" "+ str(PXSIZE)+ " " + str(pixel)+ " " + str(y*PXSIZE- PXSIZE) + " " + str(x*PXSIZE) + " " + "leftRowEndPixel\n")

def leftRowBeginPixel(file, pixel, x, y):
    pixel = pixel/256
    file.write(" "+ str(PXSIZE)+ " " + str(pixel)+ " " + str(y*PXSIZE- PXSIZE) + " " + str(x*PXSIZE) + " " + "leftRowBeginPixel\n")

def fileEnd(file):
    file.write("showpage\n" + "%"+"EOF")



def main():
    print("===========================================================")
    print("phototoline.py. Created by Izzy Snyder in April 2022. Converts a pgm file into a continuous line drawing.")
    print("===========================================================")

    f = open("graduation.pgm", "rb")
    
    f.readline()
    firstLine = f.readline()
    firstLineList = firstLine.split()
    NUMCOLS = int(firstLineList[0])
    NUMROWS = int(firstLineList[1])
    f.readline()

    out = open("output.eps", "w")
    preamble(out, NUMROWS, NUMCOLS)

    out = open("output.eps", "a")
    backup = open("backup.eps", "r+")
    for line in backup:
        # append content to second file
        out.write(line)

    #on even rows, go left to right. On odd rows, go right to left
    for y in range(NUMROWS):
        for x in range(NUMCOLS):
            pixel = f.read(1)
            if pixel != "":
                pixel = ord(pixel)+1
                if x == 0: #start pixels

                    if y%2 == 0: #left start
                        leftRowBeginPixel(out,pixel,x,NUMROWS-y)
                    else: #right start
                        leftRowEndPixel(out,pixel,x,NUMROWS-y)
                elif x == NUMCOLS-1: #end pixels
                    if y%2 == 0: #right end
                        rightRowEndPixel(out,pixel,x,NUMROWS-y)
                    else: #left end
                        rightRowBeginPixel(out,pixel,x,NUMROWS-y)
                else: #middle pixels
                    genericPixel(out,pixel,x,NUMROWS-y)
    fileEnd(out)


main()