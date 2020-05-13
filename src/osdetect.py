MAC_RELEASE_NAMES = {
    '10.5': 'leopard',
    '10.6': 'darwin-snowleopard',
    '10.7': 'lion',
    '10.8': 'mountainlion',
    '10.9': 'mavericks',
    '10.10': 'yosemite',
    '10.11': 'elcapitan',
    '10.12': 'sierra',
    '10.13': 'highsierra',
    '10.14': 'mojave',
    '10.15': 'catalina',
}


def osdetect(buildout):
    import sys
    import platform
    import os

    platforms = ['default']
    add = platforms.append
    if sys.platform == 'darwin':
        add('darwin')
        mac_ver = '.'.join(platform.mac_ver()[0].split('.')[:2])
        if mac_ver in MAC_RELEASE_NAMES:
            add('darwin-' + MAC_RELEASE_NAMES[mac_ver])
            if mac_ver == '10.6' and sys.maxint > 2147483647:
                add('darwin-snowleopard-64')
    elif sys.platform == 'linux2':
        add('linux2')
        dist, version, name = [x.lower() for x in platform.dist()]
        add('-'.join([sys.platform, dist]))
        add('-'.join([sys.platform, dist, version]))
        if name:
            add('-'.join([sys.platform, dist, name]))
    elif platform.machine() == 'x86_64':
        add('x86_64')

    if os.path.exists('/usr/lib/i386-linux-gnu'):
        add('i386-linux-gnu')

    buildout._logger.debug("Detected these platforms: %s" % ", ".join(reversed(platforms)))

    variants = {}
    parts = set()
    for key in buildout.keys():
        if ':' not in key:
            continue
        part, variant = key.split(':')
        variants.setdefault(variant, []).append((part, key))
        parts.add(part)

    for platform_name in reversed(platforms):
        for part, key in variants.get(platform_name, []):
            if part in buildout._raw:
                continue
            buildout._raw[part] = buildout._raw[key].copy()
