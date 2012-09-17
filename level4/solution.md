## Solution Summary

XSS.

Idea: trick karma_fountain into giving karma to one of our users by creationg a user with some javascript as its password and then sending karma to karma_fountain from that user. The reuslt is that our user's password will now be shown to karma_fountain next time it logs in, and the Javascript will submit the trade form, making karma_fountain give karma to our user.

## Solution Details

TODO: find actual JS to use as password.

## Problem Statement (Copied from CTF website)

The Karma Trader is the world's best way to reward people for good deeds: https://level04-2.stripe-ctf.com/user-ygjaufnnxh. You can sign up for an account, and start transferring karma to people who you think are doing good in the world. In order to ensure you're transferring karma only to good people, transferring karma to a user will also reveal your password to him or her.

The very active user karma_fountain has infinite karma, making it a ripe account to obtain (no one will notice a few extra karma trades here and there). The password for karma_fountain's account will give you access to Level 5.

You can obtain the full, runnable source for the Karma Trader from git clone https://level04-2.stripe-ctf.com/user-ygjaufnnxh/level04-code. We've included the most important files below.

