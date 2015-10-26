This is a 2D hash table object.

It acts like a regular hash table except that you must pass two keys, not one. You must make sure to pass the keys in a consistent manner, or the object will not correctly be retrieved. 

Also, the objects added to the hash table must have two fields, key_x and key_y. These are needed as fields in the object for the purpose of the collusions. 