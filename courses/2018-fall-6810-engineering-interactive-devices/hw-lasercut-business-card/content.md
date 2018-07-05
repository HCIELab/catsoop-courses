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

If you have never done any laser cutting before, you might want to follow this <a href="CURRENT/tutorial-laser-cutting">tutorial on laser cutting</a> that we prepared.
The tutorial also includes information as to where to laser cut on campus and where to buy materials.

<section>Deliverables</section>

* photo of your business card, upload here
* laser cut file for your business card, upload here
* bring your card to class on wednesday, September 13, 1pm


<section>Task</section>

The title says it all. Laser cut your own business card, upload the deliverables to gradebook, and bring your card to class. Materials, design etc. is all up to you. We recommend using paper, cardboard, acrylic, or wood. Google for some inspiration. 

<figure>
  <p><img src="CURRENT/businesscard-examples.png" width="80%"/>
  <figcaption>Business Card Example</figcaption>
</figure>
