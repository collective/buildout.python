def osdetect(buildout):
    import sys
    import platform
    import os

    platforms = ['default']
    if sys.platform == 'darwin':
        platforms.insert(0, 'darwin')
        mac_ver = platform.mac_ver()
        if mac_ver[0].startswith('10.5'):
            platforms.insert(0, 'darwin-leopard')
        elif mac_ver[0].startswith('10.6'):
            platforms.insert(0, 'darwin-snowleopard')
            if sys.maxint > 2147483647:
                platforms.insert(0, 'darwin-snowleopard-64')
        elif mac_ver[0].startswith('10.7'):
            platforms.insert(0, 'darwin-lion')
        elif mac_ver[0].startswith('10.8'):
            platforms.insert(0, 'darwin-mountainlion')
        elif mac_ver[0].startswith('10.9'):
            platforms.insert(0, 'darwin-mavericks')
        elif mac_ver[0].startswith('10.10'):
            platforms.insert(0, 'darwin-yosemite')
        elif mac_ver[0].startswith('10.11'):
            platforms.insert(0, 'darwin-elcapitan')
        elif mac_ver[0].startswith('10.12'):
            platforms.insert(0, 'darwin-sierra')
    elif sys.platform == 'linux2':
        platforms.insert(0, 'linux2')
        dist, version, name = [x.lower() for x in platform.dist()]
        platforms.insert(0, '-'.join([sys.platform, dist]))
        platforms.insert(0, '-'.join([sys.platform, dist, version]))
        if name:
            platforms.insert(0, '-'.join([sys.platform, dist, name]))
    elif platform.machine() == 'x86_64':
        platforms.insert(0, 'x86_64')

    if os.path.exists('/usr/lib/i386-linux-gnu'):
        platforms.insert(0, 'i386-linux-gnu')

    buildout._logger.debug("Detected these platforms: %s" % ", ".join(platforms))

    variants = {}
    parts = set()
    for key in buildout.keys():
        if ':' not in key:
            continue
        part, variant = key.split(':')
        variants.setdefault(variant, []).append((part, key))
        parts.add(part)

    for platform_name in platforms:
        for part, key in variants.get(platform_name, []):
            if part in buildout._raw:
                continue
            buildout._raw[part] = buildout._raw[key].copy()
