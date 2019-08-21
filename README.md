Python code which combines images files into a single pdf. <br />
The images files are obtained from a directory which is specfied by the user, when running the code.<br />
<br />
The required modules for the code are "img2pdf" and "os"<br />
<br />
In this repository:<br />
=> "write_images_to_pdf.py" : main python code, which is formatted with intention of being converted to .exe [pyintaller]. i.e - Code has user interface (text).<br />
=> "write_images_to_pdf[Bare_minimum_code].py" :  bare essential code used to convert images to single pdf [ same as main code but without text user interface] .<br />
=> "write_image_to_pdf.exe" : 'write_images_to_pdf.py' (along with dependecies) converted to standalone .exe with the use of "pyinstaller";.<br />.  this file (the .exe) is originally made for personal usage [don't have to open python IDE to run code].<br /> 
                              The current size of the .exe (>200mb) is due the inclusion of required module "img2pdf"; a workaround is yet to be made for this filesize issue.<br />
<br />                             
<br />
Know bug:<br />
     most .png files seem to cause error with function "img2pdf.convert"<br />
     ,seemingly, due to alpha channel of png (a work around is yet to be made)<br />
<br />

