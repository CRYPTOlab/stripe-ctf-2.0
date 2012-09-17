## Solution Summary

Exploit failure to check GET vs POST requests.

Idea: upload a php script on the level2 servers (see level2 solution) that returns `AUTHENTICATED` when it is pinged.
Set the pingback URL to `level5/?pingback=level2-url`, such that a double redirect is triggered and level5 takes
level2's response as valid.

## Solution Details

TODO: include php code used.

## Problem Statement (Copied from CTF website)

Many attempts have been made at creating a federated identity system for the web (see OpenID, for example). However, none of them have been successful. Until today.

The DomainAuthenticator is based off a novel protocol for establishing identities. To authenticate to a site, you simply provide it username, password, and pingback URL. The site posts your credentials to the pingback URL, which returns either "AUTHENTICATED" or "DENIED". If "AUTHENTICATED", the site considers you signed in as a user for the pingback domain.

You can check out the Stripe CTF DomainAuthenticator instance here: https://level05-1.stripe-ctf.com/user-lticydeddw. We've been using it to distribute the password to access Level 6. If you could only somehow authenticate as a user of a level05 machine...

To avoid nefarious exploits, the machine hosting the DomainAuthenticator has very locked down network access. It can only make outbound requests to other stripe-ctf.com servers. Though, you've heard that someone forgot to internally firewall off the high ports from the Level 2 server.

Interesting in setting up your own DomainAuthenticator? You can grab the source from git clone https://level05-1.stripe-ctf.com/user-lticydeddw/level05-code, or by reading on below.

