# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:46:41 2019

@author: Jamie M JOHNS 2019

Github repository:https://github.com/JamieMJohns/Combine-image-files-into-single-pdf-python-/

This  code is formated with the intention of being
converted to an .exe (using pyinstaller), for convenience of re-use 
outside of a python IDE... however currently used module [img2pdf] results
in exe being larger than 200mb.

A bare mininum version of the code (without the user interface text [print functions]);
is also available on the same github repository [above];
 the related python file is named "write_images_to_pdf[Bare_minimum_code].py"

# Note you must have modules "img2pdf" and "os" installed in your python IDE before converting code
  to .exe [such as with use of pyinstaller as the code was used for]

"""
import img2pdf # required module for writing image files to pdf
import os # required module for searching full path of files [os.walk] and also used to change color of text/background in .exe

os.system('color 1F') #set color of text and background to respectivly be bright white and blue [just for aesthetics]
os.system('mode con:cols=80 lines=30') # set number of lines and columns for exe [not required, but original exe had too many columns/lines than needed]
print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' #String for user interface
print '@@@@@@@@@@@@@@ Combine images into a single pdf  @@@@@@@@@@@@@@@@@@@@@@@' #String for user interface
print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' #String for user interface
print '                       Version 1.0                                       '
print '                 Code created in Spyder (Python 2.7)' #String for user interface
print '                           By                                           ' #String for user interface
print '                       Jamie Johns                                      ' #String for user interface
print '                          2019           ' #String for user interface
print '   The code was converted to an .exe file using "Pyinstaller"           ' #String for user interface
print  ' (current used python module img2pdf results .exe file size >200mb)'
print 'Description===[to be updated]=========================================='#String for user interface
print  'Program/code obtains image files (jpg,png,tif,bmp and gif) from a given'
print  'directory than combines the files into a single pdf; by chronological'
print  'order of image filenames.'
print  ' [all other file types but previously specified image files are ignored]'
print ''
print 'User specified inputs: [copy/paste] ###################'
print '\tInput directory = directory to images that are to be added into pdf'
print '\tOuput directory = directory that output pdf will be created in'
print '\tOuput filename = specified name of output pdf'
print '#######################################################'
print 'further notes: most .png files seem to cause error at function img2pdf.convert'
print '(from code) due to alpha channel of png (a work around is yet to be made)'
print '  [a current workaround is to convert png to .jpg or another image type]'
print '>> if there is an error; the program will tell you..'
print '========================================================================' #String for user interface
raw_input('<Press any key to continue>') #code waits for user response before continuing

try: # try running main code (try catch is used, because code is run in exe; so user can see error before program closes)
    print 'For specifying input/output directory, an example is (without quotes):\n"C:\\folder\\subfolder\\subsubfolder"\n'
    full_path=raw_input('>Input directory of images: ') #user specified intput path
    write_path=raw_input('>output directory of pdf: ') #user specified ouput path
    pdf_name=raw_input('>Filename of pdf: ') #user specified pdf name
    # Determine if extension '.pdf' needs to be added @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    if '.pdf' not in pdf_name: # if '.pdf' not found in specifed filename
        pdf_name=pdf_name+'.pdf' # add extension
    else: #else, if '.pdf' is SOMEWHERE in filename (may no be at end)
        if pdf_name.split('.pdf')[-1]!='': # split by '.pdf'; if at end last item will be blank
            pdf_name=pdf_name+'.pdf' # add extension
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
    raw_input('<Press any key to start process or exit program>') #code waits for user response before continuing
    accepted_filetypes=['.jpg','.png','.tif','.bmp','.gif'] # accepted file types for input into pdf
    filez=[files for root, dirs, files in os.walk(full_path)]  #list of all files in main and sub direc
    if any(isinstance(i, list) for i in filez): #if list is nested (i.e - there were sub-directories)
        filez=filez[0] #file names exclude subdirectories in direc  
    filez = [k for k in filez if any([j in k.lower() for j in  accepted_filetypes])] # for each file; if filename contains any items from accepted list; keep
    file_path=[] # initilize list; full directory path to files to be added to pdf
    for j in filez: # for each file; create full directory path
        file_path.append(root+'/'+j) # ^^ append to list
    print('Process Started...')
    with open(write_path+'/'+pdf_name, "wb") as f: #open pdf file for writing 
        f.write(img2pdf.convert(file_path)) # write image files (listed by file path) to pdf
    f.close() #close the pdf file from writing
    print('Process complete!!')
    print('')
    print('Output filename: '+pdf_name)
    print('Output path: '+write_path)
except Exception as err1: #If above resulted in error (also record error message as string "err1")
    print 'There was an error with the directory you entered.' #String for user interface
    print 'The python specific error is listed as: ' #String for user interface
    print err1 #Print python specific error
finally:
    if f: # if pdf file is still open for writting:
        try: # try close opened pdf file [try/except added in current version of code in case of unforseen potential error]
            f.close() # close pdf file for writting
        except: #if unexpected error with closing file (added to avoid program [.exe] closing on error])
            pec_done=0 ## ^^ then do nothing (line/code here is place holder)
    raw_input('<Press enter to exit program>')
    