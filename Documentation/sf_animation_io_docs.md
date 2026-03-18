# Rig management

# Registering rig

In the context of Starfield, there can be no animation without a rig. Generally, before importing or exporting the animation, one needs to register the rig into the Starfield Animation Blender addon.

## On what registering does

Registering a rig moves it to the addon folder, making it accessible in the drop-down list when you import any animation. As there can be no animation without a rig, it is expected for the user to register the rig before attempting to import an animation. Rigs are imported at: **tool\_animation\_io\\Assets\\Rigs**, and the obsolete rigs can be safely deleted by the user by finding the addon folder and going to that subpath.

## Process

To activate the search menu, press the following keybinding:  
![](Documentation/sfanim_image1.png)

To register the rig, search for it:  
![](Documentation/sfanim_image2.png)

You will see the following menu:  
![](Documentation/sfanim_image3.png)

## Explanation

**Name:** The name rig will be registered as. Will be visible in UI.  
**Existing rigs:** A list of every rig registered before.

After registering the rig, you can import or export the animations that are made for that rig. Please note the animations unsuitable for the rig, will look wrong.

# Importing rig

To import a rig, find File \-\> Import \-\> Starfield Rig (.rig).  
![](Documentation/sfanim_image4.png)  
After clicking, a file picker will open. Find a Starfield .rig file you want to import (generally located at characterassets folder of extracted .ba2), and import it.

An example of a human male rig imported:  
![](Documentation/sfanim_image5.png)

# Manipulating rig

The addon introduces a new panel, named Starfield Animation Management. In the context of managing a rig, it can be used for in-depth adjustment of the rig. It is expected for the user to find and open the panel.

To edit the bone properties, select a bone, and expand the required headers on the panel:  
![](Documentation/sfanim_image6.png)  
*Tip: By default, the addon shows only the data of a selected bone. To make it show data of every bone \- which may display a lot of data, click the **Show all selected** checkmark.*

## Property explanation

**Index:** The index of the bone, starting at zero (Root bone has index 0\)  
**Mirror:** Indicates if the bone belongs to a symmetrical pair. Evaluated second bone name is shown next to the value \- in this example, L\_Clavicle has R\_Clavicle as a Mirror bone, and vice-versa \- R\_Clavicle has Mirror bone set to R\_Clavicle index. Not every bone has this property.  
**Type:** Options are Default or Twist; for regular use-cases, picking **Default** is recommended.

## Twist bone property explanation

The extra panel header is shown if the bone is a twist bone. Not every bone is a twist bone.  
**Driver index:** Index of a bone that drives the twist bone. Evaluated bone name is shown next to the index.  
**Driver weight:** Weight of the driver.

## Bone Mapping

![](Documentation/sfanim_image7.png)  
Bone Mapping is another section on the panel, which lists bones and what are they mapped as. On custom rigs that are intended to be exported as a .rig file to be used in-game, it is recommended to have the bones mapped closely to how vanilla rigs do it. For example, Root bone should be mapped as Root, and such.

## Exporting Rig

![](Documentation/sfanim_image8.png)  
For some projects, you may want to export a custom rig from Blender. At first, make sure your object is an armature with “Is Rig” checkmark checked.

Navigate to File \-\> Export \-\> Starfield Rig (.rig)  
![](Documentation/sfanim_image9.png)  
A file picker will appear, where you can select where your .rig file will be exported.

# Rig Structure

## “Static” Rig

Static rigs, such as doors, are a great starting point for animating as it doesn’t require any skinning or complicated behaviors. Just an open/close animation or even a single idle looped as we see in the example below.

![](Documentation/sfanim_image10.png)

The nif and rig are paired via NiNode’s and unique strings.  
![](Documentation/sfanim_image11.png)  
The top most NiNode is the object itself, and the next NiNode down should be where the root bone appears in your model with a matching name. The geometry nodes may or may not need to have a similar name followed by ‘:’ and an iterative number, however it is advised to follow this practice as it is common in native assets.

![](Documentation/sfanim_image12.png)

For your model, the NiNode should have the position data offset from its parent, just as the transform of its corresponding bone in the rig appears. 

The geometry node should be set to a default position (ie xyz \= 0,0,0; xyzw \= 0,0,0,1; scale \= 1.0).

For static animations, BSX flags Havok and Complex appear to be sufficient but this is unconfirmed.

# Docs: Animation

# Importing Animation

Before importing an animation, make sure to register the appropriate rig \- in other cases, it will be impossible to import it as the animation cannot exist without a rig.

Importing an animation can be done as File \-\> Import \-\> Starfield Animation (.af)  
![](Documentation/sfanim_image13.png)

It will open a file picker, where you can navigate to an .af file you wish to import. The text under every option should be descriptive enough.  
![](Documentation/sfanim_image14.png)

When you finish setting up the settings, import the .af animation.  
![](Documentation/sfanim_image15.png)
