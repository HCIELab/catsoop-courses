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

<div class="goals"><b>Analyze UI Design:</b> 

In the next weeks, we will show you a bunch of un-usual user interface.
Your job is to look at the user interface, think about its use, and write down an informed opinion about the pros and cons of each user interface. We hope that by thinking about a different user interface every week, you will take these considerations into account when designing your own user interface for your class project.

</div>
</br></br>
<div class="goals"><b>Tippen mit Kippen (German for: Vote with Cigarettes)</b> 

The user interface below serves as both a cigarette dispenser as well as a voting machine. 
To vote on the question shown (in this case: 'Will Germany win the european soccer league?'), users dispose their cigarettes either on the left side ('Yes') or on the right side ('No'). What are you thoughts on this? List both pros and cons (2-3 paragraphs):

<figure>
  <p><img src="CURRENT/tippen-mit-kippen.jpg" width="50%"/>
  <figcaption>Voting with Cigarettes</figcaption>
</figure>

