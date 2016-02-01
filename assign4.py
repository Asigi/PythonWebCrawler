import re
import urllib

try:
    import urllib.request
except:
    pass




#This function reads in the list of urls that are provided.
#It then adds those URLs to a Dictionary as keys with empty arrays as values.
#Returns a dictionary {URL: [list of links]}
def makeDict():
    file = open("urls.txt", "r")
    myDict = {}
    for aline in file:
        myDict[aline] = []
    return myDict



#The main function
def mymain():
    urlDict = makeDict()
    print("in main")
    print(urlDict)



#Find the main function
if __name__ == '__main__':
    mymain()






'''
sites = 'google yahoo cnn msn'.split()

pat = re.compile(r'<title>+.*</title>+', re.I|re.M)

for s in sites:
    print ('Searching: ' + s)
    try:
        u = urllib.urlopen('http://' + s + '.com')
    except:
        u = urllib.request.urlopen('http://' + s + '.com')
    text = u.read()
    title = re.findall(pat, str(text))
    print(title[0])
'''
