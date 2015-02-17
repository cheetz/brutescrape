====================================================================================
__________                __           _________                                        
\______   \_______ __ ___/  |_  ____  /   _____/ ________________  ______   ____
 |    |  _/\_  __ \  |  \   __\/ __ \ \_____  \_/ ___\_  __ \__  \ \____ \_/ __ \
 |    |   \ |  | \/  |  /|  | \  ___/ /        \  \___|  | \// __ \|  |_> >  ___/
 |______  / |__|  |____/ |__|  \___  >_______  /\___  >__|  (____  /   __/ \___  >
        \/                         \/        \/     \/           \/|__|        \/

Brutescrape | A web scraper for generating password files based on plain text found
               in specific web pages.
Written by Peter Kim <Author, The Hacker Playbook>
                     <CEO, Secure Planet LLC>

Usage | python brutescrape.py
====================================================================================

< About >

	Brutescrape is a tool designed to parse out text from specific web pages and generate password lists for bruteforcing with this text.
	The main idea in mind was to be able to create password lists that were specific to an organization. This way, the user will then have 
	a password list that contains keywords specific to the target entity, which provides a better chance at recovering credentials used
	within said entity. Furthermore, the use of rule files found within the users favorite password cracking tool could essentially increase
	the chances of recovering plain text passwords from an organization. 

	E.X >> The user is performing a penetration test against HackMe, Inc. The user knows the HackMe company has a website http://www.hackme.com/, and 
	uses BruteScrape against this site. The user now has a password file created specifically from parsing text within HackMe's website. The user
	then uses this wordlist against hashes they had found during a phase of the pentest. The user then decides to use this wordlist against his list
	of hashes within oclHashcat, and recovers the plain text of a hash: "hackme". 
	
	In this example, the user found a very weak password, but cases such as these would be very rare, as organizations usually have password policies
	in place. The use of rules files would probably be more viable in recovering these plain text hash values, and so the user attempts to crack the
	hashes again, this time using a rule file that will append 4 digits from 0000 - 9999 at the end of every word in his list. 

	Ah! More hashes are found: "hackme4331,hackme9901". How about a rule to change every word to leet speak?

	More hashes found: "h4ckm3, h4ckm3,inc.P455". And so on and so forth.

< Usage >

	Using the script is simple. The target webpage(s) should be listed in your "sites.scrape" file like so-

		http://www.site.com,http://www.site2.com,http://www.site3.com/index.php,http://www.site4.com/admin

	Then run the script-

		python brutescrape.py

	And that's it. The target sites defined in your "sites.scrape" file will be parsed through and the parsed words will be written to a file
	named "passwordList.txt". 
