def osdetect(buildout):
    import sys
    import platform

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
    elif platform.machine() == 'x86_64':
        platforms.insert(0, 'x86_64')

    buildout._logger.debug("Detected these platforms: %s" % ", ".join(platforms))

    variants = {}
    parts = set()
    for key in buildout.keys():
        if ':' not in key:
            continue
        part, variant = key.split(':')
        variants.setdefault(variant, []).append((part, key))
        parts.add(part)

    for platform in platforms:
        for part, key in variants.get(platform, []):
            if part in buildout._raw:
                continue
            buildout._raw[part] = buildout._raw[key].copy()
