import re
import os
import unittest

#Claire Zuo 72712801

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """
    
    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')
    
    # Read the lines from the file object into a list
    lines = infile.readlines()
    
    # Close the file object
    infile.close()
    
    # return the list of lines
    return lines

def find_word(string_list):
    """ Return a list of words that contain three digit numbers in the middle. """
    newlist = []

    expression = r'(\b[a-zA-Z]+)\d\d\d([a-zA-Z]+)'

    # loop through each line of the string list
    for line in string_list:

    # find all the words that match the regular expression in each line
        first = re.findall(expression, line)
        for item in first:
            newlist.append(item)
    return newlist

def find_days(string_list):
    """ Return a list of days from the list of strings the dates format in the text are MM/DD/YYYY. """  

    # initialize an empty list
    listofdays = []

    # define the regular expression
    expressionn = r'\b\d*[\/](\d*)[\/]\d\d\d*'

    # loop through each line of the string list
    for line in string_list:

    # find all the dates that match the regular expression in each line
        findit = re.findall(expressionn, line)

    # loop through the found dates and only add the days to your empty list 
        for itemm in findit:
            listofdays.append(itemm[0:])

    #return the list of days
    return listofdays

def find_domains(string_list):
    """ Return a list of web address domains from the list of strings the domains of a wbsite are after www. """

    # initialize an empty list
    listfordomain = []

    # define the regular expression
    expression3 = r'^https?:[\/]+[a-zA-Z]+[.][a-zA-Z0-9\.]+'

    # loop through each line of the string list
    for line in string_list:

    # find all the domains that match the regular expression in each line
        findagain = re.findall(expression3, line)

    # loop through the found domains
        for domains in findagain:
    # get the domain name by splitting the (//) after the https or http to get the website name
    # then strip the www. to get only the domain name
            listfordomain= domains.split('//')
            q = listfordomain[1]
            w = q.strip('www.')
    # add the domains to your empty lists
            listfordomain.append(w)

    #return the list of domains
    return listfordomain

class TestAllMethods(unittest.TestCase):


    def test_find_word(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        word_list = find_word(string_list)
        self.assertEqual(len(word_list),4)
    
    def test_find_days(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        days_list = find_days(string_list)
        self.assertEqual(days_list,['23', '12', '31', '4', '1', '4'])
    
    def test_domains(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        domain_list = find_domains(string_list)
        self.assertEqual(domain_list,['pythex.org', 'si.umich.edu', 'sabapivot.com', 'stars.chromeexperiments.com', 'theofficestaremachine.com', 'regex101.com'])


def main():
	# Use main to test your function. 
    # Run unit tests, but feel free to run any additional functions you need
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()