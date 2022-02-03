
# Karoua Youtube Download Gui

<h2>Download youtube videos</h2>

<p>Hi.</p>
<p>There are many youtube downloaders scattered around the web.
 Many of them non-functional or have lots of garbage  such  as 
 ads, malwares, anoying messages and so on.

My software is straight to the point:</p>
<ul>
  <li>Insert youtube link</li>
  <li>Choose resolution</li>
  <li>Download</li>
</ul>      

This version has a GUI interface but it also runs on CLI.

<h2>Running with GUI interface:</h2>

	python youtube_download.py

![GUI interface](./img/image01.png)




<h2>Running with CLI interface:</h2>

	python youtube_download.py --nogui

![CLI interface](./img/image02.png)


## Standalone executable for Windows:
Perhaps you do not have python installed or you cant install python in your machine and just want a fast way to get things running. The standalone executable is perfect choice.
<ul>
	<li>Download the zip file, unzip it into a new folder</li>
	<li>Download CRC checksum file</li>
	<li>Download my PGP public key</li>		
</ul>

### How to check the zipfile has not been tampered with:

#### First, you need to check if my public key has not been hacked or tampered with. In order to do that, you should download my public pgp key at least in two different sourcers and check if they are the same. If they are the same and have not been revoked, good, the key is valid and secure for use. 

#### Visit the following address:

<a href = "http://keyserver2.pgp.com"> PGP Global Directory</a>

Search for my pgp fingerprint:

	46C1 8DF7


or directly  here:

https://keyserver2.pgp.com/vkd/DownloadKey.event?keyid=0xB79AAE8846C18DF7 


Download the provided file and compare with pgp public key here on my github. If they are the same, perfect, you are good to go.

Import my pgp public signature key:

	gpg --import andersonFrossard.publ.asc

Check wether youtube_download.zip has been signed by myself:

	gpg --verify youtube_download.sig

To pass verification you should see a message saying
>Good signature from Anderson Frossard. (Das ist meine key. Wir ziehen voran!)

gpg will probably also say this signature is not certified. That´s because you have just downloaded it and have not applied command *trust* to it.

Once the gpg has verified the zip file and been signed by myself, you are safe to unzip it and run its executable.

If you want additional step of safety, you can verify the crc.txt file and check wether the hash of downloaded zip file meet the hash indicated in crc.txt file. Here it is:

	gpg --verify crc.txt.sig

Once sucessfully verified, you are good to hash your downloaded zip file and compare with contents from crc.txt.
The hash should be exactly the same. You are safe to unzip and run the executable. 
<table>
	<tr>
		<td>SHA-256</td>
		<td>File</td>
	<tr>
		<td>1446056F904BCC639CB844611F69E8218FCE32AB3314E00F676BF80FE659061B</td>
		<td>youtube_download.zip</td>
	</tr>
</table>


Enjoy!
