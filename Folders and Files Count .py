Folders and Files Count 

The program must accept N string values representing the locations of N files in a computer. The program must find the number of folders and the number of files present in 
each root folder as shown in the Example Input/Output section. The names of the root folders must be printed in sorted order. 
Note: There are no files without a folder. 

Boundary Condition(s): 1 <= N <= 50 6 <= Length of each string <= 100 
Input Format: The first line contains N. The next N lines contains N string values representing the locations of N files in a computer. 
Output Format: The lines, each contains the name of a root folder, the number of folders and the number of files present in each root folder. 

Example Input/Output 1: 
Input:
 12 
\Documents\MyDetails\photo.jpeg 
\Videos\movie01.mp4 \Videos\MiniProject\overview.mp4 
\Documents\MyDetails\resume.pdf
\Videos\MiniProject\completeDemo.mp4
\Videos\Python\tutorial001.mp4
\Downloads\FirefoxSetup.exe
\Downloads\XYZScanner.exe
\Videos\Python\tutorial002.mp4
\Documents\MyDetails\voterID.pdf
\Downloads\TelegramDesktop\image_12022021.jpeg
\Downloads\TelegramDesktop\image_13022021.jpeg 

Output: 
Documents - 1 folder 0 files 
Downloads - 1 folder 2 files 
Videos - 2 folders 1 file 

Explanation: There is only 1 folder inside the root folder Documents. Documents -> MyDetails There are 1 folder and 2 files inside the root folder Downloads.
 Downloads -> TelegramDesktop Downloads -> FirefoxSetup.exe and XYZScanner.exe There are 2 folders and 1 file inside the root folder Videos. 
 Videos -> MiniProject and Python Videos -> movie01.mp4

 Example Input/Output 2: 
 
 Input:
7 
\Videos\Project\Combined\Edited\myproject.mp4 
\Videos\myVlogs\day001.mp4 \Videos\day003.mp4 
\Desktop\image1.png 
\Videos\myVlogs\day002.mp4
\Videos\Project\Combined\myproject.mp4
\Desktop\abc.txt

Output: 
Desktop - 0 folders 2 files
Videos - 2 folders 1 file



#Your code below
x=int(input());l1=[];l2=[];l3=[]
for k in range(x):
    a=input().strip().split("\\");l1.append(a);l2.append(a[1]);
so=sorted(list(set(l2)));s1,su='',''
for k in so:
    la=[]
    f,fi=0,0
    for h in l1:
        if k==h[1]:
            if len(h)==4 and h[2] not in la :f+=1;la.append(h[2])
            if len(h)>4 and h[2] not in la:f+=1;la.append(h[2])
            if len(h)==3:fi+=1
    if f>1 or f==0:si='folders'
    else:si='folder'
    if fi>1 or fi==0:su='files'
    else:su='file'
    l3.append([k,'- '+str(f)+' '+si,str(fi)+' '+su])
for k in l3:print(*k)