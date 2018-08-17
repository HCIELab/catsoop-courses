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


<goals><b>Goals:</b> In this tutorial, we will describe how to use a DSLR camera. </goals>

<figure>
  <p><img src="CURRENT/dslr.png" style="width:6in" />  
    <figcaption>DSLR Camera</figcaption>
</figure>

<section>Tips for Taking Good Photos</section>

Here is a guide to the various settings on a DSLR camera. It's important to understand these settings to be able to take a good picture. However, remember that in the digital age, we can also do a lot with photo editting afterward. Here are some things you can do to make photo-editting easier later on:

* Take pictues with a clean background. This will remove a lot of work later. The IDC has a photo studio.
* Take pictures in the RAW format. This will give you more power later.
* Make sure everything you need is in focus and the lighting is good.
* Take a picture as close while still giving context. Remember that you can crop the photo later so it's okay to leave a little too much context, but you don't want to be zooming in on a small thing in the corner when you crop, as then the object would be likely out of focus and grainy.

<section>Camera Modes</section>

There are four modes you can choose from when shooting with a DSLR camera.

* P: Auto-setting aperture and shutter speed
* Tv: Shutter speed priority
* Av: Aperature priority
* M: Manual setting

<figure>
  <p><img src="CURRENT/dslr_settings.png" style="width:6in" />  
    <figcaption>DSLR Camera Settings</figcaption>
</figure>

<section>Aperture</section>

Changing the size of the aperture has two effects.

First, when you change the size of the opening, you change how much light passes into the camera. More light means a brighter picture.

<figure>
  <p><img src="CURRENT/aperture_light.png" style="width:6in" />  
    <figcaption>DSLR Camera Settings</figcaption>
</figure>

Second, the size of the aperture can change how blurry the picture is. A smaller aperture means that the image will be crisp everywhere, but a larger aperture might only focus the front.

Fun fact: This concept applies to human eyes as well! If you have bad eyesight, try curling up your undex finger until there is just a little bit of light passing through the center and hold that up to your eye. Now look at something in the distance. You might find that what you are looking at appears much crisper! This is also why people often squint to see things better.

<figure>
  <p><img src="CURRENT/sharp.png" style="width:3.5in" /> <img src="CURRENT/blurry.png" style="width:3.5in" />
  <figcaption>The image on the left is taken with an f/13 aperture and is uniformly sharp. The image on the right is take with a larger aperture of f/4.5 and has close object sharp but far objects blurry.</figcaption>
</figure>


<section>Shutter Speed</section>

Shutter speed effects two things as well.

First, it also effects brightness. The longer the shutter is open (slower speed), the more light will come in.

The shutter speed will also effect the crispness of moving objects. The longer the shutter is open, the more blurred a moving object becomes. Of course, sometimes this can be a feature.

<figure>
  <p><img src="CURRENT/eagle.png" style="width:3.5in" /> <img src="CURRENT/ocean.png" style="width:3.5in" />
  <figcaption>The image on the left has the shutter open for just 1/4000 of a second. On the right, the shutter is open for 6 seconds.</figcaption>
</figure>


<section>Brightness</section>

As we've seen, the brightness of an image is effected both by shutter speed and aperture. It's important that the image you take has a good brightness. If it is either too dark or too bright, this will lead to grainy images, especially if you zoom in.

Over all, the trade off means that if you want a fast shutterspeed (short exposure), you'll need a large aperture and if you want a small aperture, you'll need a slower speed (long exposure).