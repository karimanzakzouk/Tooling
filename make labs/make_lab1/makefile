fileSrc1 = main.c
fileObj1 = main.o
fileHeader1 =

fileSrc2 = MathGeek\MathGeek.c
fileObj2 = MathGeek\MathGeek.o
fileHeader2 = MathGeek\MathGeek.h

fileSrc3 = FastPrinter\FastPrinter.c
fileObj3 = FastPrinter\FastPrinter.o
fileHeader3 = FastPrinter\FastPrinter.h

fileSrc4 = ScanningEye\ScanningEye.c
fileObj4 = ScanningEye\ScanningEye.o
fileHeader4 = ScanningEye\ScanningEye.h 

fileSrc5 = AngrySpeaker\AngrySpeaker.c
fileObj5 = AngrySpeaker\AngrySpeaker.o
fileHeader5 = AngrySpeaker\AngrySpeaker.h

fileSrc6 = TheOldWise\TheOldWise.c
fileObj6 = TheOldWise\TheOldWise.o
fileHeader6 = TheOldWise\TheOldWise.h 

allObjs = $(fileObj1) $(fileObj2) $(fileObj3) $(fileObj4) $(fileObj5) $(fileObj6)

CC = gcc

FinalTargetName=MasterApplication.exe

$(FinalTargetName) : CFLAG = 
$(allObjs): CFLAG = -c

$(FinalTargetName) : $(allObjs) 
	$(CC) $(CFLAG) $^ -o $@
$(fileObj1) : $(fileSrc1) 
	$(CC) $(CFLAG) $< -o $@
$(fileObj2) : $(fileSrc2) 
	$(CC) $(CFLAG) $< -o $@
$(fileObj3) : $(fileSrc3) 
	$(CC) $(CFLAG) $< -o $@ 
$(fileObj4) : $(fileSrc4) 
	$(CC) $(CFLAG) $< -o $@ 
$(fileObj5) : $(fileSrc5) 
	$(CC) $(CFLAG) $< -o $@ 
$(fileObj6) : $(fileSrc6) 
	$(CC) $(CFLAG) $< -o $@

.PHONY : clean link onlyCompile

clean:
	DEL $(FinalTargetName) $(allObjs)

link:
	$(CC) $(allObjs) -o $(FinalTargetName)

onlyCompile:  $(allObjs)
