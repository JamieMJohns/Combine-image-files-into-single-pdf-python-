# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:52:38 2019

@author: Jamie M JOHNS 2019

Github repository:https://github.com/JamieMJohns/Combine-image-files-into-single-pdf-python-/

This file presents "bare minimum" version of the main python code found on the repository listed above.
 [i.e - bare essential lines of code without user interface (printed text) of the main code]
 
 As with the main python code, a key thing to note:
     most .png files seem to cause error with function "img2pdf.convert"
     ,seemingly, due to alpha channel of png (a work around is yet to be made)
     
         a current workaround is to convert png to .jpg or another image type

"""
import img2pdf # required module for writing image files to pdf
import os # required module for searching full path of files [os.walk]

full_path=raw_input('Input dir: ') #user specified intput path (e.g "C:\folder\subfolder\sub_subfolder")
write_path=raw_input('output dir: ') #user specified ouput path (e.g "C:\folder\subfolder\sub_subfolder")
pdf_name='My_ouput_pdf.pdf' #output file name of pdf (file name must contain ".pdf")
accepted_filetypes=['.jpg','.png','.tif','.bmp','.gif'] # list of accepted file types for input into pdf
filez=[files for root, dirs, files in os.walk(full_path)]  #list of all files in main and sub direc
if any(isinstance(i, list) for i in filez): #if list is nested (i.e - there were sub-directories)
    filez=filez[0] #file names exclude subdirectories in direc  
filez = [k for k in filez if any([j in k.lower() for j in  accepted_filetypes])] # for each file; if filename contains any items from accepted list; keep
file_path=[] # initilize list; full directory path to files to be added to pdf
for j in filez: # for each file; create full directory path
    file_path.append(root+'/'+j) # ^^ append to list 
with open(write_path+'/'+pdf_name, "wb") as f: #open pdf file for writing 
    f.write(img2pdf.convert(file_path)) # write image files (listed by file path) to pdf
f.close() #close the pdf file from writing
