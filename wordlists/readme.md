api_endpoints_with_path.txt - 397442
api_endpoints.txt - 

[A-z][0-9]^(v[1-2])|[0-9][A-z] exludes lines with strings contain random chars like 8e77b3768b440a281c5101ca7941d5e0. They are most likely won't be found.

\.js$|\.jpeg|\.jpg|\.svg|\.woff|\.woff2|\.html|\.css|\.php|\.png|\.gif excludes file extensions that are most likely won't be found at /api.

Now deleting lines containing + and &.

\w\.(co|com|tw|com\.|co\.) - with heavy heart I decided to exclude lines containing domains, too. Mostly it's just garbage.


For endpoints only:

"/api/(v[0-9])|/api/|^/(v[0-9])/", "^/" and deletion of dupes gives api_endpoints.txt. Bruteforce with this list when you know for sure there is only 1 version of API, lets say, only /api/v2/ only valid.
