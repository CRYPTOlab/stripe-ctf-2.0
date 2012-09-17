## Solution Summary

Sloppy programming. No code needed.

Send the following request:

    /index.php?attempt=&filename=some-random-filename

Idea: replace the file that gets read to check the combination by passing in an invalid filename. The "read" combination will now be empty, since the file does not exist. Send an empty attempt as well, causing the match in line 16 of `index.php` to succeed.

## Solution Details

Solution relies on the `extract()` function, which takes an array and makes variables from the key/value pairs in the array. The key is that if a variable with the same name as a key in the array already exists, then its value gets replaced by the value in the array (see default `extract_type` in the [documentation](http://php.net/manual/en/function.extract.php "extract() documentation"). 

So, by adding a `filename` parameter, we can replace the `$filename` variable with whatever we want. We replace it with a nonexisting file so that the `$combination` that our `$attempt` is checked again is "" (empty).

## Problem Statement (Copied from CTF website)

Excellent, you are now on Level 1, the Guessing Game. All you have to do is guess the combination correctly, and you'll be given the password to access Level 2! We've been assured that this level has no security vulnerabilities in it (and the machine running the Guessing Game has no outbound network connectivity, meaning you wouldn't be able to extract the password anyway), so you'll probably just have to try all the possible combinations. Or will you...?

You can play the Guessing Game at https://level01-2.stripe-ctf.com/user-wagsupfjzd. The code for the Game can be obtained from git clone https://level01-2.stripe-ctf.com/user-wagsupfjzd/level01-code, and is also included below.
