def osdetect(buildout):
    import sys, platform

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

    buildout._logger.debug("Detected these platforms: %s" % ", ".join(platforms))

    variants = {}
    for key in buildout.keys():
        if ':' not in key:
            continue
        part, variant = key.split(':')
        variants.setdefault(variant, []).append((part, key))

    for platform in platforms:
        for part, key in variants.get(platform, []):
            if part in buildout:
                continue
            buildout._raw[part] = buildout._raw[key].copy()
