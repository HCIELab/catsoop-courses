<python>
tutor.init_random()
super_secret = [1 if cs_random.randint(0,9)<5 else 0 for x in range(4)]
second_super_secret = [1 if x ==0 else 0 for x in super_secret]

def is_close(closeness):
    def close(x,y):
        return  abs((x-y)*1.0/y)<closeness
    return close

csq_nsubmits = float(50.0)

cs_scripts += '<script type="text/javascript" src="COURSE/scripts/scrollspy_builder.js"></script>'

cs_print("""
<script>
var user = "%s";
var whereat = "%s";
</script>
"""%(cs_username,cs_path_info))
</python>



<iframe width="560" height="315" src="CURRENT/selfie-camera.mp4" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>



This weeks user interface features a selfie camera that is a flying drone. 
People throw it in a certain direction to get a selfie. The drone then automatically returns to the thrower.

What are you thoughts on this? </br>
List both pros and cons (2-3 paragraphs):

</br></br>

