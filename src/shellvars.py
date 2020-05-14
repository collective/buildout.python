# takes any shellvars entries, and expands each
# name via `/bin/sh` and stores the result
# in the same section.

def expand_shellvars(buildout):
    from subprocess import check_output, CalledProcessError
    import os
    for sectname, section in buildout._raw.iteritems():
        if "shellvars" not in section:
            continue
        for line in section["shellvars"].splitlines():
            name, _, cmd = line.partition("=")
            name, cmd = name.strip(), cmd.strip()
            if not cmd:
                continue
            try:
                section[name] = check_output(cmd, shell=True, env=os.environ).strip()
                buildout._logger.debug(
                    "Set %s.%s to %r",
                    sectname,
                    name,
                    section[name]
                )
            except CalledProcessError as exc:
                buildout._logger.debug(
                    "Skipped %s.%s, process failed: %r",
                    exc
                )
