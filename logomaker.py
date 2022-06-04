import argparse
from PIL import Image, ImageDraw
import re

    
def xy_given_ratio(s,r):
    return [(s*r, s*r), (s*(1-r), s*(1-r))]

def calc_angle(character): 
    return ((ord(character)-65)*360/26-90, (ord(character)-65+1)*360/26-90)

def draw_arc(draw, s, r1, r2, letter):
    draw.ellipse(xy_given_ratio(s,r1), fill=0)
    draw.ellipse(xy_given_ratio(s,r2), fill=1)
    start_ang, stop_ang = calc_angle(letter)
    draw.pieslice(xy_given_ratio(s,r1-0.01), start_ang, stop_ang, fill=1)

def main():
    parser = argparse.ArgumentParser(description = "Make your own Jane Street inspired logos!")
    parser.add_argument('initials', type=str,
                        help = '3 letter initials for logo')
    parser.add_argument("-s", "--size", type = int, default = 500,
                        help = "Side length of output file")
    parser.add_argument("-o", "--output", type = str, default = 'logo.jpg', metavar='filename',
                        help = "Name of output file")
    args = parser.parse_args()  
    
    initials = args.initials.upper() 
    if(not (initials.isalpha() and len(initials)==3)):
        print('Initials are invalid, try again')
        return  
    filename = args.output
    print(args.output[-4:])
    if(not args.output[-4:] in ['.jpg', '.png', 'gif', '.bmp']):
        print('Filetype not supported, appending .jpg to filename')
        filename += '.jpg'
    

    img = Image.new('1', (args.size,args.size), 1)
    draw = ImageDraw.Draw(img)
    
    draw_arc(draw, args.size, 0.05, 0.11, initials[2])
    draw_arc(draw, args.size, 0.14, 0.20, initials[1])
    draw_arc(draw, args.size, 0.23, 0.29, initials[0])
    
    
    img.save(filename)
    print(f"Created image {filename} of size {args.size}x{args.size} with initials {initials}")


if __name__ == "__main__":
    main()