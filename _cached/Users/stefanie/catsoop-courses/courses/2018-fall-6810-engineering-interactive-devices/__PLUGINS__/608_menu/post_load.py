

def html_generator(stuff,header=True):
    out = ""
    for i in stuff:
        if i == 'divider':
            out += '\n<li class="divider"></li>'
            continue #we're done here
        link = i['link']
        if isinstance(link, str):
            if header:
                out += '\n<li class="nav-item top_bar"><a href="%s">%s</a></li>' % (link, i['text'])
            else:
                out += '\n<li class="nav-item top_bar inner_list"><a href="%s">%s</a></li>' % (link, i['text'])
            
        else:
            out += '\n<li class="nav-item dropdown top_bar">'
            out += ('<a href="#" data-toggle="dropdown" '
                    'class="dropdown-toggle" role="button" '
                    'aria-expanded="false">')
            out += i['text']
            out += '<span class="caret"></span></a>'
            out += '<ul class="dropdown-menu">'
            out += html_generator(link, False)
            out += '</ul>'
    if header:
        return out + '</ul></div>'
    else:
        return out


if 'cs_user_info' in globals():
    base_url = cs_url_root + '/' + '/'.join(cs_path_info)
    perms = cs_user_info.get('permissions', None)
    staff_menu = {'text': 'Staff', 'link': []}
    if 'staff' in perms:
        staff_menu['link'].append({'text': 'WHDW', 'link': '%s?action=stats' % base_url})
    if 'admin' in perms:
        if 'queue_enable' in globals() and queue_enable:
            staff_menu['link'].append({'text': 'Manage Partners', 'link': '%s?action=manage_groups' % base_url})
    if len(staff_menu['link']) > 0:
        cs_top_menu.append(staff_menu)
    blank = ""
    out = html_generator(cs_top_menu,True)
    cs_top_menu = out
    




