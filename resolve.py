import re
import sys
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
    nThreads =  64 

    # no fancy argument processing :-/
    fileName = sys.argv[1]
    
    # loading all the query entries from the file
    lines = open(fileName).readlines()

    # number of lines assigned to earch worker depends
    # on the number of lines and threads
    nLines = len(lines)/nThreads

    # generating the desired number of workers for parallel processing
    pool = multiprocessing.Pool(processes=nThreads)

    # assinging blocks of nLines to each worker
    result_list = pool.map(processLines, 
                    (lines[line:line+nLines] for line in xrange(0,len(lines),nLines) ) )

    #result = {}
    #for e in result_list:
    #    for l in e:
    #        print l
