## Solution Summary

SQL Injection. No code needed.

Idea: the secret we're looking for is stored on the Secret Safe under a namespace that we don't have access to.
We send the SQL wildcard '%' as our namespace in order to match all namespaces in the SQL query used to retrieve
values.

## Solution Details

First notice that the values are stored as <namespace>.<key> in the database. The query used to retrieve
values (line 34 in `level00.js`) has the following:

    var query = 'SELECT * FROM secrets WHERE key LIKE ? || ".%"';

There is no input sanitization. The '?' in that query gets replaced by whatever value you pass as the 'namespace' parameter. Passing a '%' makes the query select everything in the database (all namespaces). One of them has the password to the next level.

## Problem Statement (Copied from CTF website)

Welcome to Capture the Flag! If you find yourself stuck or want to learn more about web security in general, we've prepared a list of helpful resources for you. You can chat with fellow solvers in the CTF chatroom (also accessible in your favorite IRC client at irc://irc.stripe.com:+6697/ctf).

We'll start you out with Level 0, the Secret Safe. The Secret Safe is designed as a secure place to store all of your secrets. It turns out that the password to access Level 1 is stored within the Secret Safe. If only you knew how to crack safes...

You can access the Secret Safe at https://level00-2.stripe-ctf.com/user-ggspeibshv. The Safe's code is included below, and can also be obtained via git clone https://level00-2.stripe-ctf.com/user-ggspeibshv/level00-code.


