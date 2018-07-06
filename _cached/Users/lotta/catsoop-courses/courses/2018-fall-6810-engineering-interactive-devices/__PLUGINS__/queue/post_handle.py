

# Add the "Ask for Help/Checkoff" for any discovered questions

BeautifulSoup = csm_tools.bs4.BeautifulSoup
soup = BeautifulSoup(cs_content)

addtoqueue = '''\
queue.add('{type}', {{
  location: queue.get('location'),
  assignment: {{
    name: '{csq_name}',
    page: catsoop.this_path,
    path: catsoop.path_info,
    display_name: '{csq_display_name}',
  }},
}})
'''

tablenumber_modal = '''\
!queue.get('location') ?
swal({{
    title: "Enter Table Number",
    text: "Please enter your table number:",
    type: "question",
    input: "text",
    showCancelButton: true,
    inputPlaceholder: "Table number (e.g., 6A)",
    preConfirm: function(text){{
        return new Promise(function(resolve, reject) {{
        if (text === false) reject('no');
        else if (text === "") {{
            reject("You need to write something!");
        }}else{{
            resolve();
        }}}});
    }}
    }}).then(function(text) {{
        queue.set('location', text);
        ''' + addtoqueue + '''
        queue.set('_visible', true);
    }}) : (''' + addtoqueue + ''', queue.set('_visible', true))'''

def queue_buttons(qtype, context):

    buttons = soup.new_tag('span')
    buttons['id'] = '{}_queue_buttons'.format(context['csq_name'])

    button = soup.new_tag('button')
    button['class'] = ['btn', 'btn-catsoop', 'help']
    button.string = 'Ask for Help'
    button['onclick'] = tablenumber_modal.format(
        type = 'help',
        **context,
    )
    buttons.append(' ')
    buttons.append(button)

    if qtype['qtype'] == 'checkoff':
        button = soup.new_tag('button')
        button['class'] = ['btn', 'btn-catsoop', 'checkoffbtn']
        button.string = 'Ask for Checkoff'
        button['onclick'] = tablenumber_modal.format(
            type = 'checkoff',
            **context,
        )
        buttons.append(' ')
        buttons.append(button)

    return buttons

if queue_enable:
    for name, (qtype, context) in queue_questions.items():
        qdiv = soup.find(id='cs_qdiv_{}'.format(name))
        if qdiv is None: continue

        buttons = qdiv.find(id='{}_buttons'.format(name))
        if buttons is None: continue

        buttons.insert_after(queue_buttons(qtype, context))

    cs_content = str(soup)


