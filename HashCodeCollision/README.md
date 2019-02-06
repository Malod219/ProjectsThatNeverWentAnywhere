# HashCodeCollision
This was as a response to a challenge to find a collision in hashcodes for a very good hash function
- I take an input from firstNames.txt and lastNames.txt(which were the 100 most common first and last names)
- With these I generate 10 thousand full names
- With this I generated 1 million person objects with the full names each and corresponding ages 1-100(1 and 100 inclusive)
- From this I compare hashCodes for each person object to every recorded hashCode and then afterwards added it to the arraylist
- The common names and ages 1-100 were selected because they make sense as data sets and because I'm making some random name generator

Notes on the hashfunction
- It adds an age which means if a collision is found, it is confirmed to carry on for additions on the age with the same Names.
- I only found 66 collisions across 1 million reasonable inputs. This is a 0.0066% collision rate which is cool.
