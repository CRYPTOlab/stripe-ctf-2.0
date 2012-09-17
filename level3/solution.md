## Solution Summary

SQL injection.

Idea: inject SQL in the SELECT query at line 86 of `secretvault.py` to make results any values of our choosing. We can then authenticate as any user we want.

## Solution Details

1. Pick a password to use, which we'll call `$fake_password`. Take its SHA256 hash, which we'll call `$hashed_pass`.

2. Try to login with username set to: `gibberish' UNION SELECT 1 AS id, $hashed_pass AS password_hash, '' AS salt FROM users;--`. Send `$fake_password` as the password and voila, you're in!

We're exploiting the SQL query used to find users in `/login` on line 86. The query:

     query = """SELECT id, password_hash, salt FROM users WHERE username = '{0}' LIMIT 1""".format(username)

will become:

    SELECT id, password_hash, salt FROM users WHERE username = 'gibberish' UNION SELECT 1 AS id, $hashed_pass AS password_hash, '' AS salt FROM users;--' LIMIT 1

Since there is no user with username `gibberish` (or if there is, then try another username!), the first SELECT in the union query returns an empty result set. The second SELECT is hard-coded to return the values 1, `$hashed_pass`, and '', so those are the values the password will be checked against. By sending `$fake_password` as the password, we successfully authenticate as user with user id 1.

## Problem Statement (Copied from CTF website)

After the fiasco back in Level 0, management has decided to fortify the Secret Safe into an unbreakable solution (kind of like Unbreakable Linux). The resulting product is Secret Vault, which is so secure that it requires human intervention to add new secrets.

A beta version has launched with some interesting secrets (including the password to access Level 4); you can check it out at https://level03-2.stripe-ctf.com/user-fjrioqjned. As usual, you can fetch the code for the level (and some sample data) via git clone https://level03-2.stripe-ctf.com/user-fjrioqjned/level03-code, or you can read the code below.
