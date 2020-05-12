import random
import os
H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

text1 = B+"""
                                                                                 
   """+F+'Author: '+W+'iXacknet'+B+"""                            
 \\    //      /\      //////  ||  //
  \\  //      //\\     ||  //  || //
   \\//      //  \\    ||      ||||
   //\\     ////\\\\   ||      ||\\
  //  \\   //      \\  ||  \\  || \\
 //    \\ //        \\ \\\\\\  ||  \\

"""+E
text2 = G+"""
  FFFFFFF OOOOOOO  ZZZZZ  II  LL 
  FF      OO   OO     ZZ  II  LL 
  FFFFF   OO   OO    ZZ   II  LL
  FF      OO   OO   ZZ    II  LL
  FF      OOOOOOO  ZZZZZ  II  LLLLLL

 """+E
text3 = F+"""
  FFFFFFF OOOOOOO  ZZZZZ  II  LL 
  FF      OO   OO     ZZ  II  LL 
  FFFFF   OO   OO    ZZ   II  LL
  FF      OO   OO   ZZ    II  LL
  FF      OOOOOOO  ZZZZZ  II  LLLLLL
"""+E
text4 = O+"""
  FFFFFFF OOOOOOO  ZZZZZ  II  LL 
  FF      OO   OO     ZZ  II  LL 
  FFFFF   OO   OO    ZZ   II  LL
  FF      OO   OO   ZZ    II  LL
  FF      OOOOOOO  ZZZZZ  II  LLLLLL
                                                                                                        
                                                                                                                                                                                                                                                                                     
"""+E
text5 = W+"""
 \\    //      /\      //////  ||  //
  \\  //      //\\     ||  //  || //
   \\//      //  \\    ||      ||||
   //\\     ////\\\\   ||      ||\\
  //  \\   //      \\  ||  \\  || \\
 //    \\ //        \\ \\\\\\  ||  \\
"""+E

ran = random.randrange(1,6)

if ran == 1:
	print(text1)
elif ran == 2:
	print(text2)
elif ran == 3:
	print(text3)
elif ran == 4:
	print(text4)
elif ran == 5:
	print(text5)