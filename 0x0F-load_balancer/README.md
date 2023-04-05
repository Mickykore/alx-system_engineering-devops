<h1>0x0F-load_balancer</h1>

<h2>Background Context</h2>
You have been given 2 additional servers:
<lu>
<li>gc-[STUDENT_ID]-web-02-XXXXXXXXXX</li>
<li>gc-[STUDENT_ID]-lb-01-XXXXXXXXXX</li>
</lu>
<p>Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.</p>

<p>For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.</p>

<h2>Resources</h2>
Read or watch:
<lu>
<li><a href="https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts"Introduction to load-balancing and HAproxy</a><li>
<li><a href="https://www.techopedia.com/definition/27178/http-header">HTTP header</a></li>
<li><a href="https://haproxy.debian.net/">Debian/Ubuntu HAProxy packages</a></li>

<h2>Requirements</h2>
<h3>General</h3>
<lu>
<li>Allowed editors: vi, vim, emacs</li>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A README.md file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass Shellcheck (version 0.3.7) without any error</li>
<li>The first line of all your Bash scripts should be exactly #!/usr/bin/env bash</li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing<li>
