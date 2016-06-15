import sys 
import BigInt

def PrintStart():
	print "Long_ariph <A filelame> <act> <B filelame> <result filename> [-b] [<mod filename>]"
	print "Ariph operations: + , -, * , / ,^, %"
	print "mod and binary key isn't required "
	sys.exit(-1)


f1 = sys.argv[1]
act = sys.argv[2]
f2 =sys.argv[3]
fres = sys.argv[4]
bin1 = "a"
fm = ""

if len(sys.argv) < 5 or len(sys.argv) > 7:
	print "Wrong number of args"
	PrintStart();

if len(sys.argv[2]) > 1:
	print "unknown act"
	PrintStart()
	 
if len(sys.argv) == 6:

	 if sys.argv[5] == "-b":
		 bin1  = "b";
	 else:
		 fm = sys.argv[5]

if len(sys.argv) == 7:
	bin1 = "b"
	fm = sys.argv[6]

print"f1 :",f1;
print"act :",act;
print"f2 :",f2;
print"fres :",fres;
print"bin1 :",bin1;
if fm:
	print"fm :",fm
ch1 = BigInt.BigInt()
ch2 = BigInt.BigInt()
res = BigInt.BigInt()

c = BigInt.BigInt()
c.amount = 1
#c.digits[0] = 0

ch1.input(f1,bin1)
ch2.input(f2,bin1)

if act == "+":
	if (ch1.sign == 1) and (ch2.sign == 0):
		if ch1 > ch2:
			res = ch1 - ch2
			res.sign = 1
		if ch1 <= ch2:
			res = ch2 - ch1
	if (ch1.sign == 0) and (ch2.sign == 0):
		res = ch1 + ch2
	if (ch1.sign == 0) and (ch2.sign == 1):
		if ch1 >= ch2:
			res = ch1 - ch2
		if ch1 < ch2:
			res = ch2 - ch1
			res.sign = 1
	if (ch1.sign == 1) and (ch2.sign == 1):
		res = ch2 + ch1
		res.sign = 1
elif act == "-":
	if (ch1.sign == 1) and (ch2.sign == 0):
		res = ch2 + ch1
		res.sign = 1
	if (ch1.sign == 0) and (ch2.sign == 0):
		if ch1 < ch2:
			res = ch2 - ch1
			res.sign = 1
		else:
			res = ch1 - ch2
	if (ch1.sign == 0) and (ch2.sign == 1):
		res = ch1 + ch2
		res.sign = 0
	if (ch1.sign == 1) and (ch2.sign == 1):
		res = ch2 - ch1
		if ch1 > ch2:
			res.sign = 1
elif act == "*":
	res = ch1 * ch2
	if ch1.sign != ch2.sign:
		res.sign = 1
elif act == "/":
	if ch2 == c:
		print "Error! Division on zero"
		sys.exit(-1)
	res = ch1 / ch2
	if ch1.sign != ch2.sign:
		res.sign = 1
elif act == "%":
	if ch2 == c:
		print "Error! Division on zero"
		sys.exit(-1)
	res = ch1 % ch2
elif act == "^":
	m = BigInt.BigInt()
	m.input(fm, bin1)
	if ch2.sign == 1:
		print "Degree must be greater than zero"
		sys.exit(-1)
	if m.sign == 1:
		print "Modul must be greater than zero"
		sys.exit(-1)
	if ch1.sign == 1:
		if ch2 % 2 != 0:
			res.sign = 1
	res = BigInt.binpow(ch1, ch2, m)
	if ch1.sign == 1:
		if ch2 % 2 != 0:
			res.sign = 1
else:
	PrintStart()

res.output(fres, bin1)
