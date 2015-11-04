def dessniping():
	#Starting bits
	rsbin = "10101010110011011110111100010010"
	#from the E bit selection table
	ebit = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
	ebox = ""
	for i in ebit:
		ebox += rsbin[i-1]
	print "EBOX:"
	print ebox
	print "\n"

	#turning the ebox and xorkey into lists because we can only xor with integers
	eboxlist = list(ebox)
	xorkey = "000100100011010001010110011110001001101010111100"
	xorlist = list(xorkey)
	xoroutput1 =0
	xoroutput = ""
	#XORing the ebox and the key that was given and appending the output to a string
	for w in range(len(ebox)):
		xoroutput1 = int(eboxlist[w]) ^ int(xorlist[w])
		xoroutput += str(xoroutput1)
	print "XOR:"
	print xoroutput

dessniping()