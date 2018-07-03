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

<div class="goals"><b>Goals:</b> In this tutorial, we are describing how you can laser cut a shape. All you need is a 2D drawing program and access to a laser cutter on campus. Below are more details.</div>


<section>How Laser Cutters Work</section>

<figure>
  <p><img src="CURRENT/laser-cutter.png" style="width:3in" /> <img src="CURRENT/laser-cutter-cutting.png" style="width:4in" />
  <figcaption>A Laser Cutter (Universal Laser System PLS150D</figcaption>
</figure>

Laser Cutters are machines that can cut wood, acrylic, cardboard and other materials into 2D shapes. 
The take a 2D drawing of the path that should be cut. You then only have to define the power and speed of the laser (paper requires less power to be cut than wood) and you need to tell the laser cutter how thick your material sheet is (e.g. 3mm).  
Laser cutting is very fast compared to 3D printing, i.e. it only takes a few minutes.
It is also easy to learn since it only requires a 2D drawing of the path the laser cutter should cut as input.


<figure>
  <p><img src="CURRENT/laser-cutting-materials1.png" style="width:3in" />  
    <img src="CURRENT/laser-cutting-materials2.png" style="width:3in" />  
    <figcaption>Different Laser Cut Materials: Wood, Acrylic, Cardboard, Food</figcaption>
</figure>


<section>How to Laser Cut </section>

Here we explain how this work at the example of using Adobe Illustrator as the drawing program (you can download a 30 day trial version here) and laser cutting on the Universal Laser Cutting PLS150D laser cutter. Please see below for detailed instructions on other drawing programs and laser cutters on campus.

<subsection>Create 2D Drawing</subsection>

In Adobe Illustrator, create a new document (or use this here as a starting point, example .pdf file linked, just open the pdf with Illustrator, it will contain the path and you will be able to edit it).

Make sure that that the document is in RGB Color Mode (go to File -> Document Setup -> Color Mode -> RGB).
Use the rectangle, circle, or pen tool to create the shape you want to laser cutter.
Make sure that the inside of the shape has no color (it needs to have this struck through red line on the icon). You can double click the color to make the color selection window appear.
The main cutting color will be full red (R: 255, G: 0, B: 0), thus make sure your outline color is full red.
Finally, you need to set the line thickness setting for your path to 0.0001pt (yes that's right, the particular number of 0s does not matter, but you need to have at least a few zeros there, otherwise it will not work).
Save your drawing to a USB stick and go to the laser cutter computer.

<figure>
  <p><img src="CURRENT/laser-cutting-process1.png" style="width:3in" />  
    <figcaption>A Laser Cutter (Universal Laser System PLS150D</figcaption>
</figure>

<subsection>Send your Drawing to the Laser Cutter Software</subsection>

Open your drawing on the laser cutter computer and go to File -> Print. 
Select the Laser Cutter from the dropdown menu (it's called PLS150D). Hit the print button.
Open the laser cutter software by clicking on the ULS Control Panel Icon on the desktop. 
You should see your drawing in the software.
Your drawing should have a bright red color in the view, if it is black it will not work (either your line thickness is too thick or you set the wrong color mode in the previous step).

<figure>
  <p><img src="CURRENT/laser-cutting-process2.png" style="width:3in" />  
    <figcaption>A Laser Cutter (Universal Laser System PLS150D</figcaption>
</figure>

<subsection>Find Your Material</subsection>

Before you can set power, speed, and thickness, you need to decide on a material. 
Remember you can cut many different materials, the most common ones are wood, acrylic, and cardboard or paper. 
You cannot cut anything that is inflammable or creates toxic fumes when heated.
Reflective materials such as metal also cannot be cut on the low-end laser cutters available for class (though industrial high-end laser cutters can). 

When I use the laser cutter for a new prototype, I typically start cutting it from cardboard first (it's cheaper!) and then later cut it from more expensive materials, such as acrylic. Low-fidelity prototyping.

<subsection>Insert Material into Laser Cutter</subsection>

Put the material inside. It is generally best to put it against a corner so it doesn't move too much. The top left is standard. You should make sure that in the software, the cut is similarly moved to the top left, leaving at least 1/8" on each side.

Once you've inserted the material, you should make sure the pieces is in the right place and focus the laser. Use the program to move the laser to each corner of your cut and make sure that the material covers everything. Now move the laser somewhere in the middle for focusing. Inside the laser cutter, there is generally a spacer you can use to measure the proper distance to the material. You can use the controls on the laser cutter to move the bed up or down until the laser is the proper distance from the material.

<subsection>Set Power, Speed, Thickness</subsection>

Lasercutter software often has a database of many materials which makes it easy to automatically find the speed and power you need. If you know what you are doing, you can also set power and speed manually. Generally the red color is used for cuts and the black color is used for etching.

Advanced tip: You can use more colors to set more different kinds of cuts or gaurantee that cuts happen in a particular order. For example, if you are cutting concentric circles, you may want to be sure the inside cuts happen before the outside cuts to avoid having pieces move during the cutting process.

<figure>
  <p><img src="CURRENT/laser-cutting-process3.png" style="width:4in" />  
    <figcaption>A Laser Cutter (Universal Laser System PLS150D)</figcaption>
</figure>

<subsection>Don't Forget Safety!</subsection>

You then typically have two things left to do.

First, you need to turn the ventilation on, so the dust particles that are created during the cutting process are sucked away.

Second, you need to turn the compressor on that puts the lens chamber under pressure (this prevents the dirt particles from entering the lens chamber and getting stuck to the lens, which then cause burn spots on the lens and eventually break it).

<subsection>Start the Laser Cutter</subsection>

Before you start the laser cutter, double check that you have done all of the following:

1. The material is inside the laser cutter flush against a corner
2. Your cut in the software is all over material
3. The laser is focused
4. The power and speed are appropriate for the material you are using
5. The ventilation is on
6. The compressor is on

If all of that is okay, you are ready to hit start! Be sure to watch the laser cutter the entire time it is running. If something goes wrong, calmly hit pause on the laser cutter, and ask for help as necessary.

<section>Buying materials</section>

You can try to find free material by asking around in makerspaces. Often they might have scrap pieces that you could use if you want to cut something small. Most likely, if you want to cut something that is a particular color or large, you will have to buy your own material

<subsection>Stores</subsection>

Altec Plastics is located just 15 minutes away by redline. They have a good selection of reasonably priced plastics, and are perfect if you want to be able to make the cut ASAP.

<figure>
  <p><img src="CURRENT/altec-plastics.png" style="width:3in" />  
    <img src="CURRENT/altec-plastics-2.png" style="width:3in" />  
    <figcaption>How to get to the store and what you might find there</figcaption>
</figure>

<subsection>Online</subsection>

You can also order your materials online! You might be able to order with free shipping from Amazon, but if not, you might consider placing a group order with other classmembers to save on an expensive shipping cost. Remember that when you order materials online, they often won't come for at least 2 days!

<section>On Campus Laser Cutters</section>

By taking this class, you will have access to the IDC and EDS laser cutters. (?)

- IDC: Once you have card access, you will be able to use the shop 8am-5pm Mon-Fri, and the main space 24/7
- EDS: Hours may vary, but are typically 9-5 Mon-Fri. Note that the EDS is often in use for other classes. You can check the schedule at http://eds.mit.edu/hours.
- Other Maker Spaces: You can find other maker spaces with laser cutters [online through Project Manus](http://project-manus.mit.edu/) or [using the app Mobius](http://project-manus.mit.edu/about-mobius).


<section>Settings for Different Drawing Programs</section>

As mentioned above, any 2D drawing program should work for laser cutting. However, for any program you use, make sure that cut lines are pure red (RGB 255 0 0) and as thin as the program allows (.0001pt or 'hairline'). If you use text, you should convert it to path.

Here are some alternatives to Illistrator:

- Inkscape
- OpenDraw (OpenOffice)

<section>Operating Different Types of Laser Cutters</section>

You will likely need to be trained on every new laser cutter you want to use. These guidelines will help you use most laser cutters and should work fine for the laser cutters in the IDC and EDS.

XXX