<python>
cs_scripts += '<script type="text/javascript" src="COURSE/scripts/scrollspy_builder.js"></script>'

tutor.init_random()
super_secret = [1 if cs_random.randint(0,9)<5 else 0 for x in range(4)]
second_super_secret = [1 if x ==0 else 0 for x in super_secret]

def is_close(closeness):
    def close(x,y):
        return  abs((x-y)*1.0/y)<closeness
    return close

csq_nsubmits = float(50.0)

cs_print("""
<script>
var user = "%s";
var whereat = "%s";
</script>
"""%(cs_username,cs_path_info))
</python>


<goals><b>Goals:</b> In this tutorial, we are describing how you can create or find, and then print 3D objects. </goals>

<section>Getting your Print File</section>

In order to print anything on a 3D printer, you will need an STL file (an abbreviation of "stereolithography") of what you want to print. You can either design what you want to print from scratch and export an STL file, or you can find an STL file of something you already like online.

<subsection>Creating your Own Design</subsection>

There are many 3D editors you can use to CAD your design. Here are just a few suggestions:

- Autodesk Fusion 360 (free for students)
- Solidworks (Windows Only)
- Onshape (Free in-browser; otherwise very similar to Solidworks but with less capability)
- Sketchup (free)
- TinkerCAD (very easy, but doesn't get you very far)

<subsection>Finding Designs Online</subsection>

You can also find designs other people already made online!
[Thingiverse](https://www.thingiverse.com/search) has a large selection of files uploaded by users that you can download from.

<figure>
  <p><img src="CURRENT/thingiverse.png" style="width:6in" />  
    <figcaption>A Thingiverse search page</figcaption>
</figure>

<section>Where to Print your Object</section>

You can either print your object yourself using one of the various 3D printers located around campus, or you can have someone else print the object for you.

<subsection>Printing the Object Yourself</subsection>

TODO: flesh out the details of how this is going to work

If you come to Stefanie's lab located in 32-206, you may be able to use one of her printers if it is not already in use. Note that this means you will likely not be able to do this the day or two before a deadline :) .

There are also various 3D printers around campus you may be able to use yourself after going through some sort of training session. The IDC has several 3D printers, and you can find more through [Project Manus](http://project-manus.mit.edu/) or using the app [Mobius](http://project-manus.mit.edu/about-mobius)

<subsection>Submitting a Print Job</subsection>

TODO: flesh out the details of how this is going to work

If you have already 3D printed something in the past and the charm has been lost on you, you can instead submit a print job request. There are several places on campus that may let you do this. For the IDC, you can follow the instructions on [this](https://idc-shop.mit.edu/reserving-machines/access-idc-3d-printers) page.

<section>Different 3D Printers and Which one to use</section>

TODO: do we want a section on this or is this something for lecture?

<section>Detailed Instructions on How to 3D Print</section>

1. Create your STL file that you want to print and send it to the computer using the 3D printer
2. Open your STL file in a slicer and select the settings you want. For a faster and more consistant print job, you can use a lower resolution (2mm). If you want the print job to be smooth, use a higher resolution (1mm). You can also change the infill which will change how hollow the print ends up being. For a fast print, make the infill percent small. For a strong print, make it large.
3. Check that the 3D printer is ready. Make sure it has enough plastic coming in of the correct color and that the previous print job is done and removed.
4. Export the file produced by the slicer and send it to the 3D printer.
5. While you don't need to watch the 3D printer the entire time it is going, it is a good idea to watch the first 2-3 layers to make sure everything looks okay. If something is missalligned, you will often be able to notice then and restart the print job before wasting too much time or materials.