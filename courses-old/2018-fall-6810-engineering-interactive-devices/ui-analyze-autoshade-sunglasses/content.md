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



<iframe width="560" height="315" src="https://www.youtube.com/embed/CF4J4e7vOC8" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

This weeks user interface are autoshade sunglasses.
The device senses sunlight and when the sun reaches a certain intensity, the sunglasses automatically cover the eyes. 
If it is cloudy outside, the sunglasses move out of the way. 

What are you thoughts on this? </br>
List both pros and cons (2-3 paragraphs):

<question bigbox>
csq_check_function = lambda x,y: True
</question>

</br></br>

