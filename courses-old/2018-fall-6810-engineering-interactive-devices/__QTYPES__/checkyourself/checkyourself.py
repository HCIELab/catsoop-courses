defaults = {
    'csq_npoints': 0,
}

allow_viewanswer = False
allow_self_submit = False
allow_save = False

def total_points(**info):
    return info['csq_npoints']

def handle_submission(submissions, **info):
    pass

def render_html(last_log, **info):
    info['csq_description'] = info['csm_language'].source_transform_string(info, info['csq_description'])
    return '''
    <div class="checkyourself">
      <b>{csq_display_name}</b>
      <div>
        {csq_description}
      </div>
    </div>
    '''.format(**info)

def answer_display(**info):
    return ''
