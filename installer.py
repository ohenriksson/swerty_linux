dir = "/usr/share/X11/xkb/"
dir = "/home/oskar/Downloads/swerty-linux/swerty_linux"

evdev_search = "<layout>\n<configItem>\n<name>se</name>\n"
evdev_search += "<shortDescription>Swe</shortDescription>\n"
evdev_search += "<description>Sweden</description>\n"
evdev_search += "<languageList><iso639Id>swe</iso639Id></languageList>\n"
evdev_search += "</configItem>\n"
evdev_search += "<variantList>\n"

evdev_newtext = "<variant>\n"
evdev_newtext += "<configItem>\n"
evdev_newtext += "<name>swerty</name>\n"
evdev_newtext += "<description>Swerty</description>\n"
evdev_newtext += "</configItem>\n"
evdev_newtext += "</variant>\n"

    #     
    #     
    #   </configItem>
    #   <variantList>'



def get_se_text(dir):
    f1 = open(dir, "r")
    if f1.mode != 'r':
        raise Exception("could not read " + dir)
    setxt = f1.read()
    f1.close()
    return setxt

def append_to_se(dir,text):
    f2 = open(dir, "a")
    if f2.mode != 'a':
        raise Exception("could not append to " + dir)
    f2.write(text)
    f2.close()
    
def replace_file_with(dir,new_text):
    f = open(dir, "w")
    if f.mode != 'w':
        raise Exception("could not write to " + dir)
    f.flush()
    f.write(new_text)
    f.close()

def fix_and_split(evdev_text, search_p, new_text):
    if ~evdev_text.find(search_p):
        raise Exception("could not find Swe layout! in ")
    splitted = evdev_text.split(search_p)
    [before,after] = evdev_text.split(search_p)

    evdev_fixed = before + evdev_search + new_text + after


print("")
print("Hello")
print (dir)
print("hello world")

setxt_dir = dir + "/se.txt"
se_txt = get_se_text(setxt_dir)

sefile_dir = dir + "/symbols/se"
append_to_se(sefile_dir, se_txt)

evdev_dir = dir + "/rules/evdev.xml"
evdev_text = get_se_text(evdev_dir)

result_txt = fix_and_split(evdev_text, evdev_search, evdev_newtext)
replace_file_with(evdev_dir, result_txt)