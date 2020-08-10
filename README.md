# WickedProton
Simple proton mail brute force program written in python 
Unlike usual brute forcing tools, this is gui instead of only terminal so that you can explicitly see
 the processing speed and how fast the server responds AND ACCORDINGLY SET THE DELAY AFTER EACH LOGIN . As most sites including this one use ajax a little delay of 
 few centiseconds is always recommended although the least required delay may vary depending on your network connection and the speed of the server while it checks the login credentials .
  USAGE
 /////////// paste geckodriver in /usr/local/bin (kali linux) //////
  Most drivers require an extra executable for Selenium to communicate with the browser. You can manually specify where the executable lives before starting WebDriver, but this can make your tests less portable as the executables will need to be in the same place on every machine, or include the executable within your test code repository.

By adding a folder containing WebDriver’s binaries to your system’s path, Selenium will be able to locate the additional binaries without requiring your test code to locate the exact location of the driver.

Create a directory to place the executables in, like C:\WebDriver\bin or /opt/WebDriver/bin
Add the directory to your PATH:
On Windows - Open a command prompt as administrator and the run the following command to permanently add the directory to your path for all users on your machine:
 //////		setx /m path "%path%;C:\WebDriver\bin\" ////////
/////   export PATH=$PATH:/opt/WebDriver/bin >> ~/.profile    /////////////// for mac os and linux
 

USAGE
sudo pip install -r requirements.txt
python wickedProton4edv2.54.py
You can use any password list but change its name to password.lst
python wickedProton4edv2.54.py
   choose the browser (use appropiate web drivers for differnet browsers the given web driver works perfectly with chrome(ium) and firefox
   Safari - webkit
   opera - presto
   Internet Explorer - Trident
TIp - This program can be used for any site who doesn't have frequent time-outs with a minor change in the source code.
