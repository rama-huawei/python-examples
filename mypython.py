import sys
def main():
    print "hello there", sys.argv[1]
    sys.exit(0)
    print len(sys.argv) - 1

if __name__ == '__main__':
    main()
