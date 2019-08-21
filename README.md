<pre>
Repository description:
      A python program that automatically combines multiple image files into a single pdf;
        >> automatically placed in order (page number of pdf) by chronological order of image filenames.
      The images files are obtained from a directory which is specfied by the user, when running the code.

The required modules for the python code are "img2pdf", "os" and "pyinstaller" if intending to convert
the main python code to .exe with pyinstaller.

Files this repository:
=> "write_images_to_pdf.py" : main python code, which is formatted with intention of 
                              being converted to .exe (pyinstaller).                                                
                              i.e - Code has user interface (text).
                              
=> "write_images_to_pdf[Bare_minimum_code].py" :  bare essential code used to convert images to single pdf .
                                                    ( same as main code but without text user interface and 
                                                       try/except error handling)
Known bug with the codes (above):
     most .png files seem to cause error with function "img2pdf.convert"
     ,seemingly, due to alpha channel of png (a work around is yet to be made)

An additional file was intended to added to the repository;
        >> "write_images_to_pdf.py" converted (frozen) into a standalone .exe , along with code's dependencies, 
                    however due the module 'img2pdf' , the resulting .exe has a file size larger than 200mb;
                        [too large to upload to github (the limit is 25mb)]
                    a workaround is yet to be made for reducing the filesize.
                    
                    The code "write_images_to_pdf.py" is exact code that I have converted to .exe for personal
                    usage (such that the code can be run anytime without opening/installing a Python IDE).
                    
                   As noted, earlier in the readme, pyinstaller is the module that I use for converting the 
                   script to an exe file.
 
 A very quick tutorial for using the pyinstaller module:
  https://datatofish.com/executable-pyinstaller/
        
        
<pre />
