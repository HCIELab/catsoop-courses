from textwrap import dedent

def _pluralize(l):
    if len(l) == 0:
        return 'no partner assigned.'
    elif len(l) == 1:
        return str(l[0])
    elif len(l) == 2:
        return '%s and %s' % tuple(l)
    else:
        return ', '.join(l[:-1]) + ', and %s' % l[-1]

def _name(u):
    fn = csm_cslog.most_recent('_extra_info', [], u, {})
    if fn is None or 'name' not in fn:
        return u
    else:
        return '%s (%s)' % (fn['name'], u)

if dopartners:
    uname = cs_user_info.get('username', 'None')

    section, group, members = csm_groups.get_group(
        globals(),
        cs_path_info,
        uname,
    )

    if members:
        members = [_name(i) for i in members if i != uname]
        message = 'You should work at table %s with %s.' % (group, _pluralize(members))
    else:
        message = 'You have not yet been assigned a partner for this lab.'

    partners_display = '''\
    <center>
      <div class="solution noprint">
        <b>Partners: </b>
        <span id="queue_partners">
          {message}
        </span>
      </div>
    </center>
    '''.format(message=message)

    cs_content = dedent(partners_display) + cs_content
