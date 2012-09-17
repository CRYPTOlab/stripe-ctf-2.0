## Solution Summary

File upload vulnerability.

Idea: form intends for you to upload an image but doesn't enforce that the file is an image. You can upload any file type (including a php script) and it will be saved into a known directory (`/uploads/filename`). Upload a php script that reads `password.txt` from disk and displays it.

## Solution Details

Pretty straightforward from summary. File to upload is `TODO(ipince): upload file from linux machine into github repo`.

## Problem Statement (Copied from CTF website)

You are now on Level 2, the Social Network. Excellent work so far! Social Networks are all the rage these days, so we decided to build one for CTF. Please fill out your profile at https://level02-4.stripe-ctf.com/user-yxajrmusga. You may even be able to find the password for Level 3 by doing so.

The code for the Social Network can be obtained from git clone https://level02-4.stripe-ctf.com/user-yxajrmusga/level02-code, and is also included below.

