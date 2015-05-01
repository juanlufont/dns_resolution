#!/usr/bin/python

import re
import sys
import argparse
import dns.resolver
import multiprocessing



def processLines(lines):
    """ Resolves the DNS querys
    The functon receives a list of lines
    and construct queries based on the domain and type of
    DNS record associated to it
    """
    #result = []

    for l in lines:
        parts = l.split('.')
        # getting the domain to be resolved
        domain = re.sub(parts[-1], '', l)
        # getting the type of DNS record, cleaning whitespaces
        r_type = parts[-1].strip()
        
        # minimal error/exception handling
        try:
            q = dns.resolver.query(domain,r_type, raise_on_no_answer=False)
            # if the query successes, we just get the response in plain text
            r = q.rrset.to_text()
        except:
            # quick and dirty error message when query fails
            r = domain + " query error" 
        finally:
            #result.append(r)
            # just writing on the stdout
            print r
            # forcing the appliation to flush stdout
            sys.stdout.flush()
           
    return 1 



if __name__ == '__main__':
    """
    The application receives as input a file with the querys and
    prints on the standard output the DNS resolution for each query
    """

    parser = argparse.ArgumentParser(description='Resolves DNS queries from a given file')
    parser.add_argument('fileName', action='store', type=str, 
                        help='file containing the DNS queries')
    parser.add_argument('-t', dest='nThreads', action='store',
                        type=int, default=4, required=False,
                        help='number of parallel threads that will process the query file')
    #parser.add_argument('-o', dest='outputFile', action='store',
    #                    type=str, required=False,
    #                    help='output file')


    args = parser.parse_args()

    nThreads =  args.nThreads 
    fileName = args.fileName 
    
    # loading all the query entries from the file
    lines = open(fileName).readlines()

    # number of lines assigned to earch worker depends
    # on the number of lines and threads
    nLines = len(lines)/nThreads

    # generating the desired number of workers for parallel processing
    pool = multiprocessing.Pool(processes=nThreads)

    # assinging blocks of nLines to each worker
    try:
        # timeout as trick to get Ctrl+C working
        result_list = pool.map_async(processLines, 
                    (lines[line:line+nLines] for line in xrange(0,len(lines),nLines) ) ).get(9999999)
    except KeyboardInterrupt:
        pool.terminate()
        sys.exit(1)

    #result = {}
    #for e in result_list:
    #    for l in e:
    #        print l
