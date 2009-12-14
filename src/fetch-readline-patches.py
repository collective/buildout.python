import re
import os
import urllib2
from pprint import pprint

def fetch(local, buildout):
    url = local['url'].rstrip('/')
    prefix = local['prefix']
    index = urllib2.urlopen(url)
    existing_patches = set(os.listdir(prefix))
    available_patches = set(re.findall('<a href="(readline\d+-\d+)">',
                            index.read()))
    index.close()
    new_patches = available_patches - existing_patches
    if len(new_patches) > 0:
        print "Fetching %s." % ", ".join(sorted(new_patches))
        for patch_name in new_patches:
            connection = urllib2.urlopen("%s/%s" % (url, patch_name))
            data = connection.read()
            connection.close()
            f = open(os.path.join(prefix, patch_name), "wb")
            f.write(data)
            f.close()
        print "Writing new combined patch."
        out = open(os.path.join(prefix, "readline.patch"), "wb")
        lspatch = sorted(os.listdir(prefix))
        for patch_name in lspatch:
            if re.match("readline\d+-\d+", patch_name):
                f = open(os.path.join(prefix, patch_name), "rb")
                out.write(f.read())
                f.close()
        out.close()
