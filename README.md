<pre>
Python code which combines images files into a single pdf. 
The images files are obtained from a directory which is specfied by the user, when running the code.

The required modules for the code are "img2pdf" and "os"


In this repository:
=> "write_images_to_pdf.py" : main python code, which is formatted with intention of 
                              being converted to .exe (pyinstaller).                                                
                              i.e - Code has user interface (text).
                              
=> "write_images_to_pdf[Bare_minimum_code].py" :  bare essential code used to convert images to single pdf .
                                                    ( same as main code but without text user interface and 
                                                       try/except error handling)

=> "write_image_to_pdf.exe" : 'write_images_to_pdf.py' (along with dependecies) converted to standalone .exe 
                               from the use of "pyinstaller".                               
                               This file (the .exe) was originally made for convenience of personal usagage;
                                  >can run the code anytime without having to install/open python IDE.
                                    {.exe as so far been tested on Windows10 64bit OS}
                               
                              The current size of the .exe (>200mb) is due the inclusion of required module "img2pdf"; 
                                  >>> a workaround is yet to be made for this filesize issue.
                             
Know bug with the code:
     most .png files seem to cause error with function "img2pdf.convert"
     ,seemingly, due to alpha channel of png (a work around is yet to be made)

<pre />
