## Solution Summary

Length-extension attack on SHA1 signature.

Idea: given an existing payload and its valid SHA1 signature (calculated as `sha(payload + secret)`), there is a way to generate a valid SHA1 signature for `payload + something + secret`. We use this exploit to generate a valid request for a waffle coming from a privileged user. We can look at the logs of user 1 and find a valid request for a wrong waffle. All we need to do is generate a valid request for the right waffle by appending `&waffle=liege` after the original payload.

## Solution Details

TODO: give better explanation.

Link to resource: http://www.vnsecurity.net/2010/03/codegate_challenge15_sha1_padding_attack/

## Problem Statement (Copied from CTF website)

Welcome to the penultimate level, Level 7.

WaffleCopter is a new service delivering locally-sourced organic waffles hot off of vintage waffle irons straight to your location using quad-rotor GPS-enabled helicopters. The service is modeled after TacoCopter, an innovative and highly successful early contender in the airborne food delivery industry. WaffleCopter is currently being tested in private beta in select locations.

Your goal is to order one of the decadent Liège Waffles, offered only to WaffleCopter's first premium subscribers.

Log in to your account at https://level07-2.stripe-ctf.com/user-nasaamhiaj with username ctf and password password. You will find your API credentials after logging in. You can fetch the code for the level via
git clone https://level07-2.stripe-ctf.com/user-nasaamhiaj/level07-code, or you can read it below. You may find the sample API client in client.py particularly helpful.

