**grep for ffuf results filtering with n HTTP code:**

``^\[Status: 403,(.*?)\]``

**ffuf filtering program's banner and all unnecessary lines:**

``cat ffuf_output.txt | cat ffuf_results.txt | grep -E "\[Status:|\| URL"``


**ffuf filtering 200s with n size:**

``\[Status: 200, Size: 562[0-9][0-9],(.*?)\n(.*?)\n(.*?)\n\n``

**ffuf filtering empty robots.txt file:**

``\[Status: 200, Size: 26(.*?)\n(.*?)/robots\.txt\n(.*?)\n\n``


**WAYBACKMACHINE filtering invalid URLS to avoid some programs' exceptions:**

``cat wayback.txt | grep -E "^htt(p|ps)://(.*)/"``


**js endpoints processing from a list of alive hosts:**

``grep -oh "\"\/[a-zA-Z0-9_?&=/\-\#\.]*\"" | awk \x39{!/.css/ && !/.png/ && !/.jpg/ && !/.svg/ && !/.jpeg/ && !/.ico/ && !/.gif/ && !/.woff/ && !/.woff2/; gsub("\"","",$0); gsub("\\?$","",$0); gsub("/\$","",$0);  gsub("^","{}",$0); print $0}\x39 | sort -u``


**grep for filtering nuclei response with credentials-all template from https://github.com/w9w/JSA/blob/main/automation.sh:**
``\[credentials-disclosure-all\] \[http\] \[medium\][\W\w][^\n]{0,300}``
