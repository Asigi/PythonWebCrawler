import re
import urllib
from random import choice
import csv

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
    file.close()
    return myDict





#This function takes in the url which needs to be have its HTML scanned for links.
#It also takes in dictionaries that will be updated.
def crawl(url, urlDict):

    try:  # Get the webpage
        req = urllib.urlopen(url)
    except:
        try:
            req = urllib.request.urlopen(url)
        except:
            return urlDict #TODO, maaybe remove the troubling url?

    whole_string = str(req.read())
    
    
    results = []
    ahreflinks = []
    link_re = re.compile(r'a href\s?=\s?"http[s]?://\S*', re.I|re.M)
    ahreflinks = re.findall(link_re, whole_string) #get everything with 'a href' and 'http' in it
    #print(ahreflinks) #test
    #print("length of a href links is: ", len(ahreflinks)) #test
    
    for alink in ahreflinks:
        results.append(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', alink))


    words = []
    




    #Find and and add all the links
    for dlink in results:
        linkslist = urlDict.get(url)
        if dlink not in linkslist:
            #print("{0} is not in the dict for url {1}".format(dlink, url)) #test
            linkslist.append(dlink) #append to links for this url
            urlDict[url] = linkslist
            item = dlink.pop()
            if item not in urlDict.keys(): #add this to the available pages.
                urlDict[item] = []
                
    return urlDict




#The main function
def mymain():
    urlDict = makeDict() 
    urlCount = 0 #this is the number of pages scanned.
    usedURL_list = []

    wordDict = {} #holds the words.
    
    while urlCount <= len(urlDict):
        
        if urlCount == 100: #process a max of 100 sites.
            break;
        
        theChoice = choice(list(urlDict.keys()))
        print("choice is ", theChoice)
        if theChoice not in usedURL_list:
            #print("which is not in the list of used URLs") #test
            urlDict = crawl(theChoice, urlDict)
            
            print("size of links list of current url is: ", len(urlDict[theChoice])) #test
            usedURL_list.append(theChoice)
            print("size of dict is: ", len(urlDict)) #test
            urlCount = urlCount + 1
            print("urlCount is now at ", urlCount) #test


    writer = csv.writer(open('crawl.csv', 'wb'))
    for key, value in urlDict.items():
        writer.writerow([key, value])


            
#Find the main function
if __name__ == '__main__':
    mymain()






'''
sites = 'google yahoo cnn msn'.split()

pat = re.compile(r'<title>+.*</title>+', re.I|re.M)
#note that the + in the reg.express. requires atleast one occurance of the thing. Its dif than *
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

'''
def crawl(url, maxlevel):
    # Limit the recursion, we're not downloading the whole Internet
    if(maxlevel == 0):
        return
    
    # Get the webpage
    try:
        req = urllib.urlopen(url)
    except:
        req = urllib.request.urlopen(url)
    
    result = []

    # Find and follow all the links
    links = link_re.findall(str(req.read()))
    pastlink = ""
    for link in links:
        if link is not None:
            pastlink = str(link)
            print("link is: ", str(link))
            pastlink = link
            result += crawl(link, maxlevel - 1)

    return result
'''

#this is how links will be found
#link_re = re.compile(r'<a href="(http.*?)".*>', re.I|re.M)


#NOTE: website address must begin with HTTP or HTTPS

#r'<a href="(.*?)".*>(.*)</a>'
#NOTE: this re also gives me (<link here>, <linked word here>)


    #links = re.findall(r"\w+le", str(req.read()))
    #print(len(links))
    #r'<a href="(http.*?)".*>'

    
 #   links = re.findall('a href\s?=\s?"http[s]?://\S*', str(req.read()))

